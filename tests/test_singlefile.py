import modelindex


def test_singlefile():
    mi = modelindex.load("tests/test-mi/01_base")

    assert "Models" in mi.data
    assert mi.models is not None
