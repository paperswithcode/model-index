# How it works

There is a root file for the model index: `model-index.yml` that contains (or links to) all the 
metadata in a consistent format. An example with a single model:

```yaml
Models:
  - Name: Inception v3
    Metadata:
      FLOPs: 5731284192
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
      Training Time: 24 hours
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

The fields present in this file are **common fields** that are automatically recognized by Papers with Code
and enable comparison across different models. You can also add any number of **custom fields** that are
specific to your model or library. 

For example:

```yaml
Models:
  - Name: My new model
    Metadata:
      Training Time: 24 hours
      my parameter: 120
      my parameter2: 
        sub parameter1: value 1
        sub parameter2: value 2
      
      
```

So you can mix-and-match from our set of common field and any other field you want to add.

We recommend putting the `model-index.yml` file in the root of your repository (so that relative links such as 
`docs/inception-v3-readme.md` are easier to write), but you can also put it anywhere else in the repository (e.g.
int your `docs/` or `models/` folder). 

## Storing metadata in markdown files

Metadata can also be directly stored in model's README file. For example in this `docs/rexnet.md` file:

```markdown
<!--
Type: model-index
Name: RexNet
Metadata: 
  Epochs: 400
  Batch Size: 512
Paper: https://arxiv.org/abs/2007.00992v1
-->

# Summary

Rank Expansion Networks (ReXNets) follow a set of new design 
principles for designing bottlenecks in image classification models.

## Usage

import timm
m = timm.create_model('rexnet_100', pretrained=True)
m.eval()
```

In this case, you just need to include this markdown file into the global `model-index.yml` file:

```yaml
Models:
  - docs/rexnet.md
```

