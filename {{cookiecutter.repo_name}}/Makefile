TARGET?=local
COMPONENT?={{cookiecutter.package_name}}
VERSION:={{cookiecutter.src_dir}}/${COMPONENT}/version.py

include make/common.mk

include make/install.mk
include make/test.mk
include make/help.mk
include make/clean.mk
include make/lint.mk
include make/ci.mk

.DEFAULT:help
