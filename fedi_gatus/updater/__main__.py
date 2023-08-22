import logging
import os


import fedi_gatus.updater.data as data

if os.getenv("LOG_LEVEL") is None:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=int(os.getenv("LOG_LEVEL")))


def main():
    w = data.Worker()
    w.initialize_db()
    w.get_raw_data()
    logging.info("Data Downloaded")
    logging.info("Updating database")
    w.insert_data()
    # TODO Add test to make sure data is present, and redo if not


if __name__ == "__main__":
    logging.info("Updater start")
    main()
    logging.info("Updater finished")
