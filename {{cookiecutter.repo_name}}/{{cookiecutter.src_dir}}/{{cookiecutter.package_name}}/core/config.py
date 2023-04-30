from pydantic import BaseSettings

from {{cookiecutter.package_name}}.version import __version__


class Config(BaseSettings):
    title: str == "{{cookiecutter.project_name}}"
    version: str = __version__

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
