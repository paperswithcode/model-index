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
    mi = modelindex.load("tests/test-mi/16_images/")

    assert len(mi.collections) == 1
    assert len(mi.models) == 2
    err = mi.check(silent=True)

    assert len(err) == 2
    assert "Image file nonexistant.png" in err[0]

    assert mi.collections[0].image == "images/image.png"

    mi = modelindex.load("tests/test-mi/16_images/mi2.yml")

    assert len(err) == 2
    assert "Image file nonexistant.png" in err[0]

    assert mi.models[0].image == "../images/image.png"
    assert mi.models[1].image == "http://somewhere.com/external"

