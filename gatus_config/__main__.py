import logging
from importlib import metadata
from importlib.metadata import PackageNotFoundError

import typer

app_name = "gatus_config"

try:
    version = metadata.version(app_name)
except PackageNotFoundError:
    logging.warning("Package not installed")
    version = "0"


app = typer.Typer(
    no_args_is_help=True,
    epilog=f"Version: {version} \n Project: https://github.com/Jelloeater/gatus_config",
)


def run():
    logging.debug("hello world")


if __name__ == "__main__":
    app()
