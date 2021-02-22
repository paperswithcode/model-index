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


def test_results_check():
    mi = modelindex.load("tests/test-mi/09_check/mi1.yml")

    e = mi.models[0].results[0].check_errors
    assert len(e) == 1
    assert "dataset" in e[0].lower()

    msgs = mi.check(silent=True)
    assert len(msgs) == 1
    assert "Results[0]" in msgs[0]

    mi = modelindex.load("tests/test-mi/09_check/mi2.yml")

    e = mi.models[0].results[0].check_errors
    assert len(e) == 0

    mi = modelindex.load("tests/test-mi/09_check/mi3.yml")

    e = mi.models[0].results[0].check_errors
    assert len(e) == 2
    assert "dataset" in e[0].lower()
    assert "metrics" in e[1].lower()

    mi = modelindex.load("tests/test-mi/09_check/mi4.yml")

    e = mi.models[0].results[0].check_errors
    assert len(e) == 3
    assert "dataset" in e[0].lower()
    assert "task" in e[1].lower()
    assert "metrics" in e[2].lower()

    assert len(mi.models[0].metadata.check_errors) == 0
    assert len(mi.models[0].check_errors) == 0

    mi = modelindex.load("tests/test-mi/09_check/mi5.yml")
    assert len(mi.models[0].check_errors) == 1
    assert "what" in mi.models[0].check_errors[0]
    assert "not exist" in mi.models[0].check_errors[0]

    msgs = mi.check(silent=True)
    assert len(msgs) == 4

    mi = modelindex.load("tests/test-mi/09_check/mi6.yml")
    assert len(mi.models[0].check_errors) == 2
    assert "what" in mi.models[0].check_errors[0]
    assert "not exist" in mi.models[0].check_errors[0]
    assert "README" in mi.models[0].check_errors[1]

    assert len(mi.models[0].results.check_errors) == 1
    assert "django" in mi.models[0].results.check_errors[0]
    assert "not exist" in mi.models[0].results.check_errors[0]

    mi = modelindex.load("tests/test-mi/09_check/mi7.yml")
    assert len(mi.check_errors) == 1
    assert "not exist" in mi.check_errors[0]

    mi = modelindex.load("tests/test-mi/10_import_meta_check")

    assert mi.models[0].filepath.endswith("meta/m1.yml")
    msgs = mi.check(silent=True)

    assert "noexist.json" in msgs[0]
    assert "wrongsubdir" in msgs[1]

    mi = modelindex.load("tests/test-mi/09_check/mi8.yml")
    assert len(mi.models[0].check_errors) == 1
    assert "what" in mi.models[0].check_errors[0]
    assert "not exist" in mi.models[0].check_errors[0]


def test_any_file():
    m1 = modelindex.load("tests/test-mi/07_import_models/model1.yaml")

    assert isinstance(m1, Model)
    assert m1.metadata.epochs == 90
    assert len(m1.results) == 1

    m2 = modelindex.load("tests/test-mi/07_import_models/model2.yaml")

    assert isinstance(m2, Model)
    assert m2.metadata.epochs == 120
    assert len(m2.results) == 1

    mi = modelindex.load("tests/test-mi/11_markdown/subdir/rexnet3.md")

    assert isinstance(mi, ModelIndex)
    assert mi.models[0].name == "RexNet3"

    rl = modelindex.load("tests/test-mi/09_check/results_list.yaml")

    assert isinstance(rl, ResultList)
    assert len(rl) == 3
    assert rl[1].metrics["Top 1 Accuracy"] == "70.67%"
    assert len(rl[2].check_errors) == 1
    assert "Metrics" in rl[2].check_errors[0]

    with pytest.raises(ValueError):
        modelindex.load("tests/test-mi/09_check/invalid_file.yml")