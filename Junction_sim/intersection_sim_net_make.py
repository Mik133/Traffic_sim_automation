#---Written by Michael Popov and Yuval Marsh---

#Imports
from xml.dom import minidom

import Simple_road_sim.netHeaderObject as nho
import Simple_road_sim.locationHeaderObject as lho

from Junction_sim.intersection_sim_utils import make_regular_edge_shapes, POSITIVE_SIDE, NEGATIVE_SIDE, \
    make_regular_junction_shapes, calc_conv_boundary, shape_to_string, regular_edge_xml_maker, dead_end_junction_maker, \
    jucntion_shape_to_string_six_vals, make_priority_junction_shapes, junction_shape_to_string_eight_vals, \
    priority_junction_maker, connection_maker, internal_edge_shapes, internal_edge_maker

# Objects import


def split_road_sim_net_make(file_name):
    # Inputs:
    road_length = 150.00
    lane_width = 2.00
    x_init = 0.00
    y_init = 0.00
    num_of_reqs = 2
    req_responses = ['00','00']
    req_foes = ['00','00']
    req_cont = ['0','0']
    # Create XML Doc
    intersection_net = minidom.Document()
    # Create Net header Entry
    net_header_obj = nho.netHeader('1.16','5','5.50')
    net_header_xml = net_header_obj.to_XML(intersection_net)
    intersection_net.appendChild(net_header_xml)
    # Create Location entry
    conv_boundary = calc_conv_boundary(x_init,y_init,road_length,lane_width)
    location_header_obj = lho.locationHeader(conv_boundary)
    location_header_xml = location_header_obj.to_XML(intersection_net)
    net_header_xml.appendChild(location_header_xml)
    # Calculate shapes for regular edges
    E0_pos_shape = make_regular_edge_shapes(road_length,x_init,y_init,lane_width,POSITIVE_SIDE)
    E0_pos_shape_string = shape_to_string(E0_pos_shape)
    E0_neg_shape = make_regular_edge_shapes(road_length,E0_pos_shape['x_f'],E0_pos_shape['y_f'],lane_width,NEGATIVE_SIDE)
    E0_neg_shape_string = shape_to_string(E0_neg_shape)
    E1_pos_shape = make_regular_edge_shapes(road_length,E0_pos_shape['x_f'],y_init,lane_width,POSITIVE_SIDE)
    E1_pos_shape_string = shape_to_string(E1_pos_shape)
    E1_neg_shape = make_regular_edge_shapes(road_length,E1_pos_shape['x_f'],E1_pos_shape['y_f'],lane_width,NEGATIVE_SIDE)
    E1_neg_shape_string = shape_to_string(E1_neg_shape)
    # Calculate shapes for regular junctions
    J0_shape = make_regular_junction_shapes(x_init,y_init,lane_width)
    J0_shape_string = jucntion_shape_to_string_six_vals(J0_shape)
    J2_shape = make_regular_junction_shapes(E1_pos_shape['x_f'],E1_pos_shape['y_f'],lane_width)
    J2_shape_string = jucntion_shape_to_string_six_vals(J2_shape)
    # Calculate shapes for priority jucntions
    J1_shape = make_priority_junction_shapes(x_init,y_init,lane_width,road_length)
    J1_shape_string = junction_shape_to_string_eight_vals(J1_shape)
    # Calculate shapes for internal edges
    J1_0_shape = internal_edge_shapes(x_init, y_init, lane_width, road_length, NEGATIVE_SIDE)
    J1_0_shape_string = shape_to_string(J1_0_shape)
    J1_1_shape = internal_edge_shapes(x_init, y_init, lane_width, road_length, POSITIVE_SIDE)
    J1_1_shape_string = shape_to_string(J1_1_shape)
    # Make regular edges
    regular_edge_xml_maker('E0','J0','J1',1,f"{road_length}",E0_pos_shape_string,'13.89',intersection_net,net_header_xml)
    regular_edge_xml_maker('-E0','J1','J0',1,f"{road_length}",E0_neg_shape_string,'13.89',intersection_net,net_header_xml)
    regular_edge_xml_maker('E1','J1','J2',1,f"{road_length}",E1_pos_shape_string,'13.89',intersection_net,net_header_xml)
    regular_edge_xml_maker('-E1','J2','J1',1,f"{road_length}",E1_neg_shape_string,'13.89',intersection_net,net_header_xml)
    # Make internal edges
    internal_edge_maker('J1_0',1,f"{road_length}",J1_0_shape_string,'13.89',intersection_net,net_header_xml)
    internal_edge_maker('J1_1',1,f"{road_length}",J1_1_shape_string,'13.89',intersection_net,net_header_xml)
    # Make dead end Junctions
    dead_end_junction_maker('J0',f"{J0_shape['x_0']}",f"{J0_shape['y_0']}",'-E0_0','',J0_shape_string,intersection_net,net_header_xml)
    dead_end_junction_maker('J2',f"{J2_shape['x_0']}",f"{J2_shape['y_0']}",'E1_0','',J2_shape_string,intersection_net,net_header_xml)
    # Make priority junctions
    priority_junction_maker('J1',f"{x_init + road_length}",f"{y_init + lane_width}",'-E1_0 E0_0',':J1_0_0 :J1_1_0',J1_shape_string,intersection_net,num_of_reqs
                            ,req_responses,req_foes,req_cont,net_header_xml)
    # Make Connections
    connection_maker('-E1','-E0','0','0','J1_0_0','s','M',intersection_net,net_header_xml)
    connection_maker('E0', 'E1', '0', '0', 'J1_1_0', 's', 'M', intersection_net, net_header_xml)
    connection_maker('J1_0', '-E0', '0', '0', '', 's', 'M', intersection_net, net_header_xml)
    connection_maker('J1_1', 'E1', '0', '0', '', 's', 'M', intersection_net, net_header_xml)
    # Make XML net file
    intersection_net_xml = intersection_net.toprettyxml(indent="\t")
    with open(file_name, 'w') as xml_file:
        xml_file.write(intersection_net_xml)