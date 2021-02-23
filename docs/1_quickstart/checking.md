# Checking an index

To ensure the model index doesn't have any errors in its metadata you can run an automated check on the whole
index, or an individual file:

via the CLI:
```shell script
$ mi check  # Check the entire index
$ mi check models/metadata/inception_v3.json    # check one file
```

or programatically:

```python
import modelindex

# check entire index
mi = modelindex.load("<path to model-index.yml>")
mi.check()

# check one file
mi = modelindex.load("models/metadata/inception_v3.json")
mi.check()
```




