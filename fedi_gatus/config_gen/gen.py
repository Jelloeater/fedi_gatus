import logging

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
    logging.info('Generate UI')

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
    logging.info('Config generated')
    return u + e


def generate_top_instances():
    logging.info('Get top instances')
    d = db.DbAccess().get_top_lemmy_instances()
    instances = []
    for i in d: #TODO not in order by user count
        url = "https://" + i.domain
        instances.append({"name": f"{i.domain}", "url": url})
    return instances
