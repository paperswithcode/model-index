<!--
Type: model-index
Collections:
- Name: ResNet
  Paper: '1512.03385'
  Metadata:
    Architecture:
      - 1x1 Convolution
      - Bottleneck Residual Block
      - Batch Normalization
      - Convolution
      - Global Average Pooling
      - Residual Block
      - Residual Connection
      - ReLU
      - Max Pooling
      - Softmax
  README: mi-readmes/resnet.md
Models:
- Name: ResNet-101 
  Code: https://github.com/pytorch/vision/blob/5a315453da5089d66de94604ea49334a66552524/torchvision/models/resnet.py#L304
  Config: https://github.com/pytorch/vision/tree/master/references/classification
  In Collection: ResNet
  Metadata:
    Batch Size: 32
    Epochs: 90
    FLOPs: 15667943424
    ID: resnet101
    LR: 0.1
    LR Gamma: 0.1
    LR Step Size: 30
    Momentum: 0.9
    Parameters: 44549160
    Training Data:
    - ImageNet
    Training Resources: 8x NVIDIA V100 GPUs
    Training Techniques:
    - Weight Decay
    - SGD with Momentum
    Weight Decay: 0.0001
  Results:
  - Dataset: ImageNet
    Metrics:
      Top 1 Accuracy: 77.37%
      Top 5 Accuracy: 93.56%
    Task: Image Classification
  Weights: https://download.pytorch.org/models/resnet101-5d3b4d8f.pth
- Name: ResNet-152
  Code: https://github.com/pytorch/vision/blob/5a315453da5089d66de94604ea49334a66552524/torchvision/models/resnet.py#L316
  Config: https://github.com/pytorch/vision/tree/master/references/classification
  In Collection: ResNet
  Metadata:
    Batch Size: 32
    Epochs: 90
    FLOPs: 23117674496
    ID: resnet152
    LR: 0.1
    LR Gamma: 0.1
    LR Step Size: 30
    Momentum: 0.9
    Parameters: 60192808
    Training Data:
    - ImageNet
    Training Resources: 8x NVIDIA V100 GPUs
    Training Techniques:
    - Weight Decay
    - SGD with Momentum
    Weight Decay: 0.0001
  Results:
  - Dataset: ImageNet
    Metrics:
      Top 1 Accuracy: 78.31%
      Top 5 Accuracy: 94.06%
    Task: Image Classification
  Weights: https://download.pytorch.org/models/resnet152-b121ed2d.pth
-->

# Summary

**Residual Networks**, or **ResNets**, learn residual functions with reference to the layer inputs, instead of learning unreferenced functions. Instead of hoping each few stacked layers directly fit a desired underlying mapping, residual nets let these layers fit a residual mapping. They stack [residual blocks](https://paperswithcode.com/method/residual-block) ontop of each other to form network: e.g. a ResNet-50 has fifty layers using these blocks. 

## How do I load this model?

To load a pretrained model:

```python
import torchvision.models as models
resnet18 = models.resnet18(pretrained=True)
```

Replace the model name with the variant you want to use, e.g. `resnet18`. You can find 
the IDs in the model summaries at the top of this page.

To evaluate the model, use the [image classification recipes]((https://github.com/pytorch/vision/tree/master/references/classification)) from the library.

```bash
python train.py --test-only --model='<model_name>'
```

## How do I train this model?

You can follow the [torchvision recipe](https://github.com/pytorch/vision/tree/master/references/classification) on GitHub for training a new model afresh.

## Citation

```BibTeX
@article{DBLP:journals/corr/HeZRS15,
  author    = {Kaiming He and
               Xiangyu Zhang and
               Shaoqing Ren and
               Jian Sun},
  title     = {Deep Residual Learning for Image Recognition},
  journal   = {CoRR},
  volume    = {abs/1512.03385},
  year      = {2015},
  url       = {http://arxiv.org/abs/1512.03385},
  archivePrefix = {arXiv},
  eprint    = {1512.03385},
  timestamp = {Wed, 17 Apr 2019 17:23:45 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/HeZRS15.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```