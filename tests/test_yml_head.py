import modelindex
import pytest
from modelindex import Metadata
from modelindex.models.Collection import Collection
from modelindex.models.CollectionList import CollectionList
from modelindex.models.Model import Model
from modelindex.models.ModelList import ModelList
from modelindex.models.Result import Result
from modelindex.models.ResultList import ResultList
from modelindex.models.ModelIndex import ModelIndex


def test_yml_head():
    mi = modelindex.load("tests/test-mi/19_yml_head/readme.md")

    assert len(mi.models) == 1
    assert mi.models[0].name == "my model name"
    assert len(mi.models[0].results) == 1
    assert mi.models[0].results[0].task == "Speech Recognition"
    assert mi.models[0].results[0].dataset == "Common Voice en"
    assert mi.models[0].results[0].metrics == {
        "Test WER": 10
    }

    mi = modelindex.load("tests/test-mi/19_yml_head/readme-noname.md")

    assert len(mi.models) == 1
    assert mi.models[0].name is None
    assert len(mi.models[0].results) == 1
    assert mi.models[0].results[0].task == "Speech Recognition"
    assert mi.models[0].results[0].dataset == "Common Voice en"
    assert mi.models[0].results[0].metrics == {
        "Test WER": 20
    }