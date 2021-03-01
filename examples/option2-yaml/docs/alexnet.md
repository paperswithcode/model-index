# Summary

**AlexNet** is a classic convolutional neural network architecture. It consists of convolutions, max pooling and dense layers as the basic building blocks

## How do I load this model?

To load a pretrained model:

```python
import torchvision.models as models
squeezenet = models.alexnet(pretrained=True)
```

Replace the model name with the variant you want to use, e.g. `alexnet`. You can find the IDs in the model summaries at the top of this page.

To evaluate the model, use the [image classification recipes]((https://github.com/pytorch/vision/tree/master/references/classification)) from the library.

```bash
python train.py --test-only --model='<model_name>'
```

## How do I train this model?

You can follow the [torchvision recipe](https://github.com/pytorch/vision/tree/master/references/classification) on GitHub for training a new model afresh.

## Citation

```BibTeX
@article{DBLP:journals/corr/Krizhevsky14,
  author    = {Alex Krizhevsky},
  title     = {One weird trick for parallelizing convolutional neural networks},
  journal   = {CoRR},
  volume    = {abs/1404.5997},
  year      = {2014},
  url       = {http://arxiv.org/abs/1404.5997},
  archivePrefix = {arXiv},
  eprint    = {1404.5997},
  timestamp = {Mon, 13 Aug 2018 16:48:41 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/Krizhevsky14.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```