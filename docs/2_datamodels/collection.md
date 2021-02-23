# Collection

To keep related model together, you can create Collections. The metadata format for collections is the same as for models
and all member models **inherit** all the metadata and can override/add to it. 

The fields of a collection are exactly the same as fields of a [Model](model.html) - see the description there. 

## A full example

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
```

In this example we have two variants of the `Mask R-CNN` model, one with a ResNet-50 backbone and one with a ResNet-101 backbone. These models belong together as variants of the Mask R-CNN, so we link them via a `Mask R-CNN` model collection.
