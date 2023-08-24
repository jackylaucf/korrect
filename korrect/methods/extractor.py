import asyncio
import json
import os
import yaml

from concurrent.futures import CancelledError, Future
from concurrent.futures.thread import ThreadPoolExecutor
from korrect.model import KorrectModel
from korrect.methods.tool import google_search
from openai.error import OpenAIError
from typing import Dict, List


class KorrectExtractor:
    def __init__(self, prompt, prompt_template_location, model_type):
        self.prompt_template_location = prompt_template_location
        self.model = KorrectModel(model_type, 'gpt-3.5-turbo')
        self.response = self.model.prompt([{"role": "user", "content": prompt}])

    def extract_claim(self):
        with open(os.path.join(self.prompt_template_location, "extraction.yaml")) as f:
            self.claim_prompts = yaml.load(f, Loader=yaml.FullLoader)
            claim_prompt = self.claim_prompts['knowledge_qa']
            templated = [
                    {"role": "system", "content": claim_prompt['system']},
                    {"role": "user", "content": claim_prompt['user'].format(input=self.response)},
                ]
            self.claims = json.loads(self.model.prompt(messages=templated))

    def extract_from_model(self, templates: List[List[Dict]], timeout=None) -> List[List[str]]:
        extractor_futures: List[Future] = []
        results: List[List[str]] = []
        with ThreadPoolExecutor() as executor:
            for template in templates:
                extractor_futures.append(executor.submit(lambda t: json.loads(self.model.prompt(messages=t)), template))
        for future in extractor_futures:
            try:
                results.append(future.result(timeout=timeout))
            except Exception as ex:
                print(ex)
        return results

    def extract_query(self):
        with open(os.path.join(self.prompt_template_location, "query.yaml")) as f:
            self.query_prompts = yaml.load(f, Loader=yaml.FullLoader)
            query_prompt = self.query_prompts['knowledge_qa']
            templated = [[
                {"role": "system", "content": query_prompt['system']},
                {"role": "user", "content": query_prompt['user'].format(input=claim['claim'] if 'claim' in claim else '')},
            ] for claim in self.claims]

            self.queries = self.extract_from_model(templated)
    
    def get_evidence(self):
        evidences = asyncio.run(google_search(snippet_cnt=5).run(self.queries))
        self.evidences = [[obj["content"] for obj in evidence] for evidence in evidences]
        claims = [[c] for c in self.claims]
        self.query_evidence_pair = [{"claim": c["claim"], "evidence": e} for claim in claims for c, e in zip(claim, evidences)]

    def validate_claim_based_on_evidence(self):
        with open(os.path.join(self.prompt_template_location, "validation.yaml")) as f:
            self.validation_prompts = yaml.load(f, Loader=yaml.FullLoader)
            validation_prompt = self.validation_prompts['knowledge_qa']

            templated = [
                [
                    {"role": "system", "content": validation_prompt['system']},
                    {"role": "user", "content": validation_prompt['user'].format(claim=pair['claim'], evidence=str(evidence["content"]))}
                ]
                for pair in self.query_evidence_pair
                for evidence in pair["evidence"]
            ]

            self.validated = self.extract_from_model(templated)