###############################################################################
"""
    This module provides models used as messages to be passed via messageq.

"""
###############################################################################
from collections import Counter
from typing import Any, Dict, List, Tuple

from pydantic import BaseModel


class Post(BaseModel):
    """
    Post is used to store content and publication from the front-end
    """

    content: str
    publication: str


class ProcessedPost(BaseModel):
    """ProcessedPost is used to store the results of the DataProcessor"""

    publication: str = None  # Not-required on creation
    entities: Counter = Counter()
    article_count: int = 0

    @property
    def pub_key(self):
        return self.publication.strip().lower()

    def _transform_for_database(self, top_n: int = 2000) -> List[str, str, str, Dict]:
        """Returns a list of tuples containing one of two types of message.

        For messages used as Firestore documents storing the word and count:
            (publication, collection, doc_id, document_dict)

        For messages used to increment the publication's document count
            publication, None, None, {'count': 1}
            When consuming this type of message check the collection or doc_id
            for None values
        """
        return list(self._transform_for_database(top_n))

    def __add__(self, other):
        self.article.count += 1
        self.publication = other.publication
        self.entities += other.entities
        return self
