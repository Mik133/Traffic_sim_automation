import math

class simple_sim_args:
    def __init__(self):
        self.net_file_name = "simple_net.net.xml"
        self.routes_file_name = "simple_rou.xml"
        self.cfg_file_name = "simple.sumocfg"


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

