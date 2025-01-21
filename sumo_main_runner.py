import os

from Simple_road_sim.simple_sim_main import simple_sim_maker

# Constants:
SIMPLE_SIM = 'simple'
SPLIT_ROAD_SIM = 'split'

if __name__ == '__main__':
    simp_type = SIMPLE_SIM
    if simp_type == SIMPLE_SIM:
        simple_sim_maker()
    elif simp_type == SPLIT_ROAD_SIM:
        print("DEBUG = split sim")