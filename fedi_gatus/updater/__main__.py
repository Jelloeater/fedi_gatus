import logging
import os
from fedi_gatus.shared import db

if os.getenv("LOG_LEVEL") is None:
    logging.basicConfig(level=logging.WARNING)
else:
    logging.basicConfig(level=int(os.getenv("LOG_LEVEL")))


def main():
    logging.info("Update Database info")
    d = db.DataAccess()
    d.drop_table()  # Clear table
    d.create_table()
    r = d.get_top_lemmy_instances()
    instances = []
    for i in r:
        instances.append({"name": f"{i.domain} - {i.description}", "url": i.domain})
    return instances


if __name__ == "__main__":
    main()
