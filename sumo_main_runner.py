import os

from Simple_road_sim.simple_sim_main import simple_sim_maker
from Junction_sim.intersection_sim_net_make import split_road_sim_net_make
# Constants:
SIMPLE_SIM = 'simple'
SPLIT_ROAD_SIM = 'split'

if __name__ == '__main__':
    simp_type = SIMPLE_SIM
    if simp_type == SIMPLE_SIM:
        simple_sim_maker(150,0,'E0','E1','J0','J1','13.89',4,10,25,0.25)
    elif simp_type == SPLIT_ROAD_SIM:
        split_road_sim_net_make()