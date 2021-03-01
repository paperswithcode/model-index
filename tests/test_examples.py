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


def test_examples():
    mi = modelindex.load("examples/option1-markdown")

    assert len(mi.collections) == 2
    assert len(mi.models) == 3

    assert mi.collections[0].name == "AlexNet"
    assert mi.collections[1].name == "ResNet"

    assert mi.models[0].code == "https://github.com/pytorch/vision/blob/5a315453da5089d66de94604ea49334a66552524/torchvision/models/alexnet.py#L53"
    assert mi.models[1].code == "https://github.com/pytorch/vision/blob/5a315453da5089d66de94604ea49334a66552524/torchvision/models/resnet.py#L304"
    assert mi.models[2].code == "https://github.com/pytorch/vision/blob/5a315453da5089d66de94604ea49334a66552524/torchvision/models/resnet.py#L316"

    mi = modelindex.load("examples/option2-yaml")

    assert len(mi.collections) == 2
    assert len(mi.models) == 3

    assert mi.collections[0].name == "AlexNet"
    assert mi.collections[1].name == "ResNet"

    assert mi.models[0].metadata.flops == 1429383808
    assert mi.models[1].metadata.flops == 15667943424
    assert mi.models[2].metadata.flops == 23117674496
