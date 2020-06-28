# -*- coding: utf-8 -*-
"""Builds boilerplate as a package

"""
import setuptools
from distutils import util

version = dict()
path = util.convert_path("src/fastapi_template/version.py")
with open(path) as file:
    exec(file.read(), version)

setuptools.setup(version=version["__version__"])
