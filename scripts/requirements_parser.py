#!/usr/bin/env python3
"""Install requirements with ease.

This file is primarily for providing all users a way to install test
dependencies with ease. Instead of having to install tests_require on each
test.
"""
import configparser
import sys

cfg = configparser.ConfigParser()
cfg.read("setup.cfg")

options = cfg["options"]

switch = {
    "install": "install_requires",
    "test": "tests_require",
    "setup": "setup_requires",
}

dependencies = []

for arg in sys.argv[1:]:
    operation = switch[arg]
    requirements = options[operation].strip()
    dependencies.extend(requirements.split("\n"))

sys.stdout.write("\n".join(dependencies))
