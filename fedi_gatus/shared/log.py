import logging
import os


def main():
    if os.getenv("LOG_LEVEL") is None:
        logging.basicConfig(level=logging.WARNING)
    else:
        logging.basicConfig(level=int(os.getenv("LOG_LEVEL")))
