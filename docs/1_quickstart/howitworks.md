# How it works

There is a root file for the model index: `model-index.yml` that contains (or links to) all the 
metadata in a consistent format. An example with a single model:

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

## Linking files

You don't have to keep everything in a single file. You can split the model
index into separate files and then link to them in the main `model-index.yml`
file (with `inception-v3.yml` containing the same model dictionary as above):

```yaml
Models:
  - models/inception-v3.yml
```

See [Including metadata from other files](./creating.html#including-metadata-from-other-files) for more information.

