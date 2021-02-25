# Importing metadata

It might not be convenient to maintain a huge `model-index.yml` file in your repository. So `model-index` make it easy
to stitch together metadata from many different sources. 

Data can be imported from other YAML files, JSON files and from Markdown files. 

## Importing fields

For [Models](../2_datamodels/model.html), [Metadata](../2_datamodels/model.html#metadata) and 
[Results](../2_datamodels/model.html#result) you can provide a filename instead of actual values. For example:

```yaml
Models:
  - Name: Inception v3
    Metadata: models/metadata/inception_v3.yml
    Results: models/metadata/inception_v3_results.json
``` 

Both YAML and JSON are supported. The content of the file needs to conform to the expected 
structure specified for [Models](../2_datamodels/model.html), [Metadata](../2_datamodels/model.html#metadata) and 
[Results](../2_datamodels/model.html#result). 

So in this case, `incdeption_v3.yml` could look like this:

```yaml
Batch Size: 120
Epochs: 100
Dropout: 0.1
```

and `inception_v3_results.json` could look like this:

```json
[
  {
    "Task": "Image Classification",
    "Dataset": "ImageNet ReaL",
    "Metrics": {
      "Accuracy": "90.2%"
    }   
  }
]
```

## Importing a whole YAML file

Import in your `model-index.yml`:

```yaml
Import:
  - models/metadata/inception_models.yml
```

Here the `inception_models.yml` file has to be in [ModelIndex](../2_datamodels/modelindex.html) format
(i.e. the same as the root `model-index.yml` file). For example:

```yaml
Collection:
  - Name: Inception models
Models:
  - Name: Inception v3 (original)
    In Collection: Inception models
    Metadata:
      Epochs: 90
  - Name: Inception v3 (retrained)
    In Collection: Inception models
    Metadata:
      Epochs: 120
```

## Importing a whole JSON file

The imported file can also be in JSON format, as long as it has the same structure as the YAML:

```yaml
Import:
  - models/metadata/mnasnet_100.json
  - models/metadata/mnasnet_200.json
```

So one of these JSON files could look like:

```json
{
  "Epochs": 120,
  "Dropout": 0.2
}
```

## Importing a whole Markdown file

```yaml
Import:
  - docs/rexnet.md
```

Instead of specifying the `README` field of the model, you can add the model metadata directly into the markdown file.

Include the metadata in YAML format in a comment, with a `Type: model-index` key to indicate that it should be parsed
by the `model-index` library. So, the `rexnet.md` could look like this:

```markdown
<!--
Type: model-index
Models:
  - Name: RexNet
    Metadata: ../models/metadata/rexnet.json        
    Results: ../models/metadata/rexnet_results.json
-->
# Summary

Rank Expansion Networks (ReXNets) follow a set of new design principles for 
designing bottlenecks in image classification models.

## How to use this model

....
``` 

## Using wildcards to import multiple files

Specify wildcards to import multiple files: 

```yaml
Import:
  - docs/*.md
  - models/metadata/*.json
```
