#!/usr/bin/env python

import json
import os

def debug_rac(rac_json):

    for key in rac_json['system_info']:
        print(key,"===") 
        print(rac_json['system_info'][key])

    return 0

def view_rac(rac_json):

    if bool(rac_json['failed']):
        print("ERROR: failed racadm call")
        return 1

    system_info = rac_json['system_info']
    print(system_info['System'][0]['ChassisServiceTag'])
    for pci_dev in system_info['PCIDevice']:
        print("  ",pci_dev['Description'])
    for disk in system_info['PhysicalDisk']:
        print("    ",disk['FQDD']," ",disk['Size'])

    return 0

#rac_file = "../data/racadm-hyp-4.json"
#with open(rac_file) as rac_f:
#    rac_data = json.load(rac_f)

#print(rac_data)
#print(json.dumps(rac_data, indent = 4, sort_keys=True))

#a = process_rac(rac_data)
#b = view_rac(rac_data)

for rac_file in os.listdir("../data"):
    if "racadm-hyp" in rac_file:
        with open("../data/"+rac_file) as rac_f:
            rac_data = json.load(rac_f)
        a = view_rac(rac_data)

