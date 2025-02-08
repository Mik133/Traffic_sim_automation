#---Written by Michael Popov and Yuval Marsh---
from PIL.PdfParser import IndirectObjectDef

# Consts
NEGATIVE_SIDE = "Negative"
POSITIVE_SIDE = "Positive"
GOING_DOWN = "down"
GOING_UP = "up"

# Imports
from Junction_sim import junctionObject
from Junction_sim import connectionObject
from Junction_sim import edgeObject
from Junction_sim import trafficLightObject

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

def make_regular_edge_shape_vertical(road_length,x_init,y_init,lane_width,side):
    if side == GOING_UP:
        y_final = y_init + road_length
    else:
        y_final = y_init - road_length
    x_final = x_init + lane_width
    shape = {'x_0': x_init,
             'x_f': x_final,
             'y_0': y_init,
             'y_f': y_final}
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

def dead_end_junction_six_vals(x_init,y_init,lane_width):
    shape = {'x_0':x_init,
             'y_0':y_init + 0.5,
             'x_m':x_init - 0.02,
             'y_m':y_init + lane_width,
             'x_f':x_init,
             'y_f':y_init}
    return shape

def internal_edge_six_points_type_1_3(x_init,y_init):
    shape = {'x_0':x_init,'y_0':y_init,
             'x_m':x_init + 3.85,'y_m':y_init + 0.50,
             'x_f':x_init + 4.00,'y_f':y_init + 0.60}
    return shape

def internal_edge_shapes(x_init,y_init,lane_width,road_length,side):
    x_1 = x_init + road_length + 0.1
    y_1 = y_init + lane_width
    x_2 = x_1 + 0.3
    y_2 = y_init + lane_width
    if side == POSITIVE_SIDE:
        shape = {'x_0':x_1,
                 'y_0':y_1,
                 'x_f':x_2,
                 'y_f':y_2,}
    else:
        shape = {'x_0':x_2,
                 'y_0':y_2,
                 'x_f':x_1,
                 'y_f':y_1,}
    return shape

def internal_edge_ten_points_type_j1_0(x_init,y_init):
    shape = {'x_1':x_init,'y_1':y_init,
             'x_2':x_init - 2.50,'y_2':y_init + 0.40,
             'x_3':x_init - 4.20,'y_3':y_init + 0.50,
             'x_4':x_init - 5.20,'y_4':y_init + 3.20,
             'x_5':x_init - 5.50,'y_5':y_init + 4.80}
    return shape

def internal_edge_ten_points_type_j1_4(x_init,y_init):
    shape = {'x_1':x_init,'y_1':y_init,
             'x_2':x_init - 0.30,'y_2':y_init - 2.50,
             'x_3':x_init - 2.40,'y_3':y_init - 4.20,
             'x_4':x_init - 3.10,'y_4':y_init - 5.15,
             'x_5':x_init - 5.60,'y_5':y_init - 5.60}
    return shape

def internal_edge_ten_points_type_j1_5(x_init,y_init):
    shape = {'x_1':x_init,'y_1':y_init,
             'x_2':x_init + 0.60,'y_2':y_init - 3.90,
             'x_3':x_init + 2.25,'y_3':y_init - 6.60,
             'x_4':x_init + 5.00,'y_4':y_init - 8.30,
             'x_5':x_init + 8.80,'y_5':y_init - 8.90}
    return shape

def internal_edge_eight_points_type_j1_6(x_init,y_init):
    shape = {'x_1': x_init, 'y_1': y_init,
             'x_2': x_init + 2.60, 'y_2': y_init + 1.60,
             'x_3': x_init + 4.30, 'y_3': y_init + 4.30,
             'x_4': x_init + 4.80, 'y_4': y_init + 8.20}
    return shape

def traffic_light_junction_shape(x_init,y_init):
    shape = {'x_0':x_init, 'y_0':y_init,
             'x_1':x_init - 0.06, 'y_1':y_init - 6.40,
             'x_2':x_init - 18.40, 'y_2':y_init - 6.30,
             'x_3':x_init - 18.40, 'y_3':y_init + 0.10,
             'x_4':x_init - 12.20, 'y_4':y_init + 0.50,
             'x_5':x_init - 11.40, 'y_5':y_init + 1.10,
             'x_6':x_init - 10.85, 'y_6':y_init + 1.85,
             'x_7':x_init - 10.55, 'y_7':y_init + 2.85,
             'x_8':x_init - 10.45, 'y_8':y_init + 4.10,
             'x_9':x_init - 4.00, 'y_9':y_init + 4.10,
             'x_10':x_init - 3.60 , 'y_10':y_init + 1.85,
             'x_11':x_init - 3.00, 'y_11':y_init + 1.05,
             'x_12':x_init - 2.20, 'y_12':y_init + 0.50,
             'x_13':x_init - 1.20, 'y_13':y_init + 0.10}
    return shape

def internal_edge_four_points_type(x_init,y_init,side):
    if side == POSITIVE_SIDE:
        shape = {'x_0':x_init,'y_0':y_init,
                 'x_f':x_init -  14.50,'y_f':y_init + 0.10}
    else:
        shape = {'x_0':x_init,'y_0':y_init,
                 'x_f':x_init +  14.50,'y_f':y_init - 0.10}
    return shape


def internal_shape_to_string_ten_points(shape):
    return (f"{shape['x_1']},{shape['y_1']} {shape['x_2']},{shape['y_2']} {shape['x_3']},{shape['y_3']} "
            f"{shape['x_4']},{shape['y_4']} {shape['x_5']},{shape['y_5']}")

def traffic_light_shape_to_string(shape):
    return (f"{shape['x_0']},{shape['y_0']} {shape['x_1']},{shape['y_1']} {shape['x_2']},{shape['y_2']} "
            f"{shape['x_3']},{shape['y_3']} {shape['x_4']},{shape['y_4']} {shape['x_5']},{shape['y_5']} "
            f"{shape['x_6']},{shape['y_6']} {shape['x_7']},{shape['y_7']} {shape['x_8']},{shape['y_8']} "
            f"{shape['x_9']},{shape['y_9']} {shape['x_10']},{shape['y_10']} {shape['x_11']},{shape['y_11']} "
            f"{shape['x_12']},{shape['y_12']} {shape['x_13']},{shape['y_13']} ")


def calc_conv_boundary_half_junc(road_length):
    conv_boundary = [0.00 - 1,0.00 - 1.5,road_length * 2.00 + 5,road_length + 5.00]
    return conv_boundary

def calc_conv_boundary_split(x_init, y_init, road_length, lane_width):
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
    new_junction = junctionObject.JunctDeadEndObject(j_id, x_j, y_j, inc_lanes, int_lanes, shape, net_xml)
    new_junction_xml = new_junction.to_XML()
    net_header_xml.appendChild(new_junction_xml)

def priority_junction_maker(j_id,x_j,y_j,inc_lanes,int_lanes,shape,net_xml,num_of_req,req_responses,req_foes,req_cont,net_header_xml):
    new_junction = junctionObject.JunctionPriorityObject(j_id, x_j, y_j, inc_lanes, int_lanes, shape, net_xml, num_of_req, req_responses, req_foes, req_cont)
    new_junction_xml = new_junction.to_XML()
    net_header_xml.appendChild(new_junction_xml)

def connection_maker(c_from,c_to,c_from_lane,c_to_lane,c_via,c_dir,c_state,net_xml,net_header_xml):
    new_connection = connectionObject.conncectionObject(c_from,c_to,c_from_lane,c_to_lane,c_via,c_dir,c_state,net_xml)
    new_connection_xml = new_connection.to_XML()
    net_header_xml.appendChild(new_connection_xml)

def connection_maker_link_index(c_from,c_to,c_from_lane,c_to_lane,c_via,c_tl,c_link_index,c_dir,c_state,net_xml,net_header_xml):
    new_connection = connectionObject.ConncectionObjectLinkIndex(c_from, c_to, c_from_lane, c_to_lane, c_via,c_tl, c_link_index, c_dir, c_state, net_xml)
    new_connection_xml = new_connection.to_XML()
    net_header_xml.appendChild(new_connection_xml)

def internal_edge_maker(e_id,num_of_lanes,lane_length,lane_shapes,speed,net_xml,net_header_xml):
    new_edge = edgeObject.InternalEdgeObject(e_id,num_of_lanes,lane_length,lane_shapes,speed,net_xml)
    new_edge_xml = new_edge.to_XML()
    net_header_xml.appendChild(new_edge_xml)

def internal_junction_maker(j_id,j_type,x_j,y_j,inc_lanes,int_lanes,req_responses,req_foes,req_cont,num_of_req,net_xml,net_header_xml):
    new_junction = junctionObject.JunctionInternalTrafficLightObject(j_id,j_type,x_j,y_j,inc_lanes,int_lanes,net_xml,req_responses,req_foes,req_cont,num_of_req)
    new_junction_xml = new_junction.to_XML()
    net_header_xml.appendChild(new_junction_xml)

def traffic_light_maker(tl_id,tl_type,tl_pid,tl_offset,tl_dur,tl_state,num_of_phase,net_xml,net_header_xml):
    new_tl = trafficLightObject.TrafficLightObject(tl_id,tl_type,tl_pid,tl_offset,tl_dur,tl_state,num_of_phase,net_xml)
    new_tl_xml = new_tl.to_xml()
    net_header_xml.appendChild(new_tl_xml)

def make_lanes_string(num_of_lanes,edge):
    for lane in range(num_of_lanes):
        lanes_s = edge + "_" + f"{lane} "
    lanes_s = lanes_s[:-1]
    return lanes_s
