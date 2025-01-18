#---Written by Michael Popov and Yuval Marsh---

# Consts
NEGATIVE_SIDE = "Negative"
POSITIVE_SIDE = "Positive"

# Imports
import math
import edgeObject
import junctionObject

def make_internal_edge_shapes(road_length):
    print("DEBUG")

def make_regular_edge_shapes(road_length,x_init,y_init,lane_width,side):
    if side == POSITIVE_SIDE:
        x_final = x_init + road_length
    else:
        x_final = x_init - road_length
    y_final = y_init + lane_width
    shape = {'x_0':x_init,
             'x_f':x_final,
             'y_0':y_init,
             'y_f':y_final}
    return shape

def make_regular_junction_shapes(x_init,y_init,lane_width):
    x_mid = x_init
    y_mid = y_init + lane_width * 2
    x_final = x_init
    y_final = y_init
    shape = {'x_0':x_init,
             'y_0':y_init,
             'x_m':x_mid,
             'y_m':y_mid,
             'x_f':x_final,
             'y_f':y_final}
    return shape

def make_priority_junction_shapes(x_init,y_init,lane_width,road_length):
    x_1 = x_init + road_length + 0.3
    y_1 = y_init + 5
    x_2 = x_init + road_length + 0.3
    y_2 = y_init - 1.5
    x_3 = x_init + road_length
    y_3 = y_init - 1.5
    x_4 = x_init + road_length
    y_4 = y_init + 5
    shape = {'x_1':x_1,
             'y_1':y_1,
             'x_2':x_2,
             'y_2':y_2,
             'x_3':x_3,
             'y_3':y_3,
             'x_4':x_4,
             'y_4':y_4,}
    return shape

def calc_conv_boundary(x_init, y_init, road_length, lane_width):
    conv_boundary = [x_init,y_init,x_init + road_length * 2,y_init + lane_width * 2]
    return conv_boundary

def shape_to_string(shape):
    shape_string = f"{shape['x_0']},{shape['y_0']} {shape['x_f']},{shape['y_f']}"
    return shape_string

def jucntion_shape_to_string_six_vals(shape):
    shape_string = f"{shape['x_0']},{shape['y_0']} {shape['x_m']},{shape['y_m']} {shape['x_f']},{shape['y_f']}"
    return shape_string

def junction_shape_to_string_eight_vals(shape):
    shape_string = f"{shape['x_1']},{shape['y_1']} {shape['x_2']},{shape['y_2']} {shape['x_3']},{shape['y_3']} {shape['x_4']},{shape['y_4']}"
    return shape_string

def regular_edge_xml_maker(e_id,e_from,e_to,num_of_lanes,road_length,lane_shape,speed,net_xml,net_header_xml):
    new_edge = edgeObject.RegularEdgeObject(e_id,e_from,e_to,num_of_lanes,road_length,lane_shape,speed,net_xml)
    new_edge_xml = new_edge.to_XML()
    net_header_xml.appendChild(new_edge_xml)

def dead_end_junction_maker(j_id,x_j,y_j,inc_lanes,int_lanes,shape,net_xml,net_header_xml):
    new_junction = junctionObject.JunctDeadEndObject(j_id,x_j,y_j,inc_lanes,int_lanes,shape,net_xml)
    new_junction_xml = new_junction.to_XML()
    net_header_xml.appendChild(new_junction_xml)

def priority_junction_maker(j_id,x_j,y_j,inc_lanes,int_lanes,shape,net_xml,num_of_req,req_responses,req_foes,req_cont,net_header_xml):
    new_junction = junctionObject.JunctionPriorityObject(j_id,x_j,y_j,inc_lanes,int_lanes,shape,net_xml,num_of_req,req_responses,req_foes,req_cont)
    new_junction_xml = new_junction.to_XML()
    net_header_xml.appendChild(new_junction_xml)