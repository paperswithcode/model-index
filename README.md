# model-index: maintain a source of truth for ML models

`model-index` has two goals:
- Make it easy to maintain a source-of-truth index of Machine Learning models and results 
- Browse this source-of-truth index on [Papers with Code](https://paperswithcode.com/)

The main design principle of `model-index` is **flexibility**. You can store your model metadata however is the
most convenient for you - as JSONs, YAMLs or as annotations inside markdown. `model-index` provides a convenient
way to collect all this metadata into a single file that's browsable, searchable and comparable.

You can use this library locally or choose to upload the metadata to [Papers with Code](https://paperswithcode.com)
to have your library featured on the website. 

## How model-index works

There is a root file for the model index: `model-index.yml` that contains (or links to) all the metadata. 
An example with a single model:

```yaml
Models:
  - Name: Inception v3
    Architecture:
      - Auxiliary Classifier
      - Inception-v3 Module
    Metadata:
      FLOPs: 11462568384
      Parameters: 23834568
      Epochs: 90
      Batch Size: 32
      Training Data: ImageNet  
      Training Techniques: 
        - RMSProp
        - Weight Decay
        - Gradient Clipping
        - Label Smoothing
      Training Resources: 8x V100 GPUs  
    Results:
      - Task: Image Classification
        Dataset: ImageNet
        Metrics:
          Top 1 Accuracy: 74.67%
          Top 5 Accuracy: 92.1%
    Paper: https://arxiv.org/abs/1512.00567v3
    Code: https://github.com/rwightman/pytorch-image-models/blob/timm/models/inception_v3.py#L442
    Weights: https://download.pytorch.org/models/inception_v3_google-1a9a5a14.pth 
    README: docs/inception-v3-readme.md
```

### Model Collections

To keep related model together, you can create Collections. The metadata format for collections is the same as for models
and all member models **inherit** all the metadata and can over-ride it if necessary. 

```yaml
Collections:
  - Name: Inception v3
    Architecture:
      - Auxiliary Classifier
      - Inception-v3 Module
    Metadata:
      Training Data: ImageNet  
      Training Techniques: 
        - RMSProp
        - Weight Decay
        - Gradient Clipping
        - Label Smoothing
      Training Resources: 8x V100 GPUs
    Paper: https://arxiv.org/abs/1512.00567v3
    Code: https://github.com/rwightman/pytorch-image-models/blob/timm/models/inception_v3.py#L442
    README: docs/inception-v3-readme.md

Models:
  - Name: Inception v3 - 90 epochs
    In Collection: Inception v3 
    Metadata:
      Epochs: 90
    Results:
      - Task: Image Classification
        Dataset: ImageNet
        Metrics:
          Top 1 Accuracy: 74.67%
          Top 5 Accuracy: 92.1%
    Weights: https://download.pytorch.org/models/inception_v3_google-1a9a5a14.pth
  
  - Name: Inception v3 - 120 epochs
    In Collection: Inception v3
    Metadata:
      Epochs: 120
    Results:
      - Task: Image Classification
        Dataset: ImageNet
        Metrics:
          Top 1 Accuracy: 75.1%
          Top 5 Accuracy: 93.1%
    Weights: https://download.pytorch.org/models/inception_v3_google-120-1a9a5afd.pth
```

In this example we have two variants of the `Inception v3` model, one trained for 90 epochs (the original from the paper)
and an additional model trained for additional 30 epochs - `Inception v3 - 120 epochs`.  

### Including metadata from other files

It might not be convenient to maintain a huge `model-index.yml` file in your repository. So `model-index` make it easy
to stitch together metadata from many different sources. 

#### Importing fields

For each field that expects a list or dictionary, you can provide a filename instead. For example:

```yaml
Models:
  - Name: Inception v3
    Metadata: models/metadata/inception_v3.yml
    Results: models/metadata/inception_v3_results.json
``` 

Both YAML and JSON are supported. The content of the file needs to conform to the structure  

#### Importing a whole YAML file

Import in your `model-index.yml`:

```yaml
Import:
  - models/metadata/inception_v3.yml
```

Here the `inception_v3` yaml file has the same format as the root `model-index.yml` file. 

#### Importing a whole JSON file

The imported file can also be in JSON format, as long as it has the same structure as the YAML:

```yaml
Import:
  - models/metadata/mnasnet_100.json
  - models/metadata/mnasnet_200.json
```

#### Importing a whole Markdown file

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

#### Importing multiple files

Specify wildcards to import multiple files: 

```yaml
Import:
  - docs/*.md
  - models/metadata/*.json
```

### Programmatic `markdown-index.yml`

It is possible to generate all the data programatically as well. We provide a set of Data Classes to hold the metadata,
link files together and check for any syntax errors. 

## Checking the consistency of the model index

To ensure the model index doesn't have any errors in its metadata you can run an automated check on the whole
index, or an individual file:

via the CLI:
```shell script
mi check     # check the whole index
mi check models/metadata/inception_v3.json    # check one file
```

or programatically:

```python
import modelindex as mi

mi.check()    # check the whole index
mi.check("models/metadata/inception_v3.json")  # single file
```

## Querying the model-index

It is possible to query the information in the model index through the CLI tool or programatically:

To find all models with "Inception" in their name:

```shell script
mi search "Name: Inception"
```

or programmatically: 

```python
import modelindex as mi

mi.search("Name: Inception")
``` 

## Uploading to Papers with Code

To feature your library on Papers with Code, get in touch with `hello@paperswithcode.com` and the model index
of your library will be automatically included into Papers with Code. 







