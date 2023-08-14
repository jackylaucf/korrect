## Korrect

```python
from korrect import Korrect

k = Korrect("openai", "gpt-3.5-turbo")
k.fact_checking("How many sons had teddy roosevelt in total?")

```

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
- [x] fix yaml file directory error
- [ ] add Huggingface model support
- [ ] fix async await calls
- [ ] dockerize
- [ ] env config