## Korrect

Korrect is a light-weight testing and fact-checking framework for LLMs.

To get started:

```python
from korrect import Korrect

k = Korrect()
```

then navigate to `http://localhost:8501/` and you'll find the UI:

![demo asset](https://github.com/kortex-labs/korrect/blob/6448ec72b44695cee6a284a7c7b6647debaeaa9c/korrect/asset/demo.jpeg)

right now, korrect only supports openai models.

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
- [ ] env config
- [x] fix yaml file directory error

### Contributions

To contribute, please see our [contribution guide.](./CONTRIBUTING.md)

### Community

Join our discord community [here](https://discord.gg/stGaVVhq) <img src="https://github.com/kortex-labs/korrect/blob/6448ec72b44695cee6a284a7c7b6647debaeaa9c/korrect/asset/discord.png" alt="drawing" width="35" height="20"/>