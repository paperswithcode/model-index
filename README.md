# model-index: maintain a source of truth for ML models

`model-index` has two goals:
- Make it easy to maintain a source-of-truth index of Machine Learning model metadata 
- Enable the community browse this model metadata on [Papers with Code](https://paperswithcode.com/)

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
      Architecture:
        - Auxiliary Classifier
        - Inception-v3 Module
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

The fields present in this file as **common fields** that are automatically recognized by Papers with Code
and enable comparison across different models. You can also add any number of **custom fields** that are
specific to your model or library. 

Models, Metadata and Results can also be in separate files and just be referenced:

```yaml
Models:
  - models/inception-v3.yml
```

## Getting started

Check out our [official documentation](https://model-index.readthedocs.io/en/latest/) on how to get started. 

## Uploading to Papers with Code

To feature your library on Papers with Code, get in touch with `hello@paperswithcode.com` and the model index
of your library will be automatically included into Papers with Code. 







