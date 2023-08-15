from korrect.model import KorrectModel
from korrect.methods.extractor import KorrectExtractor
import json, os
from subprocess import Popen

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

class Korrect():
    def __init__(self):
        self.ui = self._launch_ui()
    
    def _launch_ui(self):
        return Popen(["python3", "-m", "streamlit", "run", os.path.join(BASE_PATH, "ui.py")])
    
    def close(self):
        self.ui.kill()


#     k.fact_checking("How many sons had teddy roosevelt in total?")

