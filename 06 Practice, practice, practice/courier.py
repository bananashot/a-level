"""
Вам известен номер квартиры, этажность дома и количество квартир на этаже. 
Задача: написать функцию, которая по заданным параметрам напишет вам, в какой подъезд и на какой этаж подняться, чтобы найти искомую квартиру.
"""

import random

flats_per_floor = 4

def build_gen():
    global home_prop
    floors = random.randint(2, 10)
    porches = random.randint(2, 5)
    flats = floors * porches * flats_per_floor
    home_prop = [flats, porches, floors]
    return home_prop

def flat_location(flat_num, floors, flats_per_floor):
    if flat_num // floors * flats_per_floor:
        porch = (flat_num // (floors * flats_per_floor))+1
        floor = ((flat_num % (floors * flats_per_floor))//flats_per_floor) +1
        print('\nFloor - ', floor, ' and porch - ', porch,' is what you need!')
    elif not flat_num // floors * flats_per_floor:
        porch = int(flat_num // (floors * flats_per_floor)+1)
        floor = int(flat_num / (floors * flats_per_floor)+1)
        print('\nFloor - ', floor, ' and porch - ', porch, ' is what you need!')
    
newhome = build_gen()

for x in range(0, newhome[2]):
    print('\n')
    for j in range(0, newhome[1]):
        print('*'*flats_per_floor, end = '  |  ')
print('\n')
for i in range(0, newhome[1]):
    print(' 🚪 ', end = '  |  ')
        
disclaimer = '\n\nThere are {} flats in this home with {} porches and {} floors, good luck, courier!'
print(disclaimer.format(*newhome))

rand_flat = random.randint(1, home_prop[0])
print("\nYour today's order is in ", rand_flat, ' flat.' )

flat_location(rand_flat, home_prop[2], flats_per_floor)