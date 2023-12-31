## Korrect

<img alt="GitHub commit activity (branch)" src="https://img.shields.io/github/commit-activity/t/kortex-labs/korrect"> <a href="https://cla-assistant.io/kortex-labs/korrect"><img src="https://cla-assistant.io/readme/badge/kortex-labs/korrect" alt="CLA assistant" /></a>

Korrect is a light-weight hallucination testing framework for LLMs.

To get started:

```python
from korrect import Korrect

k = Korrect(ui=True)
```

then navigate to `http://localhost:8501/` and you'll find the UI:

![demo asset](https://github.com/kortex-labs/korrect/blob/32fb7584833f621f8f4ebfebb889fa8b798d3643/asset/demo.png)

right now, korrect only supports openai models.

Korrect also supports experiments in code-only mode:

```python
credentials = {
    "OPENAI_API_KEY": "*",
    "SERPER_API_KEY": "*"
}

client = Korrect(ui=False, credentials=credentials)

parameters = {
    "prompt": "who won the Nobel Peace Prize in 2020?",
    "models": [
    {"model_type": "OpenAI Chat",
    "model_name": "gpt-3.5-turbo"},
    {"model_type": "OpenAI Chat",
    "model_name": "gpt-4"}
]}

experiment = client.create_experiment(parameters=parameters)

results = experiment.run()
```

### Development 

For development, please run:

```python
python3 -m venv myenv
source myenv/bin/activate
pip3 install -e .
```

### Roadmap

- [ ] add Huggingface model support
- [ ] fix async await calls
- [ ] dockerize
- [x] env config
- [x] fix yaml file directory error
- [x] fix import error ModuleNotFound

### Contributions

To contribute, please see our [contribution guide.](./CONTRIBUTING.md)

### Community

Join our discord community [here](https://discord.gg/stGaVVhq) <img src="https://github.com/kortex-labs/korrect/blob/6448ec72b44695cee6a284a7c7b6647debaeaa9c/korrect/asset/discord.png" alt="drawing" width="35" height="20"/>