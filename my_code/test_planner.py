from planner import my_link_search
from time import sleep
import numpy as np

import sys
sys.path.append('../auto_grader')
import auto_grader

sys.path.append("./planner/")
from sa import simulated_annealing

ag = auto_grader.auto_grader()

raw_map = ag.get_map()
colour_map = np.reshape(np.array(raw_map)[:, 0], (8, 8))
num_map = np.reshape(np.array(raw_map)[:, 1], (8, 8))
map_ = num_map + colour_map * 10 + 1
map_ = np.pad(map_,((1,1),(1,1)),'constant',constant_values = (0,0)) 

print(map_)
sco, path = simulated_annealing(map_, )

for l in path:
    ag.link(*l)

sleep(1e5)