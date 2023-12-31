# nerc-obm

Utilities for managing hardware via OBMs.

- container directory contains build run and docker for building environment 
 to run all playbooks and scripts

- inventory and vars are kept outside of this repo. 
  * inventory file should contain a list of targeted hosts and 'obm_ip' 
    variable set to their idrac interfaces ip address
  * gorup_vars should point to secrets containing obm_user and obm_password
  * host_vars should be generated dynamically using mk_host_vars.py script and
    copied from into inventory directory for use by other playbooks and scripts

- play/get-hwinfo.yaml should be run first, to collect details about current inventory as well as configuration of the servers.

- play/mk_host_vars.py should be run after get-hwinfo.yaml, and will generate 
  host vars with specific details used in other playbooks

Following environment variables need to be set to run:

- NOBM_DIR directory where local copy of this repo is located
- NOBM_CFGDIR private local directory containing ansible inventory, variables 
  and secrets (tbd: split out the secrets)
- NOBM_DATADIR directory where to write output to


