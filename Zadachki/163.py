# -*- coding: utf-8 -*-
zero = ['-**--', '*--*-', '*--*-', '*--*-', '-**--', '-----']
one = ['--*--', '-**--', '--*--', '--*--', '-***-', '-----']
two = ['***--', '---*-', '-**--', '*----', '****-', '-----']
three  = ['-*---', '*--*-', '****-', '---*-', '---*-', '-----']
four = ['***--', '---*-', '-**--', '---*-', '***--', '-----']
five = ['****-', '*----', '***--', '---*-', '***--', '-----']
six = ['-**--', '*----', '***--', '*--*-', '-**--', '-----']
seven = ['****-', '---*-', '--*--', '-*---', '-*---', '-----']
eight = ['-**--', '*--*-', '-**--', '*--*-', '-**--', '-----']
nine = ['-**--', '*--*-', '-***-', '---*-', '-**--', '-----']

column_range = list(range(7))

dict0 = dict(zip(column_range, zero))
dict1 = dict(zip(column_range, one))
dict2 = dict(zip(column_range, two))
dict3 = dict(zip(column_range, three))
dict4 = dict(zip(column_range, four))
dict5 = dict(zip(column_range, five))
dict6 = dict(zip(column_range, six))
dict7 = dict(zip(column_range, seven))
dict8 = dict(zip(column_range, eight))
dict9 = dict(zip(column_range, nine))

dict_list = [dict0, dict1, dict2, dict3, dict4, dict5, dict6, dict7, dict8, dict9]

def numbers(integer):
    print_list = []
    for i in list(integer):
        if i.isdigit():
              print_list.append(dict_list[int(i)])
    return print_list

with open('Big Digits.txt', 'r') as f:
    file = f.read().split('\n')
    print(file)
    
for number in file:
    for j in numbers(number):
        for i in range(6):
            print(j[i])
            