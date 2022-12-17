# -*- coding: utf-8 -*-

"""

Link: 
    https://adventofcode.com/2022/day/6
    
Answer:
    1286
        

"""

import pandas as pd
from collections import Counter
    
data = open('input.txt', 'r').read().rstrip()

marker_start_index = 0

while marker_start_index == 0:
    for i in range(3, len(data)):
        last_four = data[i::-1][0:4]
        if len(Counter(last_four)) == 4:
            marker_start_index = i + 1
            break
        

print(marker_start_index)



"""

Link:
    https://adventofcode.com/2022/day/6#part2
    
Answer:
    3716

"""

# For part 2, the only difference is we are looking for sets of 14 distinct characters instead of 4

data = open('input.txt', 'r').read().rstrip()

marker_start_index = 0

while marker_start_index == 0:
    for i in range(13, len(data)):
        last_four = data[i::-1][0:14]
        if len(Counter(last_four)) == 14:
            marker_start_index = i + 1
            break
        

print(marker_start_index)













