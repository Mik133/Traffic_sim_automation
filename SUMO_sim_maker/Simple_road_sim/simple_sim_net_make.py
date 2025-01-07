#--This is main file to run tests--

#Imports
import netHeaderObject as nho
import locationHeaderObject as lho
import edgeObject as edgeObj
import junctionObject as junctObg

from xml.dom import minidom

from simple_sim_utils import calculate_shapes
from simple_sim_utils import calculate_conv_boundaries

def simple_sim_net_make():
    edge_0 = 'E0'# TO BE ENTERED FROM EXTERNAL(DEBUG)
    junction_0 = "J0"# TO BE ENTERED FROM EXTERNAL(DEBUG)
    junction_1 = "J1"# TO BE ENTERED FROM EXTERNAL(DEBUG)
    speed = "13.89"# TO BE ENTERED FROM EXTERNAL(DEBUG)
    num_of_lanes = 2
    # Create lane names
    inc_lanes_j1 = ""
    for lane_num in range(num_of_lanes):
        inc_lanes_j1 += edge_0 + f"_{lane_num} "
    # Base args:
    inc_lanes_j1 = inc_lanes_j1[:-1]
    road_length = 150  # meters # TO BE ENTERED FROM EXTERNAL(DEBUG)
    angle_degrees = 0  # Default is horizontal road # TO BE ENTERED FROM EXTERNAL(DEBUG)
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
    # Create and add edge & lanes
    edge_object = edgeObj.edgeObject(edge_0,num_of_lanes,f"{road_length}",junction_0,junction_1," ".join([f"{x},{y}" for x, y in shape]),speed)
    edge_xml = edge_object.to_XML(simple_net)
    net_header_xml.appendChild(edge_xml)
    # Create and add Junctions
    j0_obj = junctObg.junctionObject(junction_0,"dead_end",str(shape[0][0]),str(shape[0][1]),"",""," ".join([f"{x},{y}" for x, y in j0_shape]))
    j1_obj = junctObg.junctionObject(junction_1,"dead_end",str(shape[1][0]),str(shape[1][1]),inc_lanes_j1,""," ".join([f"{x},{y}" for x, y in j1_shape]))
    j0_xml = j0_obj.to_XML(simple_net)
    j1_xml = j1_obj.to_XML(simple_net)
    net_header_xml.appendChild(j0_xml)
    net_header_xml.appendChild(j1_xml)
    # File generate
    simple_net_xml = simple_net.toprettyxml(indent="\t")
    with open("simple_net.net.xml",'w') as xml_file:
        xml_file.write(simple_net_xml)

