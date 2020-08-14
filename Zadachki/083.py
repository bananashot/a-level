# -*- coding: utf-8 -*-
from random import shuffle
import string


alphabet = list(string.ascii_lowercase)
shuffle(alphabet)
beaty_values = list(range(1, 27))
beaty_dict = dict(zip(alphabet, beaty_values))


with open('Beautiful Strings.txt', 'r') as f:
    file = f.read().split('\n')
    for i, v in enumerate(file):
        file[i] = v.lower()
    for line in file:
        letter_sum = 0
        for letter in list(line):
            if letter in beaty_dict.keys():
                letter_sum += beaty_dict[letter]
                print(letter + ' = ' + str(beaty_dict[letter]), end = ' | ')
        print('\n' + line, '-->', letter_sum, '\n')
