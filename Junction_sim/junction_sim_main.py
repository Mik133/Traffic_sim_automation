
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

class split_road_params:
    def __init__(self):
        self.split_edges = {'E0_pos':'E0',
                            'E0_neg':'-E0',
                            'E1_pos':'E1',
                            'E1_neg':'-E1',}
        self.split_juncs = {'J_start':'J0',
                            'J_mid':'J1',
                            'J_end':'J2',}
        self.internal_edges = {'upper':'J1_0',
                               'lower':'J1_1',}
        self.num_of_rl_lanes = 1 # lanes right to left
        self.num_of_lr_lanes = 1 # lanes left to right

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
    split_net_param = split_road_params()
    intersection_sim_net_make.split_road_sim_net_make(filenames.net_file,
                                                      35.00,
                                                      split_net_param.split_edges,
                                                      split_net_param.split_juncs,
                                                      split_net_param.num_of_rl_lanes,
                                                      split_net_param.num_of_lr_lanes,
                                                      split_net_param.internal_edges)
    intersection_rou_make.split_road_rou_make(split_net_param.split_edges['E0_pos'],
                                              split_net_param.split_edges['E0_neg'],
                                              split_net_param.split_edges['E1_pos'],
                                              split_net_param.split_edges['E1_neg'],'500.00',filenames.rou_file)
    cfg_header_xml.appendChild(input_header_make(filenames.net_file,filenames.rou_file,cfg_file))
    split_cfg_xml = cfg_file.toprettyxml(indent="\t")
    with open(filenames.cfg_file, 'w') as xml_file:
        xml_file.write(split_cfg_xml)
    print("Simple simulation files generated")

