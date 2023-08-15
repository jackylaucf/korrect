## Korrect

```python
from korrect import Korrect

k = Korrect()
```

then navigate to `http://localhost:8501/` and you'll find the UI:

<!-- ![demo asset](korrect/assets/demo.jpeg) -->

right now, korrect only supports openai models.

please don't forget to export your OPENAI_API and SERPER tokens as env vars!

Join our discord community [here](https://discord.gg/stGaVVhq)

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