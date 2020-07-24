# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 00:06:15 2020

@author: Mega_PC
"""


fizz = int(input('For Fuzz: '))
buzz = int(input('For Buzz: '))
n = int(input('Third value: '))

print('\n---- result ----\n')

for i in range(1,n+1):
    if not i % fizz and not i % buzz: 
        print('FB')
    elif  not i % fizz:
        print('F')
    elif  not i % buzz:
        print('B')
    else:
        print(i)
