from {{cookiecutter.package_name}}.core.config import Config

class ServiceContainer:
    def __init__(self, config: Config) -> None:
        self.config = config
