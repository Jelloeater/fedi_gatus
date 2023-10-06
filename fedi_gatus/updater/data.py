import logging
import os

import peewee
import requests

from fedi_gatus.shared import db


class Worker:
    raw_data = None

    def get_raw_data(self):
        # TODO Add Fediseer data to DB
        fediseer_data = requests.get(url="https://fediseer.com/api/v1/whitelist",
                     params={"endorsements": 1, "limit": 999, "page": 1}, timeout=10).json()

        site='lemmy.world'
        single = requests.get(url=f"https://fediseer.com/api/v1/whitelist/{site}",
                                     params={"endorsements": 1, "limit": 999, "page": 1}, timeout=10).json()
        data = []

        rest_data = requests.get(url="https://api.fedidb.org/v1/servers/", params={"limit": 40}, timeout=3).json()
        for i in rest_data["data"]:
            data.append(i)
        while True:
            next_page = rest_data["links"]["next"]
            if next_page is None:
                break
            rest_data = requests.get(url=next_page, params={"limit": 40}, timeout=3).json()
            for i in rest_data["data"]:
                data.append(i)
            if os.getenv("TEST_MODE"):  # Only run twice in test mode
                if rest_data["links"]["prev"] is not None:
                    break

            try:
                logging.info("Downloading: " + rest_data["links"]["next"])
            except TypeError:
                pass
        self.raw_data = data

    def insert_data(self):
        d = db.DbAccess()
        for i in self.raw_data:
            try:
                d.insert_data(i)
            except peewee.IntegrityError as e:
                logging.error(e)

    def initialize_db(self):
        d = db.DbAccess()
        d.initialize()
