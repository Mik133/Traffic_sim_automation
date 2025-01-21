#---Written by Michael Popov and Yuval Marsh---
#--This is main file to run tests--

#Imports
import Simple_road_sim.netHeaderObject as nho
import Simple_road_sim.locationHeaderObject as lho
import Simple_road_sim.edgeObject as edgeObj
import Simple_road_sim.junctionObject as junctObj

from xml.dom import minidom

from Simple_road_sim.simple_sim_utils import PI_Const
from Simple_road_sim.simple_sim_utils import calculate_shapes
from Simple_road_sim.simple_sim_utils import calculate_conv_boundaries

def simple_sim_net_make(simple_sim_args_object):
    edge_0 = 'E0'# TO BE ENTERED FROM EXTERNAL(DEBUG)
    edge_1 = 'E1'# TO BE ENTERED FROM EXTERNAL(DEBUG)
    junction_0 = "J0"# TO BE ENTERED FROM EXTERNAL(DEBUG)
    junction_1 = "J1"# TO BE ENTERED FROM EXTERNAL(DEBUG)
    speed = "13.89"# TO BE ENTERED FROM EXTERNAL(DEBUG)
    num_of_lanes = 4# TO BE ENTERED FROM EXTERNAL(DEBUG)
    # Create lane names
    inc_lanes_j1 = ""
    lane_list = []
    for lane_num in range(num_of_lanes):
        inc_lanes_j1 += edge_0 + f"_{lane_num} "
        lane_list.append(edge_0 + f"_{lane_num}")
    # Base args:
    inc_lanes_j1 = inc_lanes_j1[:-1]
    road_length = 150  # meters # TO BE ENTERED FROM EXTERNAL(DEBUG)
    angle_degrees = 0 # Default is horizontal road # TO BE ENTERED FROM EXTERNAL(DEBUG)
    # Make XML Object
    simple_net = minidom.Document()
    # Net header create and add
    net_header_obj = nho.netHeader("1.16","5","5.5") # TO BE ENTERED FROM EXTERNAL(DEBUG)
    net_header_xml = net_header_obj.to_XML(simple_net)
    simple_net.appendChild(net_header_xml)
    # Calculate shapes and conv boundaries for location and lanes
    shape, j0_shape, j1_shape = calculate_shapes(road_length, angle_degrees)
    conv_boundary = calculate_conv_boundaries(shape)
    # Create Location header and add
    location_header_object = lho.locationHeader(conv_boundary)
    location_header_xml = location_header_object.to_XML(simple_net)
    net_header_xml.appendChild(location_header_xml)
    # Create and add edge & lanes(edge 0 is Left->Right , and edge 1 is Right->Left)
    edge0_object = edgeObj.edgeObject(edge_0,num_of_lanes,f"{road_length}",junction_0,junction_1,
                                      " ".join([f"{x},{y}" for x, y in shape]),speed)
    edge1_object = edgeObj.edgeObject(edge_1, num_of_lanes, f"{road_length}", junction_1, junction_0,
                                      " ".join([f"{x},{y}" for x, y in shape]), speed)
    edge0_xml = edge0_object.to_XML(simple_net)
    edge1_xml = edge1_object.to_XML(simple_net)
    net_header_xml.appendChild(edge0_xml)
    net_header_xml.appendChild(edge1_xml)
    # Create and add Junctions
    j0_obj = junctObj.junctionObject(junction_0,"dead_end",str(shape[0][0]),str(shape[0][1]),"",""," ".join([f"{x},{y}" for x, y in j0_shape]))
    j1_obj = junctObj.junctionObject(junction_1,"dead_end",str(shape[1][0]),str(shape[1][1]),inc_lanes_j1,""," ".join([f"{x},{y}" for x, y in j1_shape]))
    j0_xml = j0_obj.to_XML(simple_net)
    j1_xml = j1_obj.to_XML(simple_net)
    net_header_xml.appendChild(j0_xml)
    net_header_xml.appendChild(j1_xml)
    # File generate
    simple_net_xml = simple_net.toprettyxml(indent="\t")
    with open("simple_net.net.xml",'w') as xml_file:
        xml_file.write(simple_net_xml)

