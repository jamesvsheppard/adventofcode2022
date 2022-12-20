# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 14:27:11 2022

@author: james
"""

"""

PART ONE:
    https://adventofcode.com/2022/day/2
    
ANSWER: 
    9651
    
    
"""

import pandas as pd

plays = pd.read_table('input.txt', header = None, names = ['play'])
plays = plays['play'].str.split(' ')

 
wins = {'A' : 'Y', 'B' : 'Z', 'C' : 'X'}
losses = {'A' : 'Z', 'B' : 'X', 'C' : 'Y'}
draws = {'A' : 'X', 'B' : 'Y', 'C' : 'Z'}
worth = {'X' : 1, 'Y' : 2, 'Z' : 3}

points = 0

for i in range(0, len(plays)):
    
    game = plays[i]
    
    points = points + worth[game[1]]
    
    if game[1] == wins[game[0]]:
        points = points + 6
        continue
    
    if game[1] == draws[game[0]]:
        points = points + 3
        continue
    
    if game[1] == losses[game[0]]:
        continue


"""

PART TWO:
    https://adventofcode.com/2022/day/2#part2
    
ANSWER:
    10560
    
"""

points = 0

for i in range(0, len(plays)):
    
    game = plays[i]
    
    if game[1] == 'X':
        points = points + worth[losses[game[0]]]
        continue
    
    if game[1] == 'Y':
        points = points + 3 + worth[draws[game[0]]]
        continue
    
    if game[1] == 'Z':
        points = points + 6 + worth[wins[game[0]]]
        continue











