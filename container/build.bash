#!/bin/bash
#
set -e

#DBG="echo"

$DBG podman build -t ans-idrac -f $NOBM_DIR/container/Dockerfile
