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
    # FIXME Log file to correct path for docker
    with open("gatus-config.yaml", "w") as f:
        f.write(str(top))


if __name__ == "__main__":
    main()
