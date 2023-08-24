import os
from subprocess import PIPE, Popen

from korrect.experiment import KorrectExperiment

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

class Korrect():
    def __init__(self, ui=True, credentials: dict = {}):
        if ui:
            self.ui = self._launch_ui()
        else:
            # {
            #     "OPENAI_API_KEY": "****",
            #     "SERPER_API_KEY": "****"
            # }
            if len(credentials) == 0:
                raise Exception("credentials should not be empty with no-ui mode")
            self.credentials = credentials
            self._set_env_vars()
    
    def _set_env_vars(self):
        for name, credentials in self.credentials.items():
            os.environ[name] = credentials
    
    def _launch_ui(self):
        python_cmd = 'python' if os.name == 'nt' else 'python3'
        Popen([python_cmd, "-m", "streamlit", "run", os.path.join(BASE_PATH, "ui.py")])

    def close(self):
        self.ui.kill()

    def create_experiment(self, parameters: dict):
        self.experiment = KorrectExperiment(parameters)
        return self.experiment
