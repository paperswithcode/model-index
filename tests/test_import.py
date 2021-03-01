import modelindex
from modelindex import Metadata
from modelindex.models.Collection import Collection
from modelindex.models.CollectionList import CollectionList
from modelindex.models.Model import Model
from modelindex.models.ModelList import ModelList
from modelindex.models.Result import Result
from modelindex.models.ResultList import ResultList
from modelindex.utils import expand_wildcard_path


def test_imports():
    mi = modelindex.load("tests/test-mi/04_imports")

    assert "Models" in mi.data
    assert isinstance(mi.models, ModelList)
    assert len(mi.models) == 2


def test_result_imports():
    mi = modelindex.load("tests/test-mi/05_field_imports")

    assert "Models" in mi.data
    assert isinstance(mi.models, ModelList)
    assert len(mi.models) == 2

    assert mi.models[0].results[0].data == {
        'Task': 'Image Classification',
        'Dataset': 'ImageNet',
        'Metrics': {'Top 1 Accuracy': '74.67%', 'Top 5 Accuracy': '92.1%'}}

    assert mi.models[1].results[0].data == {
        'Task': 'Image Classification',
        'Dataset': 'ImageNet',
        'Metrics': {'Top 1 Accuracy': '75.1%', 'Top 5 Accuracy': '93.1%'}}


def test_metadata_imports():
    mi = modelindex.load("tests/test-mi/06_import_meta")

    assert "Models" in mi.data
    assert isinstance(mi.models, ModelList)
    assert len(mi.models) == 2

    assert mi.models[0].metadata.data == {
        "Epochs": 90
    }

    assert mi.models[1].metadata.data == {
        "Epochs": 120,
        "my custom parameter": "abc"
    }


def test_models_imports():
    mi = modelindex.load("tests/test-mi/07_import_models")

    assert "Models" in mi.data
    assert isinstance(mi.models, ModelList)
    assert len(mi.models) == 2
    assert len(mi.collections) == 1

    assert mi.models[0].metadata.data == {
        "Epochs": 90
    }

    assert mi.models[1].metadata.data == {
        "Epochs": 120,
    }


def test_models_imports_json():
    mi = modelindex.load("tests/test-mi/08_import_models_json")

    assert "Models" in mi.data
    assert isinstance(mi.models, ModelList)
    assert len(mi.models) == 2

    assert mi.models[0].metadata.data == {
        "Epochs": 90
    }

    assert mi.models[1].metadata.data == {
        "Epochs": 111,
    }


def test_expand_wildcard_path():
    supported = expand_wildcard_path("tests/test-mi/12_wildcard_imports/*.yml")
    assert supported == ["tests/test-mi/12_wildcard_imports/model-index.yml"]

    supported = expand_wildcard_path("tests/test-mi/12_wildcard_imports/model-index.yml")
    assert supported == ["tests/test-mi/12_wildcard_imports/model-index.yml"]

    supported = expand_wildcard_path("tests/test-mi/12_wildcard_imports/abbccabbbcc")
    assert supported == ["tests/test-mi/12_wildcard_imports/abbccabbbcc"]

    supported = expand_wildcard_path("tests/test-mi/12_wildcard_imports")
    assert supported == ["tests/test-mi/12_wildcard_imports"]

    supported = expand_wildcard_path("tests/test-mi/12_wildcard_imports/models/*.yml")
    assert supported == ["tests/test-mi/12_wildcard_imports/models/m1.yml",
                         "tests/test-mi/12_wildcard_imports/models/m2.yml"]


def test_wildcard_import():
    mi = modelindex.load("tests/test-mi/12_wildcard_imports")

    assert len(mi.models) == 2


def test_wildcard_model_import():
    mi = modelindex.load("tests/test-mi/13_wildcard_model_imports")
    assert len(mi.models) == 2
    assert len(mi.collections) == 1

    mi = modelindex.load("tests/test-mi/13_wildcard_model_imports/mi2.yml")
    assert len(mi.models) == 2
    assert len(mi.collections) == 0

    mi = modelindex.load("tests/test-mi/13_wildcard_model_imports/mi3.yml")
    assert len(mi.models) == 2
    assert len(mi.collections) == 1

    mi = modelindex.load("tests/test-mi/13_wildcard_model_imports/mi4.yml")
    assert len(mi.models) == 2
    assert len(mi.collections) == 1

    mi = modelindex.load("tests/test-mi/13_wildcard_model_imports/mi5.yml")
    assert len(mi.models) == 0
    assert len(mi.collections) == 2

    mi = modelindex.load("tests/test-mi/13_wildcard_model_imports/mi6.yml")
    assert len(mi.models) == 2
    assert len(mi.collections) == 1

    mi = modelindex.load("tests/test-mi/13_wildcard_model_imports/mi7.yml")
    assert len(mi.models) == 2
    assert len(mi.collections) == 1
    assert mi.models[0].name == "Inception v3 - 90 epochs"
    assert len(mi.models[0].results) == 2
    assert mi.models[0].results[0].metrics["Top 1 Accuracy"] == "11%"
    assert mi.models[0].results[1].metrics["Top 1 Accuracy"] == "21%"


def test_models_import_wildcard():
    mi = modelindex.load("tests/test-mi/13_wildcard_model_imports/mi8.yml")

    assert len(mi.collections) == 1
    assert len(mi.models) == 2

    assert mi.models[0].readme == "models_md/m1.md"
    assert mi.models[1].readme == "models_md/m2.md"

    mi = modelindex.load("tests/test-mi/13_wildcard_model_imports/mi9.yml")

    assert len(mi.collections) == 1
    assert len(mi.models) == 2

    assert mi.models[0].readme == "models_md/m1.md"
    assert mi.models[1].readme == "models_md/m2.md"
