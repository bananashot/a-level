# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 12:22:11 2020

@author: Mega_PC
"""


import sys
filename = sys.argv[0]

f = open(filename, 'r')
r = f.readlines()

r.reverse()

for i in r:
    print(i)
    