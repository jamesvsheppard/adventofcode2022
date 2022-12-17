# -*- coding: utf-8 -*-

"""

Link: 
    https://adventofcode.com/2022/day/5
    
Answer:
    LJSVLTWQM
        

"""

import pandas as pd

data = open('input.txt').readlines()
data = data[10:]

# this sucks but i'm just going to manually define the nine stacks as lists

s1 = ['S', 'M', 'R', 'N', 'W', 'J', 'V', 'T']
s2 = ['B', 'W', 'D', 'J', 'Q', 'P', 'C', 'V']
s3 = ['B', 'J', 'F', 'H', 'D', 'R', 'P']
s4 = ['F', 'R', 'P', 'B', 'M', 'N', 'D']
s5 = ['H', 'V', 'R', 'P', 'T', 'B']
s6 = ['C', 'B', 'P', 'T']
s7 = ['B', 'J', 'R', 'P', 'L']
s8 = ['N', 'C', 'S', 'L', 'T', 'Z', 'B', 'W']
s9 = ['L', 'S', 'G']

stack_list = ['placeholder', s1, s2, s3, s4, s5, s6, s7, s8, s9]

for i in range(0, len(data)):
    
    dir_parts = data[i].split(' ')
    
    num_moves = int(dir_parts[1])
    from_stack = int(dir_parts[3])
    to_stack = int(dir_parts[5][:-1])
    
    for j in range(0, num_moves):
        moving = stack_list[from_stack].pop()
        stack_list[to_stack].append(moving)
    
# Now we just need the 'top' item on each stack

top_items = ''

for i in range(1, 10):
    top_items = top_items + (stack_list[i][-1])

print(top_items)


"""

Link: 
    https://adventofcode.com/2022/day/5#part2
    
Answer:
    BRQWDBBJM
    

"""

# For part 2, the only difference is the crane picks up all the crates at once
# Can just tweak the loop to pop off num_moves instead of one item at a time

s1 = ['S', 'M', 'R', 'N', 'W', 'J', 'V', 'T']
s2 = ['B', 'W', 'D', 'J', 'Q', 'P', 'C', 'V']
s3 = ['B', 'J', 'F', 'H', 'D', 'R', 'P']
s4 = ['F', 'R', 'P', 'B', 'M', 'N', 'D']
s5 = ['H', 'V', 'R', 'P', 'T', 'B']
s6 = ['C', 'B', 'P', 'T']
s7 = ['B', 'J', 'R', 'P', 'L']
s8 = ['N', 'C', 'S', 'L', 'T', 'Z', 'B', 'W']
s9 = ['L', 'S', 'G']

stack_list = ['placeholder', s1, s2, s3, s4, s5, s6, s7, s8, s9]

for i in range(0, len(data)):
    
    dir_parts = data[i].split(' ')
    
    num_moves = int(dir_parts[1])
    from_stack = int(dir_parts[3])
    to_stack = int(dir_parts[5][:-1])

    temp_list = []
    
    for j in range(0, num_moves):
        temp_list.append(stack_list[from_stack].pop())
    
    for k in range(0, num_moves):
        stack_list[to_stack].append(temp_list.pop())
    
# Now we just need the 'top' item on each stack

top_items = ''

for i in range(1, 10):
    top_items = top_items + (stack_list[i][-1])

print(top_items)













