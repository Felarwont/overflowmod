import logging
import sys

def setup_logger():
    logger = logging.getLogger("overflowmod")
    logger.setLevel(logging.DEBUG)
    # logger.propagate = False
    
    # if not logger.handlers:
    #     handler = logging.StreamHandler(sys.stdout)
    #     formatter = logging.Formatter("[%(levelname)s] %(message)s")
    #     handler.setFormatter(formatter)
    #     logger.addHandler(handler)
    
    # return logger