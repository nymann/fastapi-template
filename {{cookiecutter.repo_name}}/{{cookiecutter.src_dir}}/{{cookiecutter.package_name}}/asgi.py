from {{cookiecutter.package_name}}.api import Api
from {{cookiecutter.package_name}}.core.config import Config
from {{cookiecutter.package_name}}.core.service_container import ServiceContainer

config = Config()
service_container = ServiceContainer(config=config)
api = Api(config=config, service_container=service_container).api

