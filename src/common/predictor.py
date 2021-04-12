"""This module holds the model class."""
import os
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from typing import Text

ROOT_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)


def load_models(model_name: Text = 't5-small', model_dir: Text = 'models'):
    """Load models from local directory (if they exist).

    If the models don't exist, they are loaded from the internet.

    Args:
        model_name (str, optional): The name of the model to be used.
        model_dir (str, optional): The name of the tokenizer to be used.
    """
    model_dir = os.path.join(ROOT_DIR, model_dir)
    try:
        print(f"Loading models from local directory: {model_dir}")
        tokenizer = AutoTokenizer.from_pretrained(model_dir)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_dir)
    except Exception as e:
        print(f"Failed loading models from local directory: {model_dir}")
        print("Downloading models from internet...")

        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        tokenizer.save_pretrained(model_dir)
        model.save_pretrained(model_dir)

    return model, tokenizer


class Summarizer:
    """This class represents the model."""

    def __init__(self, min_length: int = 100, max_length: int = 300):
        """Initialize model instance.

        Args:
            min_length (int, optional): The minimum length of the result.
                Defaults to 100.
            max_length (int, optional): The maximum length of the result.
                Defaults to 300.
        """
        model, tokenizer = load_models()
        self.summarizer = pipeline(
            "summarization",
            model=model,
            tokenizer=tokenizer
        )
        self.min_length = min_length
        self.max_length = max_length

    def predict(self, text: Text):
        """Invoke the model using the initialized parameters.

        Args:
            text (str): the input text to summarize.

        Returns:
            str: the summary of the text.
        """
        if type(text) != str:
            raise TypeError("text input should be of type 'str'")

        if len(text) <= self.min_length:
            return text

        return self.summarizer(
            text,
            min_length=self.min_length,
            max_length=self.max_length
        )[0]["summary_text"]
