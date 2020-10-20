#!/bin/sh

###############################################################################
# (A) Use `maintainer` to update AUTHORS.md
###############################################################################

export MAINTAINER_TOKEN=${GH_TOKEN}
go get github.com/myii/maintainer
maintainer contributor
