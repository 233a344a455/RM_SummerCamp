from planner import my_link_search
from time import sleep
import numpy as np

import sys
sys.path.append('../auto_grader')
import auto_grader

ag = auto_grader.auto_grader()

raw_map = ag.get_map()
colour_map = np.reshape(np.array(raw_map)[:, 0], (8, 8))
num_map = np.reshape(np.array(raw_map)[:, 1], (8, 8))
# print(num_map, colour_map)
map_ = num_map + colour_map * 10 + 1

print(map_)
ls = my_link_search.MyLinkSearch(map_, ag)

# sleep(1e5)
# while ls.map.any():
for x in range(1, 10):
    for y in range(1, 10):
        num = ls.map[x, y]
        if num == 0:
            continue
        
        max_sco, maxidx = -1, None
        for p2 in np.argwhere(ls.map == num):
            s = ls.search_link(x, y, *p2)
            if s is not None:
                if s > max_sco:
                    max_sco, maxidx = s, p2

        if maxidx is not None:
            # score += max_sco
            try:
                ls.link(x, y, *maxidx)
            except Exception:
                sleep(1e5)
            print(ls.map)
            # sleep(1)
            continue

sleep(1e5)