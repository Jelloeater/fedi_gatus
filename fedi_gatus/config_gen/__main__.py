import logging

import fedi_gatus.config_gen.gen


def main():
    logging.info("Config Gen Start")
    top = fedi_gatus.config_gen.gen.generate_full_config()
    # FIXME Log file to correct path for docker
    with open("gatus-config.yaml", "w") as f:
        f.write(str(top))


if __name__ == "__main__":
    main()
