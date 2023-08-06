# TODO Pull data from https://api.fediverse.observer/
import logging
import os

import requests

from fedi_gatus.shared import db


class Worker:
    raw_data = None

    def get_raw_data(self):
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
        self.raw_data = data

    def insert_data_(self):
        d = db.DataAccess()
        for i in self.raw_data:
            d.insert_data(i)
