#---Written by Michael Popov and Yuval Marsh---
import math


#Imports
import simple_sim_net_make
import simple_sim_rou_make
import simple_sim_utils
from xml.dom import minidom
# Functions
def configuration_header_maker(cfg_xml):
    config_header_xml = cfg_xml.createElement('configuration')
    config_header_xml.setAttribute('xmlns:xsi',"http://www.w3.org/2001/XMLSchema-instance")
    config_header_xml.setAttribute('xsi:noNamespaceSchemaLocation',"http://sumo.dlr.de/xsd/sumoConfiguration.xsd")
    return config_header_xml

def input_header_maker(cfg_xml,file_names):
    input_header_xml = cfg_xml.createElement('input')
    net_file_xml = cfg_xml.createElement('net-file')
    net_file_xml.setAttribute('value',file_names.net_file_name)
    rou_file_xml = cfg_xml.createElement('route-files')
    rou_file_xml.setAttribute('value',file_names.routes_file_name)
    input_header_xml.appendChild(net_file_xml)
    input_header_xml.appendChild(rou_file_xml)
    return input_header_xml

def simple_sim_maker():
    file_names_and_args = simple_sim_utils.simple_sim_args()
    simple_sim_net_make.simple_sim_net_make(file_names_and_args)
    simple_sim_rou_make.simple_sim_rou_make(file_names_and_args)
    # Make CFG file
    simple_sim_cfg = file_names_and_args.cfg_file_name
    simple_sim_cfg_xml = minidom.Document()
    config_header_xml = configuration_header_maker(simple_sim_cfg_xml)
    config_header_xml.appendChild(input_header_maker(simple_sim_cfg_xml,file_names_and_args))
    simple_sim_cfg_xml.appendChild(config_header_xml)
    simple_cfg_to_xml = simple_sim_cfg_xml.toprettyxml(indent="\t")
    with open(file_names_and_args.cfg_file_name, 'w') as xml_file:
        xml_file.write(simple_cfg_to_xml)
    print("Simple simulation files generated")

