#---Written by Michael Popov and Yuval Marsh---

#Imports
from xml.dom import minidom

import Simple_road_sim.netHeaderObject as nho
import Simple_road_sim.locationHeaderObject as lho

import intersection_sim_utils
from Junction_sim.intersection_sim_utils import make_regular_edge_shapes, POSITIVE_SIDE, NEGATIVE_SIDE, \
    make_regular_junction_shapes, calc_conv_boundary, shape_to_string, regular_edge_xml_maker, dead_end_junction_maker, \
    jucntion_shape_to_string_six_vals

# Objects import
import edgeObject
import laneObject

#def intersection_sim_net_make():
if __name__ == "__main__":
    # Inputs:
    road_length = 150.00
    lane_width = 2.00
    x_init = 0.00
    y_init = 0.00
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
    # Calculate shapes for internal edges

    # Make regular edges
    regular_edge_xml_maker('E0','J0','J1',1,f"{road_length}",E0_pos_shape_string,'13.89',intersection_net,net_header_xml)
    regular_edge_xml_maker('-E0','J1','J0',1,f"{road_length}",E0_neg_shape_string,'13.89',intersection_net,net_header_xml)
    regular_edge_xml_maker('E1','J1','J2',1,f"{road_length}",E1_pos_shape_string,'13.89',intersection_net,net_header_xml)
    regular_edge_xml_maker('-E1','J2','J1',1,f"{road_length}",E1_neg_shape_string,'13.89',intersection_net,net_header_xml)
    # Make dead end Junctions
    dead_end_junction_maker('J0',f"{J0_shape['x_0']}",f"{J0_shape['y_0']}",'-E0_0','',J0_shape_string,intersection_net,net_header_xml)
    dead_end_junction_maker('J2',f"{J2_shape['x_0']}",f"{J2_shape['y_0']}",'E1_0','',J2_shape_string,intersection_net,net_header_xml)
    # Make XML net file
    intersection_net_xml = intersection_net.toprettyxml(indent="\t")
    with open("intersection_net.net.xml", 'w') as xml_file:
        xml_file.write(intersection_net_xml)