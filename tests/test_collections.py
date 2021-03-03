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
import copy


def test_deepcopy():
    mi = modelindex.load("tests/test-mi/03_col")

    m1 = mi.models[0]
    m2 = copy.deepcopy(m1)

    m2.name = "New name"
    assert m1.name != m2.name
    assert m2.name == "New name"

    m2.results[0].task = "New task"
    assert m1.results[0].task != m2.results[0].task
    assert m2.results[0].task == "New task"

    m2.results.data.append(Result(task="", dataset="", metrics={}))
    assert len(m1.results) == 1
    assert len(m2.results) == 2

    m2.metadata.flops = 10
    assert m1.metadata.flops != m2.metadata.flops
    assert m2.metadata.flops == 10


def test_col_merge():
    mi = modelindex.load("tests/test-mi/17_collections_merge")

    m1 = mi.models[0].full_model
    m2 = mi.models[1].full_model

    assert m1.metadata.training_data == "ImageNet"
    assert m2.metadata.training_data == "Reddit"

    assert len(m1.metadata.training_techniques) == 4
    assert len(m2.metadata.training_techniques) == 5
    assert m2.metadata.training_techniques[-1] == "Transformers"

    assert m1.readme == "docs/inception-v3-readme.md"
    assert m2.readme == "docs/inception-v3-readme-120.md"

    mi = modelindex.load("tests/test-mi/17_collections_merge/mi2.yml")

    m1 = mi.models[0].full_model
    m2 = mi.models[1].full_model

    assert len(m1.results) == 2
    assert len(m2.results) == 2

    assert m1.results[0].metrics["Top 1 Accuracy"] == "11%"
    assert m2.results[0].metrics["Top 1 Accuracy"] == "11%"
    assert m1.results[1].metrics["Top 1 Accuracy"] == "74.67%"
    assert m2.results[1].metrics["Top 1 Accuracy"] == "75.1%"

    mi = modelindex.load("tests/test-mi/17_collections_merge/mi3.yml")

    err = mi.check(silent=True)

    assert len(err) == 2
    assert "Inception v3-1" in err[0]

    m1 = mi.models[0].full_model
    m2 = mi.models[1].full_model

    assert m1.metadata.training_data is None
    assert m2.metadata.training_data == "Reddit"