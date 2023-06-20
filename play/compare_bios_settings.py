#!/usr/bin/env python

import json
import yaml
import os

class IndentDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(IndentDumper, self).increase_indent(flow, False)


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

def parse_profile(profile_json):

    profile_struct = {}
    #print(profile_json)
    bios_attribute = \
        profile_json['SystemConfiguration']['Components'][0]['Attributes']
    for item in bios_attribute:
        #print(item+" -> "+str(bios_attribute[item]))
        print(item['Name']+" -> "+item['Value'])
        #print(item)

    return profile_struct

data_path = "../data/"
profile_db = {}

for rac_file in os.listdir(data_path):
    if "profile.json" in rac_file:
        host_name = rac_file.replace('-profile.json','')
        with open(data_path+rac_file) as rac_f:
            rac_data = json.load(rac_f)
        host_struct = parse_profile(rac_data)
        print("--")

