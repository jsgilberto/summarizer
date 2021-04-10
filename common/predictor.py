""" This module holds the model class
"""
from transformers import pipeline


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
        self.summarizer = pipeline("summarization")
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