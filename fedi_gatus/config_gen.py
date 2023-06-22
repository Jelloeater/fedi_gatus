import logging

import yaml

# example
x = """
endpoints:
  - name: Lemmy World
    url: https://lemmy.world
    interval: 30s
    conditions:
      - "[STATUS] == 200"
"""
obj = yaml.safe_load(x)
logging.debug(obj)
