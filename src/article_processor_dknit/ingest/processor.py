"""
This module enables us to process text using natural language processing
to extract known entities

It uses Spacy to extract entities based ona pre-built model.
The model must be downlaoded before using spacy.
"""

import spacy
from collections import Counter
from typing import Dict

from .debugging import app_logger as log


class DataProcessor:
    def __init__(self):
        log.info("Loading Spacy model")
        self.nlp = spacy.load("en_core_web_sm")
        log.info("Spacy model loaded")
        self.skip = [
            "CARDINAL",
            "DATE",
            "TIME",
            "ORDINAL",
            "PERCENT",
            "MONEY",
            "QUANTITY",
        ]

        def entities(self, doc) -> Counter:
            t = [e.text for e in doc.ents if e.label_ not in self.skip]
            return Counter(t)

        def process(self, text: str) -> Dict[str, int]:
            doc = self.nlp(text)
            return self.entities(doc)

        def process_message(self, post) -> ProcessedPost:
            pass
