# ModelIndex

The `model-index.yml` is the root file for the model index. It contains or links
to all the models available in the index. 

ModelIndex is a dict with three possible fields:

- `Models` - a list of [Model](model.html) dicts, or a list of files to import 
Model dicts from. 
- `Collections` - a list of [Collections](collection.html) dicts, or a list
of files to import Collection dicts from.  
- `Import` - a list of files to import additional ModelIndex files from 
(e.g. if you want to split the `model-index.yml` file into multiple parts)

All field names are case-insensitive. 

## A full example

An example of the full ModelIndex dict:

```yaml
Collections:
  - Name: Mask R-CNN
    Metadata:
      Training Data: COCO
      Training Techniques: 
        - SGD with Momentum
      Training Resources: 8x V100 GPUs
      Architecture:
        - RoI Align
        - RPN
    Paper: https://arxiv.org/abs/1703.06870v3
    README: docs/maskrcnn.md

Models:
  - Name: Mask R-CNN (R101-C4, 3x)
    In Collection: Mask R-CNN 
    Metadata:
      inference time (s/im): 0.145
      train time (s/iter): 0.652
      Training Memory (GB): 6.3
    Results:
      - Task: Object Detection
        Dataset: COCO minival
        Metrics:
          box AP: 42.6
      - Task: Instance Segmentation
        Dataset: COCO minival
        Metrics:
          mask AP: 36.7
    Weights: https://dl.fbaipublicfiles.com/detectron2/COCO-InstanceSegmentation/mask_rcnn_R_101_C4_3x/138363239/model_final_a2914c.pkl
  
  - Name: Mask R-CNN (R50-C4, 3x)
    In Collection: Mask R-CNN 
    Metadata:
      inference time (s/im): 0.111
      train time (s/iter): 0.575
      Training Memory (GB): 5.2
    Results:
      - Task: Object Detection
        Dataset: COCO minival
        Metrics:
          box AP: 39.8
      - Task: Instance Segmentation
        Dataset: COCO minival
        Metrics:
          mask AP: 34.4
    Weights: https://dl.fbaipublicfiles.com/detectron2/COCO-InstanceSegmentation/mask_rcnn_R_50_C4_3x/137849525/model_final_4ce675.pkl

Import:
  - additional_models.yml
```

Where `additional_models.yml` is a file in the same format and that
will be merged in. 