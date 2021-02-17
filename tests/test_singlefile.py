import modelindex
from modelindex import Metadata


def test_singlefile():
    mi = modelindex.load("tests/test-mi/01_base")

    assert "Models" in mi.data


def test_metadata():

    # empty should work
    Metadata()

    # it should allow for named arguments
    meta = Metadata(
        flops=1000,
        parameters="24M"
    )

    assert meta.data == {
        "FLOPs": 1000,
        "Parameters": "24M"
    }

    # should allow for custom
    meta = Metadata(
        flops=1000,
        my_argument=123
    )

    assert meta.data == {
        "FLOPs": 1000,
        "my_argument": 123
    }

    meta.data["my_argument"] = 11
    assert meta.data == {
        "FLOPs": 1000,
        "my_argument": 11
    }

    del meta.data["my_argument"]
    assert meta.data == {
        "FLOPs": 1000,
    }



