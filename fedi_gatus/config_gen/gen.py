import logging

import requests
import yaml

from fedi_gatus.shared import db


class Endpoint:
    name = str
    url = str
    interval = int
    conditions = [str]


def Generate_endpoints(endpoint_list: [dict]):
    list_out = []
    for i in endpoint_list:
        o = Endpoint()
        o.name = i.get("name")
        o.url = i.get("url") + "/nodeinfo/2.0.json"
        o.interval = str(20) + "s"
        o.conditions = ["[STATUS] == 200"]
        list_out.append(vars(o))
    e = {"endpoints": list_out}
    return yaml.dump(e, default_flow_style=False, sort_keys=False)


def generate_ui():
    logging.info("Generate UI")

    import os

    SCRIPT_CUR_DIR = os.path.dirname(os.path.abspath(__file__))
    # Get Template
    from string import Template

    template = open(f"{SCRIPT_CUR_DIR}/base.template.yaml", "r")
    result = Template(template.read()).safe_substitute(
        {
            "email": os.getenv("GATUS_EMAIL"),
            "site_address": os.getenv("SITE_ADDRESS"),
            "dbuser": os.getenv("POSTGRES_USER"),
            "dbpass": os.getenv("POSTGRES_PASSWORD"),
            "dbport": str(5432),
            "dbhostname": os.getenv("POSTGRES_HOSTNAME_GATUS"),
            "dbdatabase": os.getenv("POSTGRES_DB"),
        }
    )
    template.close()
    return result


def generate_full_config():
    # TODO  Add alerting to PagerDuty
    u = generate_ui()
    e = Generate_endpoints(generate_top_instances())
    logging.info("Config generated")
    return u + e
    # FIXME Add Gatus API endpoint Ex https://lemmy-status.org/api/v1/endpoints/statuses


def generate_top_instances():
    logging.info("Get top instances")
    from pythonseer import Fediseer
    f = Fediseer()
    # fediseer_data = f.whitelist.get(guarantors=3, endorsements=4)['instances']
    # TODO Ask dbo about adding params to library
    # https://github.com/Fediseer/pythonseer/issues/7

    d = requests.get(url='https://fediseer.com/api/v1/whitelist', timeout=60,
                 params={'endorsements': 3, 'guarantors': 4, 'software_csv': 'lemmy', 'limit': 100, 'domains': True}).json()['domains']

    # d = db.DbAccess().get_top_instances() # FIXME Backend is only returning a very small set of data... funnnnnn
    instances = []
    for i in d:  # TODO not in order by user count
        url = "https://" + i
        instances.append({"name": f"{i}", "url": url})
    return instances
