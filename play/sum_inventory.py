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
    hw_struct = {}
    if bool(rac_json['failed']):
        print("ERROR: failed racadm call")
        return 1

    system_info = rac_json['system_info']
    hw_struct['svc_tag'] = system_info['System'][0]['ChassisServiceTag']
    hw_struct['nics'] = []
    for pci_dev in system_info['PCIDevice']:
        dev_name = pci_dev['Description']
        if "Ethernet" in dev_name and "10G" in dev_name:
            hw_struct['nics'].append(dev_name)
    hw_struct['cpus'] = []
    for cpu in system_info['CPU']:
        hw_struct['cpus'].append(cpu['Model'])

    hw_struct['memory'] = system_info['System'][0]['SysMemTotalSize']

    #return str(svc_tag+"|"+mem_total+"|"+cpu_info+"|"+netif_name)
    return hw_struct

data_path = "../data/"
os.makedirs(data_path+"host_vars",exist_ok=True)

for rac_file in os.listdir(data_path):
    host_info = {}
    if "racadm-" in rac_file:
        with open(data_path+rac_file) as rac_f:
            rac_data = json.load(rac_f)

        #host_vars = yaml.dump(make_hostvars(rac_data),Dumper=IndentDumper)
        host_name = rac_file.replace('racadm-','')
        host_name = host_name.replace('.json','')
        #host_vars_file = data_path+"host_vars/"+host_name
        host_info[host_name] = view_rac(rac_data)
        print( yaml.dump(host_info) )
        
