from korrect.model import KorrectModel
from korrect.methods.extractor import KorrectExtractor
import json

class Korrect(KorrectModel):
    def __init__(self, model_type, model_name):
        super().__init__(model_type, model_name)

    def fact_checking(self, prompt):
        extractor = KorrectExtractor(prompt_template_location="./methods/prompts")

        resp_prompt = self.prompt([{"role": "user", "content": prompt}])

        extractor.extract_claim(resp_prompt)

        extractor.extract_query()

        extractor.get_evidence()

        extractor.validate_claim_based_on_evidence()
        
        print(f"Question: {prompt}")
        print(f"Answer: {resp_prompt}")
        print(json.dumps(extractor.claims, indent=4))
        print(json.dumps(extractor.validated, indent=4))

if __name__=="__main__":
    k = Korrect("openai", "gpt-3.5-turbo")
    k.fact_checking("How many sons had teddy roosevelt in total?")

