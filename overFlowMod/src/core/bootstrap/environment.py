from pathlib import Path
import logging
import sys

MODS_PATH = Path(__file__).parents[4].resolve()

LIB_PATH = str(MODS_PATH / "lib")
SRC_PATH = str(MODS_PATH / "overFlowMod" / "src")

def setup_runtime():
    for path_str in (LIB_PATH, SRC_PATH):
        if path_str not in sys.path:
            sys.path.insert(0, path_str)

def setup_logger():
    logger = logging.getLogger("overflowmod")
    logger.setLevel(logging.DEBUG)