TARGET?=docker
COMPONENT?=fastapi_template
TMP_DOCKER:=/tmp/.${COMPONENT}_install_docker.empty_target
TMP_HOOKS:=/tmp/.${COMPONENT}_hooks.empty_target
VERSION:=src/${COMPONENT}/core/version.py
SCRIPTS_DIR:=scripts

include make/common.mk

include make/install.mk
include make/test.mk
include make/run.mk
include make/help.mk
include make/clean.mk
include make/lint.mk
include make/format.mk
include make/ci.mk

.DEFAULT:help
