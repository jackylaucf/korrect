import os
from korrect.methods.extractor import KorrectExtractor
import json

def fact_checking(base_path, prompt, model_type): 
        extractor = KorrectExtractor(prompt=prompt, prompt_template_location=os.path.join(base_path, "methods/prompts"), model_type=model_type)

        extractor.extract_claim()

        extractor.extract_query()

        extractor.get_evidence()

        extractor.validate_claim_based_on_evidence()

        return prompt, extractor.response, extractor.claims, extractor.validated