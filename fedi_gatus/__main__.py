import logging
import os

if os.getenv("LOG_LEVEL") is None:
    logging.basicConfig(level=logging.WARNING)
else:
    logging.basicConfig(level=int(os.getenv("LOG_LEVEL")))

from importlib import metadata
from importlib.metadata import PackageNotFoundError

import typer

app_name = "fedi_gatus"

try:
    version = metadata.version(app_name)
except PackageNotFoundError:
    logging.warning("Package not installed")
    version = "0"

app = typer.Typer(
    no_args_is_help=True,
    epilog=f"Version: {version} \n Project: https://github.com/Jelloeater/gatus_config",
)


@app.command()
def main():
    logging.warning("hello world")


if __name__ == "__main__":
    typer.run(main)

# TODO Add API endpoint for DB
