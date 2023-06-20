# nerc-obm

Utilities for managing hardware via OBMs.

- container directory contains build run and docker for building environment 
 to run all playbooks and scripts

- play/get-hwinfo.yaml should be run first, to collect details about current inventory as well as configuration of the servers.

- play/mk_host_vars.py should be run after get-hwinfo.yaml, and will generate host vars with specific details used in other playbooks

Following environment variables need to be set to run:

- NOBM_DIR directory where local copy of this repo is located
- NOBM_CFGDIR private local directory containing ansible inventory, variables and secrets (tbd: split out the secrets)
- NOBM_DATADIR directory where to write output to


