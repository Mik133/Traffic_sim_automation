
# Imports:
from xml.dom import minidom
from Simple_road_sim.simple_sim_main import configuration_header_maker

class split_filenames:
    def __init__(self):
        net_file = "split_net.net.xml"
        rou_file = "split_rou.rou.xml"
        cfg_file = "split_cfg.sumocfg"

def split_sim_maker():
    filenames = split_filenames()
    cfg_file = minidom.Document()
    cfg_header_xml = configuration_header_maker(cfg_file)
    cfg_file.appendChild(cfg_header_xml)

