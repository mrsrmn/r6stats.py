# r6stats.py

r6stats.py is a Python wrapper for the R6Stats.com API

## Usage

```python
import r6stats

stats = r6stats.Stats(key="")
generic_stats = stats.get_generic_stats(username="BikiniBodhi", platform=r6stats.Platform.pc)

print(generic_stats.wins)
```

More examples are at [the examples folder](https://github.com/MakufonSkifto/r6stats.py/tree/master/examples)

## Errors

The module will raise `KeyError` if the given thing is not found
