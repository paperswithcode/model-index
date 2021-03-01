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