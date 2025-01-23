#---Written by Michael Popov and Yuval Marsh---

from Simple_road_sim.simple_sim_main import simple_sim_maker
from Junction_sim.junction_sim_main import split_sim_maker
# Constants:
SIMPLE_SIM = 'simple'
SPLIT_ROAD_SIM = 'split'

if __name__ == '__main__':
    simp_type = SPLIT_ROAD_SIM
    if simp_type == SIMPLE_SIM:
        simple_sim_maker(150,0,'E0','E1','J0','J1','13.89',4,10,25,0.25)
    elif simp_type == SPLIT_ROAD_SIM:
        split_sim_maker()