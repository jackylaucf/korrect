import asyncio
import yaml
from korrect.model import KorrectModel
import os
import json
from korrect.methods.tool import google_search

class KorrectExtractor:
    def __init__(self, prompt_template_location):
        self.prompt_template_location = prompt_template_location
        self.model = KorrectModel('openai', 'gpt-3.5-turbo')

    def extract_claim(self, response):
        with open(os.path.join(self.prompt_template_location, "extraction.yaml")) as f:
            self.claim_prompts = yaml.load(f, Loader=yaml.FullLoader)
            claim_prompt = self.claim_prompts['knowledge_qa']
            templated = [
                    {"role": "system", "content": claim_prompt['system']},
                    {"role": "user", "content": claim_prompt['user'].format(input=response)},
                ]
            self.claims = json.loads(self.model.prompt(messages=templated))
    
    def extract_query(self):
        with open(os.path.join(self.prompt_template_location, "query.yaml")) as f:
            self.query_prompts = yaml.load(f, Loader=yaml.FullLoader)
            query_prompt = self.query_prompts['knowledge_qa']
            templated = [[
                {"role": "system", "content": query_prompt['system']},
                {"role": "user", "content": query_prompt['user'].format(input=claim['claim'] if 'claim' in claim else '')},
            ] for claim in self.claims]

            self.queries = [json.loads(self.model.prompt(messages=template)) for template in templated]
    
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

            self.validated = [json.loads(self.model.prompt(messages=template)) for template in templated]