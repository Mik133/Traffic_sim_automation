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


def split_road_sim_net_make(file_name,road_length,edges,junctions,num_of_rl_lanes,num_of_lr_lanes,internal_edges):
    # Inputs:
    lane_width = 2.00 # Constant
    x_init = 0.00 # Constant
    y_init = 0.00 # Constant
    num_of_reqs = num_of_rl_lanes + num_of_lr_lanes
    req_string = ''
    req_responses = []
    req_foes = []
    req_cont = []
    for reqs in range(num_of_reqs):
        req_string += '0'
    for req in range(num_of_reqs):
        req_responses.append(req_string)
        req_foes.append(req_string)
        req_cont.append('0')
    # Make inclanes strings
    jstart_inclanes = ''
    for lane in range(num_of_lr_lanes):
        jstart_inclanes += edges['E0_neg'] + f"_{lane} "
    jstart_inclanes = jstart_inclanes[:-1]
    jend_inclanes = ''
    for lane in range(num_of_rl_lanes):
        jend_inclanes += edges['E1_pos'] + f"_{lane} "
    jend_inclanes = jend_inclanes[:-1]
    jmid_inclanes = jstart_inclanes + " " + jend_inclanes
    internal_edges_lanes_lr_list = []
    internal_edges_lanes_lr_string = ''
    for lane in range(num_of_lr_lanes):
        internal_edges_lanes_lr_list.append(internal_edges['upper'] + f"_{lane}")
        internal_edges_lanes_lr_string += ":" + internal_edges['upper'] + f"_{lane} "
    internal_edges_lanes_lr_string = internal_edges_lanes_lr_string[:-1]
    internal_edges_lanes_rl_list = []
    internal_edges_lanes_rl_string = ''
    for lane in range(num_of_rl_lanes):
        internal_edges_lanes_rl_list.append(internal_edges['lower'] + f"_{lane}")
        internal_edges_lanes_rl_string += ":" + internal_edges['lower'] + f"_{lane} "
    internal_edges_lanes_rl_string = internal_edges_lanes_rl_string[:-1]
    all_intenal_lanes = internal_edges_lanes_lr_string + " " + internal_edges_lanes_rl_string
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
    regular_edge_xml_maker(edges['E0_pos'],junctions['J_start'],junctions['J_mid'],num_of_rl_lanes,f"{road_length}",E0_pos_shape_string,'13.89',intersection_net,net_header_xml)
    regular_edge_xml_maker(edges['E0_neg'],junctions['J_mid'],junctions['J_start'],num_of_lr_lanes,f"{road_length}",E0_neg_shape_string,'13.89',intersection_net,net_header_xml)
    regular_edge_xml_maker(edges['E1_pos'],junctions['J_mid'],junctions['J_end'],num_of_rl_lanes,f"{road_length}",E1_pos_shape_string,'13.89',intersection_net,net_header_xml)
    regular_edge_xml_maker(edges['E1_neg'],junctions['J_end'],junctions['J_mid'],num_of_lr_lanes,f"{road_length}",E1_neg_shape_string,'13.89',intersection_net,net_header_xml)
    # Make internal edges
    internal_edge_maker(internal_edges['upper'],1,f"{road_length}",J1_0_shape_string,'13.89',intersection_net,net_header_xml)
    internal_edge_maker(internal_edges['lower'],1,f"{road_length}",J1_1_shape_string,'13.89',intersection_net,net_header_xml)
    # Make dead end Junctions
    dead_end_junction_maker(junctions['J_start'],f"{J0_shape['x_0']}",f"{J0_shape['y_0']}",jstart_inclanes,'',J0_shape_string,intersection_net,net_header_xml)
    dead_end_junction_maker(junctions['J_end'],f"{J2_shape['x_0']}",f"{J2_shape['y_0']}",jend_inclanes,'',J2_shape_string,intersection_net,net_header_xml)
    # Make priority junctions
    priority_junction_maker(junctions['J_mid'],f"{x_init + road_length}",f"{y_init + lane_width}",jmid_inclanes,all_intenal_lanes,J1_shape_string,intersection_net,num_of_reqs
                            ,req_responses,req_foes,req_cont,net_header_xml)
    # Make Connections
    for lane_to_connect in range(num_of_lr_lanes):
        connection_maker(edges['E1_neg'],edges['E0_neg'],f"{lane_to_connect}",f"{lane_to_connect}",
                         internal_edges_lanes_lr_list[lane_to_connect],'s','M',intersection_net,net_header_xml)
        connection_maker(internal_edges['upper'],edges['E0_neg'],f"{lane_to_connect}",f"{lane_to_connect}",
                         '','s','M',intersection_net,net_header_xml)
    for lane_to_connect in range(num_of_rl_lanes):
        connection_maker(edges['E0_pos'],edges['E1_pos'],f"{lane_to_connect}",f"{lane_to_connect}",
                         internal_edges_lanes_rl_list[lane_to_connect],'s','M',intersection_net,net_header_xml)
        connection_maker(internal_edges['lower'],edges['E0_pos'],f"{lane_to_connect}",f"{lane_to_connect}",
                         '','s','M',intersection_net,net_header_xml)

    # connection_maker(edges['E1_neg'],edges['E0_neg'],'0','0','J1_0_0','s','M',intersection_net,net_header_xml)
    # connection_maker(edges['E0_pos'], edges['E1_pos'], '0', '0', 'J1_1_0', 's', 'M', intersection_net, net_header_xml)
    # connection_maker('J1_0', edges['E0_neg'], '0', '0', '', 's', 'M', intersection_net, net_header_xml)
    # connection_maker('J1_1', edges['E1_pos'], '0', '0', '', 's', 'M', intersection_net, net_header_xml)
    # Make XML net file
    intersection_net_xml = intersection_net.toprettyxml(indent="\t")
    with open(file_name, 'w') as xml_file:
        xml_file.write(intersection_net_xml)