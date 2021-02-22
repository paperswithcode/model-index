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
    mi = modelindex.load("tests/test-mi/06_import_meta/")

    s = str(mi.models[0].metadata)
    assert "Epochs=90" in s
    s = str(mi.models[1].metadata)
    assert "Epochs=120" in s
    assert "custom={'my custom parameter': 'abc'}" in s

    s = str(mi.models[0])
    assert s == """Model(
  Name=Inception v3 - 90 epochs,
  Metadata=Metadata(
    Epochs=90,
    _filepath=tests/test-mi/06_import_meta/meta/meta1.yaml
  ),
  Results=[
    Result(
      Task=Image Classification,
      Dataset=ImageNet,
      Metrics={'Top 1 Accuracy': '74.67%', 'Top 5 Accuracy': '92.1%'},
      _filepath=tests/test-mi/06_import_meta/r1.yaml
    ),
  ],
  Weights=https://download.pytorch.org/models/inception_v3_google-1a9a5a14.pth,
  In Collection=Inception v3,
  _filepath=tests/test-mi/06_import_meta/m1.yml
)"""

    s = str(mi.models[1])
    assert s == """Model(
  Name=Inception v3 - 120 epochs,
  Metadata=Metadata(
    Epochs=120,
    custom={'my custom parameter': 'abc'},
    _filepath=tests/test-mi/06_import_meta/meta/meta2.yaml
  ),
  Results=[
    Result(
      Task=Image Classification,
      Dataset=ImageNet,
      Metrics={'Top 1 Accuracy': '75.1%', 'Top 5 Accuracy': '93.1%'},
      _filepath=tests/test-mi/06_import_meta/r2.yaml
    ),
  ],
  Weights=https://download.pytorch.org/models/inception_v3_google-120-1a9a5afd.pth,
  In Collection=Inception v3,
  _filepath=tests/test-mi/06_import_meta/m2.yml
)"""