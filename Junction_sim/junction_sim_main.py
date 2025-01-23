
# Imports:
from xml.dom import minidom
from Simple_road_sim.simple_sim_main import configuration_header_maker
from Junction_sim import intersection_sim_net_make
from Junction_sim import intersection_rou_make

class split_filenames:
    def __init__(self):
        self.net_file = "split_net.net.xml"
        self.rou_file = "split_rou.rou.xml"
        self.cfg_file = "split_cfg.sumocfg"

def input_header_make(net_file_name,rou_file_name,net_xml):
    input_xml = net_xml.createElement('input')
    net_file_xml = net_xml.createElement('net-file')
    net_file_xml.setAttribute('value', net_file_name)
    input_xml.appendChild(net_file_xml)
    rou_file_xml = net_xml.createElement('route-files')
    rou_file_xml.setAttribute('value',rou_file_name)
    input_xml.appendChild(rou_file_xml)
    return input_xml


def split_sim_maker():
    filenames = split_filenames()
    cfg_file = minidom.Document()
    cfg_header_xml = configuration_header_maker(cfg_file)
    cfg_file.appendChild(cfg_header_xml)
    intersection_sim_net_make.split_road_sim_net_make(filenames.net_file)
    intersection_rou_make.split_road_rou_make('E0','-E0','E1','-E1','500.00',filenames.rou_file)
    cfg_header_xml.appendChild(input_header_make(filenames.net_file,filenames.rou_file,cfg_file))
    split_cfg_xml = cfg_file.toprettyxml(indent="\t")
    with open(filenames.cfg_file, 'w') as xml_file:
        xml_file.write(split_cfg_xml)
    print("Simple simulation files generated")

