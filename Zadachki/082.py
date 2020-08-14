# -*- coding: utf-8 -*-

def armstrong(number):
    number = str(number)
    power = len(number)
    power_list = list(map(int, [i for i in number]))
    for ind, value in enumerate(power_list):
        power_list[ind] = value ** power
    return sum(power_list)

for i in range(1000):
    if i == armstrong(i):
        print(i, '---> ARMSTRONG!')
    