# Model

A model represents all the information about a Machine Learning model. 

Model is represented by a dict with these common fields:

- `Name` - the only required field, with the name of the model. 
- `Metadata` - a dict of [Metadata](#metadata), or a link to a file (yml/json) containing it.
- `Results` - a list of [Result](#result) dicts.
- `Paper` -  URL to the paper, or a dict with paper title, url and   
- `Code` - link to code snippet snippet
- `Weights` - link to download the pretrained weights
- `Config` - link to the config file used for training
- `README` - the content of, or a link to the README.md file for the model
- `Image` - path or URL to an image for this model
- `In Collection`- name of the [Collection](collection.html) to which this model belongs.  

The fields above will be automatically recognized by model-index, but you can
also add any number of custom fields to it. 

All field names are case-insensitive. 

## Metadata

Metadata is a dict of common and custom metadata. The common
fields are:

- `FLOPs` - The number of FLOPs of the model
- `Parameters` - The total number of parameters of the model
- `Epochs` - Number of training epochs
- `Batch Size` - Input batch size
- `Training Data` - Dataset names on which the models are trained (for full see [Datasets](https://paperswithcode.com/datasets) on Papers with Code)
- `Training Techniques` - A list of training techniques (for the full list see 
[Methods](https://paperswithcode.com/methods) on Papers with Code)
- `Training Resources` - The hardware used for training
- `Training Time` - How many hours or days it takes to train.
- `Architecture` - A list of architectural features of the model (for the full list see 
[Methods](https://paperswithcode.com/methods) on Papers with Code)

You can also add any other custom field that is specific to your model.

## Result

Result is a dict capturing the evaluation results of the model. It has
these fields:

- `Task` - Name of the task (for full see [Benchmarks](https://paperswithcode.com/sota) on Papers with Code)
- `Dataset` - Name of the dataset (for full see [Datasets](https://paperswithcode.com/datasets) on Papers with Code)
- `Metrics` - a list of dictionaries with metrics. For relevant metrics consult the see [Benchmarks](https://paperswithcode.com/sota) on Papers with Code.

## A full example

An example of the full model dict is shown below:

```yaml
Name: Inception v3
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
Config: configs/inception-v3-config.json
README: docs/inception-v3-readme.md
```
