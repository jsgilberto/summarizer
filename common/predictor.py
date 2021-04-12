""" This module holds the model class
"""
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelWithLMHead, AutoModelForSeq2SeqLM


def load_models(model_name='t5-small', model_dir='./models'):
    """ Load models from local directory (if they exist).
        If the models don't exist, they are loaded from the internet.

        Args:
            model_name (str, optional): The name of the model to be used.
            model_dir (str, optional): The name of the tokenizer to be used.
    """
    try:
        print(f"Loading models from local directory.")
        tokenizer = AutoTokenizer.from_pretrained(model_dir)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_dir)
    except Exception as e:
        print(f"Error: {e}")
        print(f"Failed loading models from local directory.")
        print(f"Downloading models from internet...")

        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        tokenizer.save_pretrained(model_dir)
        model.save_pretrained(model_dir)
    
    return model, tokenizer


class Summarizer:
    """ This class represents the model
    """
    def __init__(self, min_length=100, max_length=300):
        """ Initialize model instance

        Args:
            min_length (int, optional): The minimum length of the result. 
                Defaults to 100.
            max_length (int, optional): The maximum length of the result. 
                Defaults to 300.
        """
        model, tokenizer = load_models()
        self.summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)
        self.min_length = min_length
        self.max_length = max_length


    def predict(self, text):
        """ Invoke the model using the initialized parameters

        Args:
            text (str): the input text to summarize.

        Returns:
            str: the summary of the text.
        """
        if len(text) <= self.min_length:
            return text
        
        return self.summarizer(
            text, 
            min_length=self.min_length,
            max_length=self.max_length
        )[0]["summary_text"]