#---Written by Michael Popov and Yuval Marsh---

# Imports
from Simple_road_sim.simple_sim_main import simple_sim_maker
from Junction_sim.junction_sim_main import split_sim_maker
from Junction_sim.junction_sim_main import half_junction_maker
import os
# Constants:
SIMPLE_SIM = 'simple'
SPLIT_ROAD_SIM = 'split'
HALF_JUNC_SIM = 'half_junction'
# Folder names:
SUMO_SIM_FILES_FOLDER = "Sumo sim files"
SIMPLE_SIM_FOLDER = 'Simple road'
INTERSECTION_SIM_FOLDER = 'Intersection road'
GO_ONE_FOLDER_BACK = '..'

if __name__ == '__main__':
    sim_type = HALF_JUNC_SIM
    if not os.path.isdir(SUMO_SIM_FILES_FOLDER):
        os.mkdir(SUMO_SIM_FILES_FOLDER)
    os.chdir(SUMO_SIM_FILES_FOLDER)
    if sim_type == SIMPLE_SIM:
        if not os.path.isdir(SIMPLE_SIM_FOLDER):
            os.mkdir(SIMPLE_SIM_FOLDER)
        os.chdir(SIMPLE_SIM_FOLDER)
        simple_sim_maker(70,0,'E0','E1','J0','J1','13.89',
                         5,10,25,0.25)
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