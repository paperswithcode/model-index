# model-index: maintain a source of truth for ML models

`model-index` has two goals:
- Make it easy to maintain a source-of-truth index of Machine Learning model metadata 
- Enable the community browse this model metadata on [Papers with Code](https://paperswithcode.com/)

The main design principle of `model-index` is **flexibility**. You can store your model metadata however is the
most convenient for you - as JSONs, YAMLs or as annotations inside markdown. `model-index` provides a convenient
way to collect all this metadata into a single file that's browsable, searchable and comparable.

You can use this library locally or choose to upload the metadata to [Papers with Code](https://paperswithcode.com)
to have your library featured on the website. 

## Quick start

Models are described with metadata and a README file. If you already have a README for your model,
you can include the metadata in the comment at the top:

`models/inception-v3.md`
```markdown
<!--
Type: model-index
Models:
  - Name: Inception v3
  - Metadata:
      Parameters: 23834568
      Epochs: 90
  - Results:
      Task: Image Classification
      Dataset: ImageNet
      Metrics:
        Top 1 Accuracy: 74.67%
        Top 5 Accuracy: 92.1%
-->
# Inception v3 Model

Inception v3 is a convolutional neural network architecture.
....
```

Then link your markdown file in the global model index file `model-index.yml` (in the root of your
repository):

`model-index.yml`
```yaml
Models:
  - models/inception-v3.md
```

Alternatively, you can put all the metadata into the `model-index.yml` file and provide a link to 
an unannotated markdown file. 

## Learn more

Check out our [official documentation](https://model-index.readthedocs.io/en/latest/) for more examples. 

## Uploading to Papers with Code

To feature your library on Papers with Code, get in touch with `hello@paperswithcode.com` and the model index
of your library will be automatically included into Papers with Code. 







