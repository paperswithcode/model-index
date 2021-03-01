# An example how to use model-index

This is an example of how to use `model-index` inside your repository. 

To try it out, put the [model-index.yml](model-index.yml) file in the root of your repository. 

The `model-index.yml` file has metadata defined in two ways: inside markdown and inside yaml/json files.  
You can choose whichever suits you better, or mix them. 

## Option 1: Markdown files

You can see the full example in [option1-markdown](option1-markdown) directory. 

To use `model-index` like this, create a markdown file with the model description / usage instructions and
add `model-index` metadata at the top, like shown in [option1-markdown/docs/model1.md](option1_markdown/docs/model1.md). 

Then import all the markdown files into the root [option1-markdown/model-index.yml file](option1-markdown/model-index.yml) like this:

```yaml
Import:
  - docs/*.md
```

## Option 2: YAML/JSON files

You can see the full example in [option2-yaml](option2-yaml) directory.

To use `model-index` like this, you can either simply add all of your model metadata into `model-index.yml`,
or split it up into multiple files as shown in [option2-yaml/model-index.yml](option2-yaml/model-index.yml) file. 

## Option 3: Mix-and-match

These two options are not exclusive. You can have some of your model metadata defined in markdown, and other
in YAML/JSON files. You can also import YAML/JSON files into markdown. 

You can mix-and-match as long as everything is imported into the root `model-index.yml`.

# Documentation

For more information please refer to the [official documentation](https://model-index.readthedocs.io/en/latest/). 