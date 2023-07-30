"""
    This module provides models used as messages to be passed via messageq.

"""

from collections import Counter
from typing import Any, Dict, List, Tuple

from pydantic import BaseModel


class Post(BaseModel):
    """
    This module provides models used as messages to be passed via messageq.
    """
    content: str # Required
    publication: str # Required

class ProcessedPost(BaseModel ):
    """ProcessedPost is to store the results of the DataProcessor."""
    publications: str = None # Not required on creation
    entities: Counter = Counter()
    article_count: int = 0
    
    
    def transform_for_database(self, top_n=2000) -> List[Tuple[str, str, str, Dict]]:
    '''Returns a list of tuples containing one of two types of message.
    For messages used as Firestore documents storing the word and count:
        (publication, collection, doc_id, document_dict)

    For messages used to increment the publication's document count
        publication, None, None, {'count': 1}
        When consuming this type of message check the collection or doc_id for None values
    '''