from importlib.resources import files as resource_files
from typing import Any

import yaml


def get_logging_resource(path: str) -> dict[str, Any]:
    with resource_files(f"{__package__}").joinpath(path).open() as file:
        return dict(yaml.safe_load(file))
