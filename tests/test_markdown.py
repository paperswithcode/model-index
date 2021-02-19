import modelindex


def test_model_markdown():
    mi = modelindex.load("tests/test-mi/11_markdown")

    assert len(mi.models) == 6
    assert mi.models[0].name == "RexNet"
    assert mi.models[0].metadata.data["some field"] == 10

    assert mi.models[1].name == "RexNet1"
    assert mi.models[1].metadata.data["some field"] == 11
    assert mi.models[2].name == "RexNet2"
    assert mi.models[2].metadata.data["some field"] == 22
    assert mi.models[3].name == "RexNet3"
    assert mi.models[3].results[0].metrics == {"mAP": "19%"}
    assert mi.models[4].name == "Inception v3 - 90 epochs"
    assert mi.models[5].name == "Inception v3 - 120 epochs"
