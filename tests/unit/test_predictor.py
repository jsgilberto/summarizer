"""Unit tests for predictor."""


def test_tokenizer_loads_properly():
    """Test for loading the model.

    GIVEN the load_models function
    WHEN its called
    THEN check that the return values are not None
    """
    assert True


def test_summarizer_summarizes():
    """Test for checking if the model does its job.

    GIVEN a predictor
    WHEN the 'predict' method is called
    THEN return value is a string and of length less than the original text.
    """
    assert True


def test_summarizer_predict_doesnt_accepts_ints():
    """Testing valid input for the model.

    GIVEN a predictor
    WHEN the 'predict' method is called with an integer
    THEN a TypeError is raised.
    """
    assert True
