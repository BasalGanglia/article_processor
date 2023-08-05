"""
This module allows us to have a centralized logger that will be
used from multiple processed at the same time.
"""

from multiprocessing import get_logger
import logging


def logger(level=logging.INFO) -> logging.Logger:
    """
    This function returns a logger that can be used from multiple
    processes at the same time.
    """
    log = get_logger()
    log.setLevel(level)
    handler = logging.StreamHandler()
    handler.setFormatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    log.addHandler(handler)
    return log


# Expose app_logger to other modules
app_logger = logger()
