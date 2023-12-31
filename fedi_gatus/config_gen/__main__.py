import logging
import os

import fedi_gatus.config_gen.gen

if os.getenv("LOG_LEVEL") is None:
    logging.basicConfig(level=logging.WARNING)
else:
    logging.basicConfig(level=int(os.getenv("LOG_LEVEL")))


def main():
    logging.info("Config Gen Start")
    SCRIPT_CUR_DIR = os.path.dirname(os.path.abspath(__file__))
    logging.info(f"File_DIR={SCRIPT_CUR_DIR}")
    top = fedi_gatus.config_gen.gen.generate_full_config()

    path = f"{SCRIPT_CUR_DIR}/config"
    print(path)
    if not os.path.exists(path):
        os.makedirs(path)
    with open(f"{path}/config.yaml", "w") as f:
        f.write(str(top))


if __name__ == "__main__":
    logging.info("Config gen start")
    main()
    logging.info("Config gen finished")

# TODO Add Pagerduty integration https://github.com/TwiN/gatus/blob/master/docs/pagerduty-integration-guide.md
