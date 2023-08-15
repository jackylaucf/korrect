import os
from korrect.methods.extractor import KorrectExtractor
import json

def fact_checking(base_path, prompt, model_type): 
        extractor = KorrectExtractor(prompt=prompt, prompt_template_location=os.path.join(base_path, "methods/prompts"), model_type=model_type)

        extractor.extract_claim()

        extractor.extract_query()

        extractor.get_evidence()

        extractor.validate_claim_based_on_evidence()
        
        # print(f"Question: {prompt}")
        # print(f"Answer: {resp_prompt}")
        # print(json.dumps(extractor.claims, indent=4))
        # print(json.dumps(extractor.validated, indent=4))
        return prompt, extractor.response, extractor.claims, extractor.validated