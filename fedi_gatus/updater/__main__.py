import logging
import os


import fedi_gatus.updater.data as data

if os.getenv("LOG_LEVEL") is None:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=int(os.getenv("LOG_LEVEL")))


def main():
    logging.info("Update Database info")
    w = data.Worker()
    w.get_raw_data()
    w.insert_data()
    # TODO Add test to make sure data is present, and redo if not


if __name__ == "__main__":
    main()
