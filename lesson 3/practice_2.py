# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 10:49:44 2020

@author: Mega_PC
"""

# randomizer for a file with 20 lines:

import random

lines_count = 20
filename = open('random_3.txt', 'w+')
random_lim = 50
temp_sort = []

while lines_count:
    
    temp_sort.clear()
    
    for n in range(0, 3):
        temp_sort.append(random.randint(2,random_lim)) # когда рандомайзит 1 - то не интересно, так что от 2х
        
    temp_sort.sort()
        
    for i in temp_sort:
        filename.write(str(i) + ' ')
        
    filename.write('\n')
    lines_count -= 1
    
for line in filename.readlines():
    line.rstrip()

filename.close()

# task:

filename = open('random_3.txt', 'r')

j = filename.readlines()
x = j[0].split()
fizz = int(x[0])
buzz = int(x[1])
n = int(x[2])

intro = 'Fizz - {} | Buzz - {} | 3rd value - {}:'
print(intro.format(fizz, buzz, n))

for i in range(1,n+1):
    if not i % fizz and not i % buzz: 
        print('FB')
    elif  not i % fizz:
        print('F')
    elif  not i % buzz:
        print('B')
    else:
        print(i)

filename.close()