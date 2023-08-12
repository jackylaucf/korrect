## Korrect

```python
from korrect import Korrect

k = Korrect("openai", "gpt-3.5-turbo")
k.fact_checking("How many sons had teddy roosevelt in total?")

```

right now, korrect only supports openai models.

please don't forget to export your OPENAI_API and SERPER tokens as env vars!