import logging
import os

import fedi_gatus.config_gen.gen

if os.getenv("LOG_LEVEL") is None:
    logging.basicConfig(level=logging.WARNING)
else:
    logging.basicConfig(level=int(os.getenv("LOG_LEVEL")))


def main():
    logging.info("Update Database info")


if __name__ == "__main__":
    main()
