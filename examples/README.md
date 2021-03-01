# An example how to use model-index

This is an example of how to use `model-index` inside your repository. 

The `model-index.yml` is the main file tying together all the metadata. We recommend putting it in the root
of your repository. 

Inside the `model-index.yml` you can link metadata from separate markdown and yaml/json files. 

## Option 1: Markdown files

You can see the full example in [option1-markdown](option1-markdown) directory. 

To store your metadata in markdown, add the model-index metadata **in a comment in the markdown file**. 
Using a comment ensures that the file is still human readable in GitHub, but also contains all the metadata needed by model-index. 

You can see an example of usage inside markdown here: [docs/alexnet.md](https://raw.githubusercontent.com/paperswithcode/model-index/main/examples/option1-markdown/docs/alexnet.md)
and [docs/resnet.md](https://raw.githubusercontent.com/paperswithcode/model-index/main/examples/option1-markdown/docs/resnet.md).  

To include markdown files into the model index, simply import them into the root [model-index.yml](https://github.com/paperswithcode/model-index/blob/main/examples/option1-markdown/model-index.yml) file:

```yaml
Import:
  - docs/*.md
```

## Option 2: YAML/JSON files

You can see the full example in [option2-yaml](option2-yaml) directory.

To use `model-index` like this, you can either simply add all of your model metadata into `model-index.yml`,
or split it up into multiple files as shown in [model-index.yml](https://github.com/paperswithcode/model-index/blob/main/examples/option2-yaml/model-index.yml) file:

```yaml
Models:
- Name: AlexNet
  Metadata: metadata/alexnet.yml
  README: docs/alexnet.md
  Code: https://github.com/pytorch/vision/blob/5a315453da5089d66de94604ea49334a66552524/torchvision/models/alexnet.py#L53
  Config: https://github.com/pytorch/vision/tree/master/references/classification
  In Collection: AlexNet
  Results:
  - Dataset: ImageNet
    Metrics:
      Top 1 Accuracy: 56.55%
      Top 5 Accuracy: 79.09%
    Task: Image Classification
  Weights: https://download.pytorch.org/models/alexnet-owt-4df8aa71.pth
```

In this example we've split out the metadata into separate files in [metadata](option2-yaml/metadata) and
linked it inside model definitions like this: `Metadata: metadata/alexnet.yml` (pointing to [metadata/alexnet.yml](https://github.com/paperswithcode/model-index/blob/main/examples/option2-yaml/metadata/alexnet.yml)). We did the same with READMEs that
are linked like this: `README: docs/alexnet.md` (pointing to [metadata/alexnet.md](https://raw.githubusercontent.com/paperswithcode/model-index/main/examples/option2-yaml/docs/alexnet.md)).  

You can see how this looks like in the example [model-index.yml](https://github.com/paperswithcode/model-index/blob/main/examples/option2-yaml/model-index.yml) file

## Option 3: Mix-and-match

These two options are not exclusive. You can have some of your model metadata defined in markdown, and other
in YAML/JSON files. You can also import YAML/JSON files into markdown. 

You can mix-and-match as long as everything is imported into the root `model-index.yml`.

# Documentation

For more information please refer to the [official documentation](https://model-index.readthedocs.io/en/latest/). 