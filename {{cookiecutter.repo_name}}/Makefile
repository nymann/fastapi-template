TARGET?=local
COMPONENT?={{cookiecutter.package_name}}
VERSION:={{cookiecutter.src_dir}}/${COMPONENT}/version.py

include make/ci.mk
include make/clean.mk
include make/common.mk
include make/help.mk
include make/install.mk
include make/lint.mk
include make/run.mk
include make/test.mk

.DEFAULT:help
