from fastapi import FastAPI
from pogo_api.endpoint import Endpoint

from {{cookiecutter.package_name}}.core.config import Config
from {{cookiecutter.package_name}}.core.service_container import ServiceContainer


class Api:
    def __init__(self, config: Config, service_container: ServiceContainer) -> None:
        self.api = FastAPI(version=config.version, title=config.title, docs_url="/")
        self.services = service_container
        self.add_endpoints()

    @property
    def endpoints(self) -> list[Endpoint]:
        return []

    def add_endpoints(self) -> None:
        for endpoint in self.endpoints:
            endpoint.route.add_to_router(self.api)
