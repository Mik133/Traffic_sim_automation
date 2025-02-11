#---Written by Michael Popov and Yuval Marsh---
# Imports:
from xml.dom import minidom
from Simple_road_sim import routesObject
from Junction_sim import carFlowObject

def split_road_rou_make(edge_0_pos,edge_0_neg,edge_1_pos,edge_1_neg,vehs_per_hour,file_name):
    split_road_rou = minidom.Document()
    routes_obj = routesObject.routeHeader()
    routes_xml = routes_obj.to_XML(split_road_rou)
    split_road_rou.appendChild(routes_xml)
    flow_1_obj = carFlowObject.carFlowObject("f_0","0.00",edge_1_neg,edge_0_neg,"3600.00",vehs_per_hour)
    flow_1_xml = flow_1_obj.to_XML(split_road_rou)
    routes_xml.appendChild(flow_1_xml)
    flow_2_obj = carFlowObject.carFlowObject("f_1","0.00",edge_0_pos,edge_1_pos,"3600.00",vehs_per_hour)
    flow_2_xml = flow_2_obj.to_XML(split_road_rou)
    routes_xml.appendChild(flow_2_xml)
    split_road_rou_xml = split_road_rou.toprettyxml(indent="\t")
    with open(file_name, 'w') as xml_file:
        xml_file.write(split_road_rou_xml)

def half_junc_rou_maker(edges,flows,file_name):
    half_junc_rou = minidom.Document()
    routes_obj = routesObject.routeHeader()
    routes_xml = routes_obj.to_XML(half_junc_rou)
    half_junc_rou.appendChild(routes_xml)
    flow_0_obj = carFlowObject.carFlowObject('f_0','0.00',edges['r_h'],edges['u_r'],'3600.00',flows['flow0'])
    flow_0_xml = flow_0_obj.to_XML(half_junc_rou)
    routes_xml.appendChild(flow_0_xml)
    flow_1_obj = carFlowObject.carFlowObject('f_1','0.00',edges['r_h'],edges['l_h'],'3600.00',flows['flow1'])
    flow_1_obj_xml = flow_1_obj.to_XML(half_junc_rou)
    routes_xml.appendChild(flow_1_obj_xml)
    flow_2_obg = carFlowObject.carFlowObject('f_2','0.00',edges['u_l'],edges['r_l'],'3600.00',flows['flow2'])
    flow_2_obg_xml = flow_2_obg.to_XML(half_junc_rou)
    routes_xml.appendChild(flow_2_obg_xml)
    flow_3_obj = carFlowObject.carFlowObject('f_3','0.00',edges['u_l'],edges['l_h'],'3600.00',flows['flow3'])
    flow_3_obj_xml = flow_3_obj.to_XML(half_junc_rou)
    routes_xml.appendChild(flow_3_obj_xml)
    flow_4_obj = carFlowObject.carFlowObject('f_4','0.00',edges['l_l'],edges['u_r'],'3600.00',flows['flow4'])
    flow_4_obj_xml = flow_4_obj.to_XML(half_junc_rou)
    routes_xml.appendChild(flow_4_obj_xml)
    flow_5_obj = carFlowObject.carFlowObject('f_5','0.00',edges['l_l'],edges['u_r'],'3600.00',flows['flow5'])
    flow_5_obj_xml = flow_5_obj.to_XML(half_junc_rou)
    routes_xml.appendChild(flow_5_obj_xml)
    half_junc_rou_xml = half_junc_rou.toprettyxml(indent="\t")
    with open(file_name, 'w') as xml_file:
        xml_file.write(half_junc_rou_xml)

