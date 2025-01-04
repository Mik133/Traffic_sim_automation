import math
import xml.etree.ElementTree as ET

# Pretty print XML
def prettify(elem):
    from xml.dom import minidom
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def calculate_shapes(road_length, angle_degrees=0):
    # Default starting point
    x_start, y_start = 0.0, 0.0

    # Calculate end point based on angle and road length
    angle_radians = math.radians(angle_degrees)
    x_end = x_start + road_length * math.cos(angle_radians)
    y_end = y_start + road_length * math.sin(angle_radians)

    # Shape coordinates
    shape = [(x_start, y_start), (x_end, y_end)]

    # Generate shapes for both junctions
    j0_shape = [(x_start, y_start), (x_start, y_start - 3)]  # Adjust for visual dead-end
    j1_shape = [(x_end, y_end - 3), (x_end, y_end)]

    return shape, j0_shape, j1_shape

def calculate_conv_boundaries(shape):
    # Extract boundary values
    x_coords = [point[0] for point in shape]
    y_coords = [point[1] for point in shape]

    # Calculate boundaries
    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)

    return min_x, min_y, max_x, max_y

def generate_xml(road_length, angle_degrees=0):
    # Calculate shapes
    shape, j0_shape, j1_shape = calculate_shapes(road_length, angle_degrees)
    conv_boundary = calculate_conv_boundaries(shape)

    # Create XML structure
    net = ET.Element('net', version="1.16", junctionCornerDetail="5", limitTurnSpeed="5.50")
    location = ET.SubElement(net, 'location',
                              netOffset="0.00,0.00",
                              convBoundary=f"{conv_boundary[0]},{conv_boundary[1]},{conv_boundary[2]},{conv_boundary[3]}",
                              origBoundary="10000000000.00,10000000000.00,-10000000000.00,-10000000000.00",
                              projParameter="!")

    # Add edge
    edge = ET.SubElement(net, 'edge', id="E0", priority="-1")
    edge.set('from', 'J0')
    edge.set('to', 'J1')

    lane = ET.SubElement(edge, 'lane', id="E0_0", index="0", speed="13.89",
                          length=str(road_length),
                          shape=" ".join([f"{x},{y}" for x, y in shape]))

    # Add junctions
    j0 = ET.SubElement(net, 'junction', id="J0", type="dead_end", x=str(shape[0][0]), y=str(shape[0][1]),
                        incLanes="", intLanes="",
                        shape=" ".join([f"{x},{y}" for x, y in j0_shape]))

    j1 = ET.SubElement(net, 'junction', id="J1", type="dead_end", x=str(shape[1][0]), y=str(shape[1][1]),
                        incLanes="E0_0", intLanes="",
                        shape=" ".join([f"{x},{y}" for x, y in j1_shape]))

    # Write to XML file with pretty formatting
    with open("network.net.xml", "w") as files:
        files.write(prettify(net))

# Input values
road_length = 250
angle_degrees = 0  # Default is horizontal road

# Generate XML
generate_xml(road_length, angle_degrees)
print("XML file 'network.net.xml' generated successfully.")
