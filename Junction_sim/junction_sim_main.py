
# Imports:
from xml.dom import minidom

from Junction_sim.intersection_rou_make import half_junc_rou_maker
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
        self.num_of_rl_lanes = 4 # lanes right to left
        self.num_of_lr_lanes = 7 # lanes left to right
        self.vhs_per_hr = '500.00'

class HalfJunctionParams:
    def __init__(self):
        self.hj_edges = {'l_l':'E0',     # Left low
                         'l_h':'-E0',    # Left high
                         'r_l':'E1',     # Right low
                         'r_h':'-E1',    # Right high
                         'u_l':'-E2',    # Upper left
                         'u_r':'E2',}    # Upper right
        self.dead_end_junc = {'left':'J0',
                              'right':'J2',
                              'up':'J3'}
        self.central_junc = 'J1'
        self.int_junc = 'J1_6_0'
        self.internal_edges = {'rh_ur':'J1_0',
                               'rh_lh':'J1_1',
                               'll_rl':'J1_2',
                               'll_ur':'J1_3',
                               'ul_lh':'J1_4',
                               'ul_rl':'J1_5'}
        self.internal_special = 'J1_6'
        self.turn_direction = {'straight':'s',
                               'left':'l',
                               'right':'r'}
        self.connect_state = {'priority':'O',
                              'optional':'o',
                              'Minor_h':'M',
                              'Minor_l':'m',}
        self.junction_types = {'dead_end':'dead_end',
                               'internal':'internal',
                               'traffic_light':'traffic_light'}
        self.file_names = {'network':'half_junc.net.xml',
                           'rou':'half_junc.rou.xml',
                           'cfg':'half_junc.sumocfg',}
        self.car_flow = {'flow0':'250.00',
                         'flow1':'250.00',
                         'flow2':'250.00',
                         'flow3':'250.00',
                         'flow4':'250.00',
                         'flow5':'250.00',}
        self.traffic_light_times = ['42','3','42','3']
        self.tl_state = ['GGGgrr','yyyyrr','GrrrGG','yrrryy']
        self.num_of_lanes = {'left_low' : 1,
                             'left_high' : 1,
                             'right_low' : 1,
                             'right_high' : 1,
                             'upper_right' : 1,
                             'upper_left' : 1}
        self.total_lanes = (self.num_of_lanes['left_low'] + self.num_of_lanes['left_high'] +
                            self.num_of_lanes['right_low'] + self.num_of_lanes['right_high'] +
                            self.num_of_lanes['upper_right'] + self.num_of_lanes['upper_left'] )

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
                                              split_net_param.split_edges['E1_neg'],
                                              split_net_param.vhs_per_hr,
                                              filenames.rou_file)
    cfg_header_xml.appendChild(input_header_make(filenames.net_file,filenames.rou_file,cfg_file))
    split_cfg_xml = cfg_file.toprettyxml(indent="\t")
    with open(filenames.cfg_file, 'w') as xml_file:
        xml_file.write(split_cfg_xml)
    print("Split road simulation files generated")

def half_junction_maker():
    half_junc_args = HalfJunctionParams()
    intersection_sim_net_make.half_junction_sim_net_make(half_junc_args.hj_edges,
                                                         half_junc_args.dead_end_junc,
                                                         half_junc_args.central_junc,
                                                         half_junc_args.internal_edges,
                                                         half_junc_args.internal_special,
                                                         half_junc_args.int_junc,
                                                         half_junc_args.turn_direction,
                                                         half_junc_args.connect_state,
                                                         half_junc_args.file_names['network'],
                                                         half_junc_args.traffic_light_times,
                                                         half_junc_args.tl_state,
                                                         half_junc_args.num_of_lanes,
                                                         half_junc_args.total_lanes)
    half_junc_rou_maker(half_junc_args.hj_edges,
                        half_junc_args.car_flow,
                        half_junc_args.file_names['rou'])
    cfg_file = minidom.Document()
    cfg_header_xml = configuration_header_maker(cfg_file)
    cfg_file.appendChild(cfg_header_xml)
    cfg_header_xml.appendChild(input_header_make(half_junc_args.file_names['network'],
                                                 half_junc_args.file_names['rou'],
                                                 cfg_file))
    half_junc_cfg_xml = cfg_file.toprettyxml(indent="\t")
    with open(half_junc_args.file_names['cfg'], 'w') as xml_file:
        xml_file.write(half_junc_cfg_xml)
    print("Half junction simulation files generated")



