#---Written by Michael Popov and Yuval Marsh---

# Imports
from Simple_road_sim.simple_sim_main import simple_sim_maker
from Junction_sim.junction_sim_main import split_sim_maker
from Junction_sim.junction_sim_main import half_junction_maker
import os
# Constants:
# These are the specifiers for the desires simulation place the on you want in the 'sim_type' variable:
SIMPLE_SIM = 'simple'
SPLIT_ROAD_SIM = 'split'
HALF_JUNC_SIM = 'half_junction'
# Folder names:
SUMO_SIM_FILES_FOLDER = "Sumo sim files"
SIMPLE_SIM_FOLDER = 'Simple road'
INTERSECTION_SIM_FOLDER = 'Intersection road'
GO_ONE_FOLDER_BACK = '..'

# This class contains the simple sim parameters adjust it so it fits your need:
class SimpleSimParams:
    def __init__(self):
        self.road_length = 70
        self.angle = 0
        self.edge_0 = 'E0'
        self.edge_1 = 'E1'
        self.junc_0 = 'J0'
        self.junc_1 = 'J1'
        self.speed = '13.89'
        self.lanes_num = 5
        self.lr_cars = 10
        self.rl_cars = 15
        self.interval_cars = 0.00

# This code runs the file generation and place them in the correct folder:
if __name__ == '__main__':
    sim_type = HALF_JUNC_SIM
    if not os.path.isdir(SUMO_SIM_FILES_FOLDER):
        os.mkdir(SUMO_SIM_FILES_FOLDER)
    os.chdir(SUMO_SIM_FILES_FOLDER)
    if sim_type == SIMPLE_SIM:
        if not os.path.isdir(SIMPLE_SIM_FOLDER):
            os.mkdir(SIMPLE_SIM_FOLDER)
        os.chdir(SIMPLE_SIM_FOLDER)
        simple_params = SimpleSimParams()
        simple_sim_maker(simple_params.road_length, simple_params.angle,
                         simple_params.edge_0, simple_params.edge_1,
                         simple_params.junc_0, simple_params.junc_1,
                         simple_params.speed, simple_params.lanes_num,
                         simple_params.lr_cars, simple_params.rl_cars,
                         simple_params.interval_cars)
        os.chdir(GO_ONE_FOLDER_BACK)
    elif sim_type == SPLIT_ROAD_SIM:
        if not os.path.isdir(INTERSECTION_SIM_FOLDER):
            os.mkdir(INTERSECTION_SIM_FOLDER)
        os.chdir(INTERSECTION_SIM_FOLDER)
        split_sim_maker()
        os.chdir(GO_ONE_FOLDER_BACK)
    elif sim_type == HALF_JUNC_SIM:
        if not os.path.isdir(INTERSECTION_SIM_FOLDER):
            os.mkdir(INTERSECTION_SIM_FOLDER)
        os.chdir(INTERSECTION_SIM_FOLDER)
        half_junction_maker()
        os.chdir(GO_ONE_FOLDER_BACK)
    os.chdir(GO_ONE_FOLDER_BACK)