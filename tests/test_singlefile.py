import modelindex
from modelindex import Metadata
from modelindex.models.Collection import Collection
from modelindex.models.CollectionList import CollectionList
from modelindex.models.Model import Model
from modelindex.models.ModelList import ModelList
from modelindex.models.Result import Result
from modelindex.models.ResultList import ResultList


def test_singlefile():
    mi = modelindex.load("tests/test-mi/01_base")

    assert "Models" in mi.data
    assert isinstance(mi.models, ModelList)


def test_metadata():

    # empty should work
    Metadata()

    # it should allow for named arguments
    meta = Metadata(
        flops=1000,
        parameters="24M"
    )

    assert meta.data == {
        "FLOPs": 1000,
        "Parameters": "24M"
    }

    # should allow for custom
    meta = Metadata(
        flops=1000,
        my_argument=123
    )

    assert meta.data == {
        "FLOPs": 1000,
        "my_argument": 123
    }

    meta.data["my_argument"] = 11
    assert meta.data == {
        "FLOPs": 1000,
        "my_argument": 11
    }

    del meta.data["my_argument"]
    assert meta.data == {
        "FLOPs": 1000,
    }

    meta = Metadata.from_dict({
        "Epochs": 120,
        "my custom parameter": "abc"
    })
    assert meta.data == {
        "Epochs": 120,
        "my custom parameter": "abc"
    }


def test_metadata_from_dict():
    m = Metadata.from_dict(
        {'FLOPs': 11462568384,
         'Parameters': 23834568,
         'Epochs': 90,
         'Batch Size': 32,
         'Training Data': 'ImageNet',
         'Training Techniques': ['RMSProp',
                                 'Weight Decay',
                                 'Gradient Clipping',
                                 'Label Smoothing'],
         'Training Resources': '8x V100 GPUs',
         'Architecture': ['Auxiliary Classifier', 'Inception-v3 Module']}
    )

    assert m.data == {'FLOPs': 11462568384,
                      'Parameters': 23834568,
                      'Epochs': 90,
                      'Batch Size': 32,
                      'Training Data': 'ImageNet',
                      'Training Techniques': ['RMSProp',
                                              'Weight Decay',
                                              'Gradient Clipping',
                                              'Label Smoothing'],
                      'Training Resources': '8x V100 GPUs',
                      'Architecture': ['Auxiliary Classifier', 'Inception-v3 Module']}

    # mixed case and _ instead of space

    m = Metadata.from_dict(
        {'flops': 11462568384,
         'Parameters': 23834568,
         'epochs': 90,
         'batch_size': 32,
         'Training Data': 'ImageNet',
         'Training Techniques': ['RMSProp',
                                 'Weight Decay',
                                 'Gradient Clipping',
                                 'Label Smoothing'],
         'Training Resources': '8x V100 GPUs',
         'Architecture': ['Auxiliary Classifier', 'Inception-v3 Module']}
    )

    assert m.data == {'FLOPs': 11462568384,
                      'Parameters': 23834568,
                      'Epochs': 90,
                      'Batch Size': 32,
                      'Training Data': 'ImageNet',
                      'Training Techniques': ['RMSProp',
                                              'Weight Decay',
                                              'Gradient Clipping',
                                              'Label Smoothing'],
                      'Training Resources': '8x V100 GPUs',
                      'Architecture': ['Auxiliary Classifier', 'Inception-v3 Module']}


def test_result_list():
    ResultList()

    r = ResultList(
        [{
            "task": "Image Classification",
            "dataset": "ImageNet",
            "metrics": {
                "Top 1 Accuracy": "88%",
                "Top 5 Accuracy": "92%"
            }
        }]
    )

    assert len(r.data) == 1
    assert isinstance(r.data[0], Result)
    assert r.data[0].data == {
            "Task": "Image Classification",
            "Dataset": "ImageNet",
            "Metrics": {
                "Top 1 Accuracy": "88%",
                "Top 5 Accuracy": "92%"
            }
        }


def test_model():
    Model(name="abc")

    m = Model.from_dict(
        {'Name': 'Inception v3',
         'Metadata': {'FLOPs': 11462568384,
                      'Parameters': 23834568,
                      'Epochs': 90,
                      'Batch Size': 32,
                      'Training Data': 'ImageNet',
                      'Training Techniques': ['RMSProp',
                                              'Weight Decay',
                                              'Gradient Clipping',
                                              'Label Smoothing'],
                      'Training Resources': '8x V100 GPUs',
                      'Architecture': ['Auxiliary Classifier', 'Inception-v3 Module']},
         'Results': [{'Task': 'Image Classification',
                      'Dataset': 'ImageNet',
                      'Metrics': {'Top 1 Accuracy': '74.67%', 'Top 5 Accuracy': '92.1%'}}],
         'Paper': 'https://arxiv.org/abs/1512.00567v3',
         'Code': 'https://github.com/rwightman/pytorch-image-models/blob/timm/models/inception_v3.py#L442',
         'Weights': 'https://download.pytorch.org/models/inception_v3_google-1a9a5a14.pth',
         "Config": "config/myconfig.json",
         'README': 'docs/inception-v3-readme.md',
         'Other': 'something'}
    )

    assert m.name == 'Inception v3'
    assert m.paper == 'https://arxiv.org/abs/1512.00567v3'
    assert m.weights == "https://download.pytorch.org/models/inception_v3_google-1a9a5a14.pth"
    assert m.readme == "docs/inception-v3-readme.md"
    assert m.code == "https://github.com/rwightman/pytorch-image-models/blob/timm/models/inception_v3.py#L442"
    assert m.config == "config/myconfig.json"
    assert isinstance(m.metadata, Metadata)
    assert m.metadata.data == {'FLOPs': 11462568384,
                      'Parameters': 23834568,
                      'Epochs': 90,
                      'Batch Size': 32,
                      'Training Data': 'ImageNet',
                      'Training Techniques': ['RMSProp',
                                              'Weight Decay',
                                              'Gradient Clipping',
                                              'Label Smoothing'],
                      'Training Resources': '8x V100 GPUs',
                      'Architecture': ['Auxiliary Classifier', 'Inception-v3 Module']}

    assert m.data["Other"] == "something"

    assert isinstance(m.results, ResultList)
    assert m.readme == 'docs/inception-v3-readme.md'

    m.name = "New name"
    assert m.name == "New name"
    assert m.data["Name"] == "New name"

    m.results = {'Task': 'Image Classification',
                 'Dataset': 'ImageNet2',
                 'Metrics': {'Top 1 Accuracy': '74.67%', 'Top 5 Accuracy': '92.1%'}}

    assert isinstance(m.results[0], Result)
    assert m.results[0].dataset == "ImageNet2"

    # setters
    m.paper = "new paper"
    assert m.paper == "new paper"

    m.code = "new code"
    assert m.code == "new code"

    m.weights = "new w"
    assert m.weights == "new w"

    m.config = "new c"
    assert m.config == "new c"

    m.readme = "readme1"
    assert m.readme == "readme1"

    m.in_collection = "in col1"
    assert m.in_collection == "in col1"

    m.metadata = {'FLOPs': 122,
                  'Parameters': 111,
                  'Epochs': 90,
                  'Batch Size': 32,
                  'Training Data': 'ImageNet',
                  'Training Techniques': ['RMSProp',
                                          'Weight Decay',
                                          'Gradient Clipping',
                                          'Label Smoothing'],
                  'Training Resources': '8x V100 GPUs',
                  'Architecture': ['Auxiliary Classifier', 'Inception-v3 Module']}

    assert isinstance(m.metadata, Metadata)
    assert m.metadata.data["FLOPs"] == 122
    assert m.metadata.flops == 122
    m.metadata.flops = 9
    assert m.metadata.flops == 9


def test_model_list():
    ModelList()

    ml = ModelList(
        {'Name': 'Inception v1',
         'Metadata': {'FLOPs': 11462568384,
                      'Parameters': 23834568,
                      'Epochs': 90,
                      'Batch Size': 32,
                      'Training Data': 'ImageNet',
                      'Training Techniques': ['RMSProp',
                                              'Weight Decay',
                                              'Gradient Clipping',
                                              'Label Smoothing'],
                      'Training Resources': '8x V100 GPUs',
                      'Architecture': ['Auxiliary Classifier', 'Inception-v3 Module']},
         'Results': [{'Task': 'Image Classification',
                      'Dataset': 'ImageNet',
                      'Metrics': {'Top 1 Accuracy': '74.67%', 'Top 5 Accuracy': '92.1%'}}],
         'Paper': 'https://arxiv.org/abs/1512.00567v3',
         'Code': 'https://github.com/rwightman/pytorch-image-models/blob/timm/models/inception_v3.py#L442',
         'Weights': 'https://download.pytorch.org/models/inception_v3_google-1a9a5a14.pth',
         'README': 'docs/inception-v3-readme.md'}
    )

    assert len(ml.models) == 1
    assert isinstance(ml.models[0], Model)
    assert ml.models[0].name == "Inception v1"


def test_collections():
    Collection(name="abc")
    CollectionList()

    cl = CollectionList(
        [{'Name': 'Inception v3',
          'Metadata': {'Training Data': 'ImageNet',
                       'Training Techniques': ['RMSProp',
                                               'Weight Decay',
                                               'Gradient Clipping',
                                               'Label Smoothing'],
                       'Training Resources': '8x V100 GPUs',
                       'Architecture': ['Auxiliary Classifier', 'Inception-v3 Module']},
          'Paper': 'https://arxiv.org/abs/1512.00567v3',
          'Code': 'https://github.com/rwightman/pytorch-image-models/blob/timm/models/inception_v3.py#L442',
          'README': 'docs/inception-v3-readme.md'}]
    )

    assert len(cl.collections) == 1
    assert cl.collections[0].name == "Inception v3"


    m = Model.from_dict(
        {'Name': 'Inception v3 - 90 epochs',
         'In Collection': 'Inception v3',
         'Metadata': {'Epochs': 90},
         'Results': [{'Task': 'Image Classification',
                      'Dataset': 'ImageNet',
                      'Metrics': {'Top 1 Accuracy': '74.67%', 'Top 5 Accuracy': '92.1%'}}],
         'Weights': 'https://download.pytorch.org/models/inception_v3_google-1a9a5a14.pth'}
    )
    assert m.in_collection == 'Inception v3'


def test_collections_load():
    mi = modelindex.load("tests/test-mi/03_col")

    assert "Models" in mi.data
    assert isinstance(mi.models, ModelList)

    assert isinstance(mi.collections, CollectionList)


def test_common_dict_list_errors():
    mi = modelindex.load("tests/test-mi/14_common")

    assert mi.models[1].metadata.epochs == 130
    assert mi.models[0].results[0].task == "Image Classification"
    assert mi.models[0].results[0].metrics["Top 1 Accuracy"] == "11.67%"
