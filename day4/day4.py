# -*- coding: utf-8 -*-

"""

Link: 
    https://adventofcode.com/2022/day/4
    
Answer:
    584
        

"""

import pandas as pd

data = pd.read_table('input.txt', header = None, names = ['pair'])

# First need to parse these into useable inputs:
#   1) Split the two ranges out (at comma)
#   2) Split each of the two ranges into the start/end points (at dash)
#   3) Convert all four of these into integers 

is_overlapping = []

for i in range(0, len(data)):
    
    overlap = 0
    
    input_string = data['pair'][i]
    
    first_range, second_range = input_string.split(',')
    
    first = first_range.split('-')
    second = second_range.split('-')
    
    first_nums = list(range(int(first[0]), (int(first[1])+1)))
    second_nums = list(range(int(second[0]), (int(second[1])+1)))
    
    num_common = len(set(first_nums) & set(second_nums))
    
    if num_common == min(len(first_nums), len(second_nums)):
        overlap = 1
    
    is_overlapping.append(overlap)
    
sum(is_overlapping)
    


"""

Link: 
    https://adventofcode.com/2022/day/4#part2
    
Answer:
    933

"""

# Now we just want to know how many pairs have ANY overlap at all
# Should be essentially same loop except without checking one list is FULLY contained in the other

is_any_overlap = []

for i in range(0, len(data)):
    
    any_overlap = 0
    
    input_string = data['pair'][i]
    
    first_range, second_range = input_string.split(',')
    
    first = first_range.split('-')
    second = second_range.split('-')
    
    first_nums = list(range(int(first[0]), (int(first[1])+1)))
    second_nums = list(range(int(second[0]), (int(second[1])+1)))
    
    num_common = len(set(first_nums) & set(second_nums))
    
    if num_common > 0:
        any_overlap = 1
    
    is_any_overlap.append(any_overlap)

sum(is_any_overlap)
















