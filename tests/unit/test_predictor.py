from summarizer.common.predictor import Summarizer, load_models
import pytest


def test_tokenizer_loads_properly():
    """ GIVEN the load_models function
        WHEN its called
        THEN check that the return values are not None
    """
    model, tokenizer = load_models()
    assert model is not None
    assert tokenizer is not None


def test_summarizer_summarizes():
    """ GIVEN a predictor
        WHEN the 'predict' method is called
        THEN return value is a string and of length less than the original text.
    """

    text = "As they rounded a bend in the path that ran beside the river, Lara recognized the silhouette of a fig tree atop a nearby hill. The weather was hot and the days were long. The fig tree was in full leaf, but not yet bearing fruit.\nSoon Lara spotted other landmarks—an outcropping of limestone beside the path that had a silhouette like a man’s face, a marshy spot beside the river where the waterfowl were easily startled, a tall tree that looked like a man with his arms upraised. They were drawing near to the place where there was an island in the river."
    model = Summarizer(min_length=100, max_length=300)
    prediction = model.predict(text)

    assert type(prediction) == str
    assert len(prediction) <= len(text)


def test_summarizer_predict_doesnt_accepts_ints():
    """ GIVEN a predictor
        WHEN the 'predict' method is called with an integer
        THEN a TypeError is raised.
    """
    integer = 123
    model = Summarizer(min_length=100, max_length=300)
    with pytest.raises(TypeError) as e_info:
        prediction = model.predict(integer)
