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


def test_library():
    mi = modelindex.load("tests/test-mi/18_library")

    assert mi.library is not None

    assert mi.library.name == "AllenNLP"
    assert mi.library.repository == "https://github.com/allenai/allennlp-models"
    assert mi.library.headline == "An Apache 2.0 NLP research library, built on PyTorch, for developing state-of-the-art deep learning models on a wide variety of linguistic tasks."
    assert mi.library.website == 'https://allennlp.org/'
    assert mi.library.docs == 'https://docs.allennlp.org/'
    assert mi.library.image == "images/allennlp.png"
    assert "**AllenNLP** is a Natural Language Processing library " in mi.library.readme_content()

    mi = modelindex.load("tests/test-mi/18_library/mi2.yml")

    assert mi.library is not None

    assert mi.library.name == "AllenNLP"
    assert mi.library.repository == "https://github.com/allenai/allennlp-models"
    assert mi.library.headline == "An Apache 2.0 NLP research library, built on PyTorch, for developing state-of-the-art deep learning models on a wide variety of linguistic tasks."
    assert mi.library.website == 'https://allennlp.org/'
    assert mi.library.docs == 'https://docs.allennlp.org/'
    assert mi.library.image == "images/allennlp.png"
    assert "**AllenNLP** is a great Natural Language Processing library " in mi.library.readme_content()

    mi = modelindex.load("tests/test-mi/18_library/mi3.yml")

    assert mi.library is not None

    assert mi.library.name == "AllenNLP"
    assert mi.library.repository == "https://github.com/allenai/allennlp-models"
    assert mi.library.headline == "An Apache 2.0 NLP research library, built on PyTorch, for developing state-of-the-art deep learning models on a wide variety of linguistic tasks."
    assert mi.library.website == 'https://allennlp.org/'
    assert mi.library.docs == 'https://docs.allennlp.org/'
    assert mi.library.image == "images/allennlp.png"
    assert "**AllenNLP** is a great Natural Language Processing library " in mi.library.readme_content()

    mi = modelindex.load("tests/test-mi/18_library/mi4.yml")

    assert mi.library is not None

    assert mi.library.name == "AllenNLP"
    assert mi.library.repository == "https://github.com/allenai/allennlp-models"
    assert mi.library.headline == "An Apache 2.0 NLP research library, built on PyTorch, for developing state-of-the-art deep learning models on a wide variety of linguistic tasks."
    assert mi.library.website == 'https://allennlp.org/'
    assert mi.library.docs == 'https://docs.allennlp.org/'
    assert mi.library.image == "images/allennlp.png"
    assert "**AllenNLP** is a great Natural Language Processing library " in mi.library.readme_content()


