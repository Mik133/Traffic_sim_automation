#---Written by Michael Popov and Yuval Marsh---
# Imports:
from xml.dom import minidom
from Simple_road_sim import routesObject
from Junction_sim import carFlowObject

def split_road_rou_make(edge_0_pos,edge_0_neg,edge_1_pos,edge_1_neg,vehs_per_hour):
    split_road_rou = minidom.Document()
    routes_obj = routesObject.routeHeader()
    routes_xml = routes_obj.to_XML(split_road_rou)
    split_road_rou.appendChild(routes_xml)
    flow_1_obj = carFlowObject.carFlowObject("f_0","0.00",edge_1_neg,edge_1_pos,"3600.00",vehs_per_hour)
    flow_1_xml = flow_1_obj.to_XML(split_road_rou)
    routes_xml.appendChild(flow_1_xml)
    flow_2_obj = carFlowObject.carFlowObject("f_1","0.00",edge_0_pos,edge_0_neg,"3600.00",vehs_per_hour)
    flow_2_xml = flow_2_obj.to_XML(split_road_rou)
    routes_xml.appendChild(flow_2_xml)
    split_road_rou_xml = split_road_rou.toprettyxml(indent="\t")
    with open("split_rou.rou.xml", 'w') as xml_file:
        xml_file.write(split_road_rou_xml)


