"""
this module enables us to process text using natural language processing
to extract known entities - i.e. nouns

It uses Spacy to extract entities based on a pre-built model.
The model must be downloaded before using spacy
"""

from collections import Counter
from typing import Dict

import spacy

from .debugging import app_logger as log
from .models import Post, ProcessedPost

class DataProcessor:
    def __init__(self, model_name: str = "en_core_web_sm"):
        log.info(f"Loading model {model_name}")
        self.nlp = spacy.load(model_name)
        log.info("Model loaded")
        self.skip = [
            "CARDINAL",
            "DATE",
            "ORDINAL",
            "QUANTITY",
            "TIME",
            "MONEY",
            "PERCENT",
        ]

    def entities(self, doc) -> Counter:
        t = [e.text.lower() for e in doc.ents if e.label_ not in self.skip]
        return Counter(t)
    
    def process(self, text: str) -> Dict[str, int]:
        doc = self.nlp(text)
        return self.entities(doc)
    
    def process_message(self, post) -> ProcessedPost
