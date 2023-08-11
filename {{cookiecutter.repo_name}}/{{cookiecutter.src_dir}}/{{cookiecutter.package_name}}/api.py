import logging

from fastapi import FastAPI
from pogo_api.endpoint import Endpoint

from {{cookiecutter.package_name}}.core.config import Config
from {{cookiecutter.package_name}}.core.service_container import ServiceContainer


class Api:
    def __init__(self, config: Config, service_container: ServiceContainer) -> None:
        logging.basicConfig(level=config.log_level, format="%(levelname)s:\t%(asctime)s\t%(message)s")  # noqa: WPS323
        self.api = FastAPI(version=config.version, title=config.title, docs_url="/")
        self._services = service_container
        self._add_endpoints_to_api()

    @property
    def _get_endpoints(self) -> list[Endpoint]:
        return []

    def _add_endpoints_to_api(self) -> None:
        for endpoint in self._get_endpoints:
            endpoint.route.add_to_router(self.api)
