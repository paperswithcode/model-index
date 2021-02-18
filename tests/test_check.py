import modelindex
from modelindex import Metadata
from modelindex.models.Collection import Collection
from modelindex.models.CollectionList import CollectionList
from modelindex.models.Model import Model
from modelindex.models.ModelList import ModelList
from modelindex.models.Result import Result
from modelindex.models.ResultList import ResultList


def test_results_check():
    mi = modelindex.load("tests/test-mi/09_check/mi1.yml")

    e = mi.models[0].results[0].check_errors
    assert len(e) == 1
    assert "dataset" in e[0].lower()

    mi = modelindex.load("tests/test-mi/09_check/mi2.yml")

    e = mi.models[0].results[0].check_errors
    assert len(e) == 0

    mi = modelindex.load("tests/test-mi/09_check/mi3.yml")

    e = mi.models[0].results[0].check_errors
    assert len(e) == 2
    assert "dataset" in e[0].lower()
    assert "metrics" in e[1].lower()