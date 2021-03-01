# An example how to use model-index

This is an example of how to use `model-index` inside your repository. 

The `model-index.yml` is the main file tying together all the metadata. We recommend putting it in the root
of your repository. 

This file can contain the metadata, or link to other files containing the metadata. You can have
metadata either in markdown or yaml/json files. 

## Option 1: Markdown files

You can see the full example in [option1-markdown](option1-markdown) directory. 

To use `model-index` like this, create a markdown file with the model description / usage instructions and
add `model-index` metadata *inside a comment in the markdown file*. Putting in the comment means the file
will still be human readable in GitHub, but will also contain all the metadata needed by model-index. 

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
or split it up into multiple files as shown in [model-index.yml](https://github.com/paperswithcode/model-index/blob/main/examples/option2-yaml/model-index.yml) file.

In this example we've split out the metadata into separate files in [metadata](option2-yaml/metadata) and
linked it inside model definitions like this: `Metadata: metadata/alexnet.md`. We did the same with READMEs that
are linked like this: `README: docs/alexnet.md`.  

## Option 3: Mix-and-match

These two options are not exclusive. You can have some of your model metadata defined in markdown, and other
in YAML/JSON files. You can also import YAML/JSON files into markdown. 

You can mix-and-match as long as everything is imported into the root `model-index.yml`.

# Documentation

For more information please refer to the [official documentation](https://model-index.readthedocs.io/en/latest/). 