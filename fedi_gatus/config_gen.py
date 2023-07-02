import logging

import yaml

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
        o.name = i.get('name')
        o.url = i.get('url')
        o.interval = 20
        list_out.append(vars(o))
    e = {"endpoints": list_out}
    return yaml.dump(e, default_flow_style=False, sort_keys=False)
