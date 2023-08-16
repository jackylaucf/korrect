

class KorrectExperiment:
    def __init__(self, parameters: dict):
        self.parameters = parameters

    def run(self):
        for config in self.parameters:
            print(config)
        