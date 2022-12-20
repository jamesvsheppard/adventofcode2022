# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 13:22:06 2022

@author: james
"""

"""

PART ONE:
    https://adventofcode.com/2022/day/1
    
ANSWER:
    72602
    
"""

import pandas as pd

with open('input.txt') as f:
    
    lines = pd.Series(f.readlines())

df = pd.DataFrame(columns = ['cals'])
calcount = 0 

for i in range(0, len(lines)):

    if lines[i] == '\n':
        df = df.append({'cals':calcount}, ignore_index = True)
        calcount = 0
        continue
    calcount += int(lines[i])

df.sort_values('cals', ascending = False)


"""

PART TWO:
    https://adventofcode.com/2022/day/1#part2
    
ANSWER:
    207410
    
"""

df.sort_values('cals', ascending = False).iloc[0:3].sum()
