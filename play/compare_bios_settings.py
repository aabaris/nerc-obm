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
    bios_attributes = \
        profile_json['SystemConfiguration']['Components'][0]['Attributes']
    for item in bios_attributes:
        if item['Set On Import'] == "True" and item['Value'] != "":
          #print(item+" -> "+str(bios_attribute[item]))
          print(item['Name']+" -> "+item['Value'])
          #print(item)

    profile_struct = bios_attributes

    return profile_struct

def merge_profile_todb(host_name,host_profile, host_db):
    bios_attributes = \
        host_profile['SystemConfiguration']['Components'][0]['Attributes']
    for item in bios_attributes:

        item_name = item['Name']

        if item['Value'] != "":
            item_value = item['Value']
        else:
            item_value = "BLANK"

        if item_name  not in host_db:
            host_db[item_name] = {}
        if item_value not in host_db[item_name]:
            host_db[item_name][item_value] = []

        host_db[item_name][item_value].append(host_name)

    return 0

data_path = "../data/"
profile_db = {}

for rac_file in os.listdir(data_path):
    if "profile.json" in rac_file:
        host_name = rac_file.replace('-profile.json','')
        with open(data_path+rac_file) as rac_f:
            rac_data = json.load(rac_f)
        #host_struct = parse_profile(rac_data)
        merge_outcome = merge_profile_todb(host_name,rac_data,profile_db)
        #print("--")

for setting in profile_db:
    for value in profile_db[setting]:
        if len(profile_db[setting]) == 1:
            node_list = "ALL"
        else:
            node_list = str(profile_db[setting][value])
        print(setting+": "+value+" -> "+node_list)
