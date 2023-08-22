## Korrect

<img alt="GitHub commit activity (branch)" src="https://img.shields.io/github/commit-activity/t/kortex-labs/korrect"> <a href="https://cla-assistant.io/kortex-labs/korrect"><img src="https://cla-assistant.io/readme/badge/kortex-labs/korrect" alt="CLA assistant" /></a>

Korrect is a light-weight performance testing framework for LLMs.

To get started:

```python
from korrect import Korrect

k = Korrect()
```

then navigate to `http://localhost:8501/` and you'll find the UI:

![demo asset](https://github.com/kortex-labs/korrect/blob/6448ec72b44695cee6a284a7c7b6647debaeaa9c/korrect/asset/demo.png)

right now, korrect only supports openai models.

Korrect also supports experiments in no-ui mode:

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

- [ ] fix import error ModuleNotFound
- [ ] add Huggingface model support
- [ ] fix async await calls
- [ ] dockerize
- [x] env config
- [x] fix yaml file directory error

### Contributions

To contribute, please see our [contribution guide.](./CONTRIBUTING.md)

### Community

Join our discord community [here](https://discord.gg/stGaVVhq) <img src="https://github.com/kortex-labs/korrect/blob/6448ec72b44695cee6a284a7c7b6647debaeaa9c/korrect/asset/discord.png" alt="drawing" width="35" height="20"/>