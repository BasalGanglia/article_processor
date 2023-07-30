"""
This module allows us to have a centralized logger that will be used from multiple processes at the same time.    
"""

from multiprocessing import get_logger
import logging

def(level=logging.INFO): -> logging.Logger
    """
    Returns a logger that can be used from multiple processes at the same time.
    """
    logger = get_logger()
    logger.setLevel(level)
    return logger


# Exposing app_logger to be used by other modules.