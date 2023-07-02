import yaml

import fedi_gatus.data

# example template
x = """
endpoints:
  - name: SITE NAME HERE
    url: https://example.com
    <<: *defaults
"""


class Endpoint:
    name = str
    url = str
    interval = int
    conditions = [str]


def generate_endpoints(endpoint_list: [dict]):
    list_out = []
    for i in endpoint_list:
        o = Endpoint()
        o.name = i.get("name")
        o.url = i.get("url")
        o.interval = 20
        list_out.append(vars(o))
    e = {"endpoints": list_out}
    return yaml.dump(e, default_flow_style=False, sort_keys=False)


def generate_ui():
    import logging
    import os

    SCRIPT_CUR_DIR = os.path.dirname(os.path.abspath(__file__))
    logging.info(f"File_DIR={SCRIPT_CUR_DIR}")

    # Get Template
    from string import Template

    template = open(f"{SCRIPT_CUR_DIR}/ui.template.yaml", "r")
    result = Template(template.read()).safe_substitute({"email": os.getenv("EMAIL")})
    template.close()
    return result


def generate_full_config():
    u = generate_ui()
    e = generate_endpoints(fedi_gatus.data.generate_top_instances())
    return u + e
