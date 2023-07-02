# TODO Pull data from https://api.fediverse.observer/

import requests


def generate_top_instances():
    rest_data = requests.get(url="https://api.fedidb.org/v1/servers/", params={"limit": 40}, timeout=3).json()
    next_page = rest_data["links"]["next"]

    instances = []
    i = {"name": "Lemmy World", "url": "https://lemmy.world"}  # TODO Remove demo data
    instances.append(i)

    return instances
