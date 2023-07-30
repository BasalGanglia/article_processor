"""
This module allows us to have a centralized logger that will be used from multiple processes at the same time.


Here is copilot explanation:

Here is the explanation for the code below:
1. get_logger() returns a logger object with the name of the current module.
2. setLevel() sets the threshold for this logger to level.
3. StreamHandler() returns a handler object that can be used to log messages to the console.
4. setFormatter() sets the Formatter for this handler to fmt.
5. Because logging.Formatter doesn't have any arguments, we use the default arguments.


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
