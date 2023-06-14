#!/bin/bash
#

set -e

#DBG="echo"

$DBG podman run -it \
	-v $NOBM_DIR/play:/opt/nobm/play:Z,ro \
	-v $NOBM_CFGDIR/inventory:/opt/nobm/inventory:Z,ro \
	-v $NOBM_DATADIR:/opt/nobm/data:Z,rw \
	--entrypoint=bash localhost/ans-idrac
