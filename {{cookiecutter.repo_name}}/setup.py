from distutils import util
from typing import Dict

import setuptools

version: Dict[str, str] = {}
path = util.convert_path("{{cookiecutter.src_dir}}/{{cookiecutter.package_name}}/version.py")
with open(path) as version_file:
    exec(version_file.read(), version)  # noqa: S102 DUO105, WPS421

setuptools.setup(version=version["__version__"])
