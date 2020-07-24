"""
Входным данным является целое число. Необходимо:

    написать проверку, чтобы в работу пускать только положительные нечетные числа
    для правильного числа нужно построить бриллиант из звездочек или любых других символов и вывести его в консоли. Для числа 1 он выглядит как одна взездочка, для числа три он выглядит как звезда, потом три звезды, потом опять одна, для пятерки - звезда, три, пять, три, одна...
"""

import random

max_star = 20

def nech_random():
    while True:
        n = random.randint(3, max_star)
        if n%2:
            return n
        
        
number = nech_random()

spaces = number//2
additive = 1

for i in range(0, number//2):
    print(' '*spaces + '*'*additive)
    spaces -= 1
    additive += 2

print('*'*number)

for i in range(0, number//2):
    spaces += 1
    additive -= 2
    print(' '*spaces + '*'*additive)