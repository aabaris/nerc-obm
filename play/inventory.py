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

def make_hostvars(rac_json):

    if bool(rac_json['failed']):
        print("ERROR: failed racadm call")
        return 1

    system_info = rac_json['system_info']
    host_vars = {}
    host_vars['dell_svc_tag'] = system_info['System'][0]['ChassisServiceTag']
    host_vars['vdisks'] = []
    for vdisk in system_info['VirtualDisk']:
        host_vars['vdisks'].append( 
                                   { 'vdisk':
                                    { 'name': vdisk['Name'] }
                                     })
    host_vars['pdisks'] = []
    for pdisk in system_info['PhysicalDisk']:
        controller = pdisk['FQDD'].split(":")[2]
        host_vars['pdisks'].append( 
                                   { 'pdisk': 
                                    { 'name': pdisk['FQDD'], 
                                     'size': pdisk['Size'],
                                     'controller': controller } 
                                    }
                                   )
    return host_vars

#rac_file = "../data/racadm-hyp-4.json"
#with open(rac_file) as rac_f:
#    rac_data = json.load(rac_f)

#print(rac_data)
#print(json.dumps(rac_data, indent = 4, sort_keys=True))

#a = process_rac(rac_data)
#b = view_rac(rac_data)

data_path = "../../../data/"

for rac_file in os.listdir("../../../data"):
    if "racadm-hyp" in rac_file:
        with open(data_path+rac_file) as rac_f:
            rac_data = json.load(rac_f)

        host_vars = yaml.dump(make_hostvars(rac_data),Dumper=IndentDumper)
        host_name = rac_file.replace('racadm-','')
        host_vars_file = data_path+host_name
        print(host_vars_file)
        hvfh = open(host_vars_file,"w")
        hvfh.write(host_vars)
        hvfh.close()
