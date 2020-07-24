import random

def nech_random():
    while True:
        n = random.randint(3, 20)
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