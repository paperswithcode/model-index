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

