"""
This module allows us to have a centralized logger that will be used from multiple processes at the same time.    
"""

from multiprocessing import get_logger
import logging


def logger(level=logging.INFO) -> logging.Logger:
    """
    Returns a logger that can be used from multiple processes at the same time.
    """
    """
    .. note:: AI Comments
    
    q: what is the purpose of this function?
    a: This function returns a logger that can be used from multiple processes at the same time.
    q: What is the purpose of StreamHander()?
    a: StreamHandler() returns a handler object that can be used to log messages to the console.
    """
    logger = get_logger()
    logger.setLevel(level)
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )
    return logger


app_logger = logger()
