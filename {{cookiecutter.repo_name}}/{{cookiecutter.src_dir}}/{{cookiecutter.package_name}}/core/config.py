from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

from {{cookiecutter.package_name}}.version import __version__


class Config(BaseSettings):
    title: str = "{{cookiecutter.project_name}}"
    version: str = __version__
    log_level: str = "INFO"

    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
    )
