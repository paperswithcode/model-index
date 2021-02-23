# Creating a new index

The model index is just a collection of interlinked yaml/json/markdown files,
so you can just create them yourself. 

We also provide a set of classes that make the creation easy (docs coming soon!). 

## Including metadata from other files

It might not be convenient to maintain a huge `model-index.yml` file in your repository. So `model-index` make it easy
to stitch together metadata from many different sources. 

### Importing fields

For each field that expects a list or dictionary, you can provide a filename instead. For example:

```yaml
Models:
  - Name: Inception v3
    Metadata: models/metadata/inception_v3.yml
    Results: models/metadata/inception_v3_results.json
``` 

Both YAML and JSON are supported. The content of the file needs to conform to the expected structure specified above. 

### Importing a whole YAML file

Import in your `model-index.yml`:

```yaml
Import:
  - models/metadata/inception_v3.yml
```

Here the `inception_v3` yaml file has the same format as the root `model-index.yml` file. 

### Importing a whole JSON file

The imported file can also be in JSON format, as long as it has the same structure as the YAML:

```yaml
Import:
  - models/metadata/mnasnet_100.json
  - models/metadata/mnasnet_200.json
```

### Importing a whole Markdown file

```yaml
Import:
  - docs/rexnet.md
```

Instead of specifying the `README` field of the model, you can add the model metadata directly into the markdown file.

Include the metadata in YAML format in a comment, with a `Type: model-index` key to indicate that it should be parsed
by the `model-index` library. So, the `rexnet.md` would look like this:

```markdown
<!--
Type: model-index
Models:
  - Name: RexNet
    Metadata: ../models/metadata/rexnet.json        
    Results: ../models/metadata/rexnet_results.json
-->
# Summary

Rank Expansion Networks (ReXNets) follow a set of new design principles for designing bottlenecks in image classification models

## How to use this model

....
``` 

### Importing multiple files

Specify wildcards to import multiple files: 

```yaml
Import:
  - docs/*.md
  - models/metadata/*.json
```

## Programmatic `markdown-index.yml`

It is possible to generate all the data programatically as well. More docs to come on this soon!
