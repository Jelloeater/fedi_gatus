import logging

import yaml

# example template
x = """
endpoints:
  - name: SITE NAME HERE
    url: https://example.com
    <<: *defaults
"""
obj = yaml.safe_load(x)
logging.debug(obj)


class Endpoint:
    name = str
    url = str
    interval = int
    conditions = [str]



yamlo = []
x = Endpoint()
x.name = "Lemmy World2"
x.url = "cool site"
x.interval = 20
x.conditions = ["[STATUS] == 404"]
yamlo.append(x.__dict__)
e = {"endpoints" : x.__dict__}
out = yaml.dump(e,default_flow_style=False)
print(out)
