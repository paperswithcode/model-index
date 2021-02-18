import modelindex
from modelindex import Metadata
from modelindex.models.Collection import Collection
from modelindex.models.CollectionList import CollectionList
from modelindex.models.Model import Model
from modelindex.models.ModelList import ModelList
from modelindex.models.Result import Result
from modelindex.models.ResultList import ResultList


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

