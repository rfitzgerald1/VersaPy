import logging
from loguru import logger
import sys

def setup_logging():
    logger.remove()
    logger.add(sys.stdout, format="{time} - {level} - {message}", level="INFO")
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    return logger

setup_logging()
logger.info("Logging configured!")
