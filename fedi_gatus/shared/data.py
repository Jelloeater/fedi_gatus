# TODO Pull data from https://api.fediverse.observer/

import requests


def get_raw_data():
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
    return data
