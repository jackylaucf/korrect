from korrect.model import KorrectModel
import json, os
from subprocess import Popen
from korrect.experiment import KorrectExperiment

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

class Korrect():
    def __init__(self):
        self.ui = self._launch_ui()
    
    def _launch_ui(self):
        return Popen(["python3", "-m", "streamlit", "run", os.path.join(BASE_PATH, "ui.py")])
    
    def close(self):
        self.ui.kill()

    def create_experiment(self, parameters: dict = {}):
        # {
        #     {"model_type": "OpenAI Chat", "model": "gpt-3.5-turbo"},
        #     {"model_type": "OpenAI Chat", "model": "gpt-4"}
        # }
        self.experiment = KorrectExperiment(parameters)

