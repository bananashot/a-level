n = int(input('Amount of money: '))
pages = [1000, 500, 200, 100, 50, 20, 10, 5]

while n >= 5:
    for i in pages:
        if n // i:
            print( n // i, ' x ', i)
            n %= i
        else:
            pass
    
print('Extra: ', n)
        