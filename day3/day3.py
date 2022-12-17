# -*- coding: utf-8 -*-

"""

Link: 
    https://adventofcode.com/2022/day/3
    
Answer:
    8139
        

"""

import pandas as pd

items = pd.read_table('input.txt', header = None, names = ['items'])

# setting up reference key for 'priority' of each character
alphabet = 'abcdefghijklmnopqrstuvwxyz' + 'abcdefghijklmnopqrstuvwxyz'.upper()

letters = [x for x in alphabet]
priority = [x for x in range(1, 53)]

key = dict(zip(letters, priority))

# looping through list of strings and recording common character

common_char = []
points = []

for i in range(0, len(items)):
    
    pack = items['items'][i]
    
    mid = int(len(pack)/2)
    
    common = list( set( pack[0:mid]) & set(pack[mid: ]) )

    common_char.append(common[0])
    points.append(key[common[0]])
    
inventory = pd.DataFrame({'items' : items['items'],
              'common_character' : common_char,
              'points' : points})
    
inventory['points'].sum()

"""

Link: 
    https://adventofcode.com/2022/day/3#part2
    
Answer:
    2668

"""

# pull groups of three packs
# find common letter in those three using set() 

badges = []
badge_points = []

len(items['items'])

for i in range(2, 300, 3):
    packs = [ items['items'][i],
                  items['items'][i-1],
                  items['items'][i-2] ]
    
    badge = list ( set(packs[0]) & set(packs[1]) & set(packs[2]) )
    
    badges.append(badge[0])
    badge_points.append(key[badge[0]])
    
badge_inventory = pd.DataFrame({'badge' : badges,
                                'badge_priority_points' : badge_points})

badge_inventory['badge_priority_points'].sum()
