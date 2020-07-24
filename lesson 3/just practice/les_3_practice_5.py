
amount = int(input('Amount of money: '))
pages = [1000, 500, 200, 100]
small_pages = [50, 20, 10, 5]
count_operations = []

print('Report:')

while True:
    if amount > 854:
        for i in pages:
            if amount - i > 754:
                amount -= i
                count_operations.append(i)
    else:
        break


for i in range(0, 10):
    for j in small_pages:
        if amount - j >= 0:
            amount -= j
            count_operations.append(j)
            
        
for big_num in pages:
    print(count_operations.count(big_num), ' x ', big_num)        
        
for small_num in small_pages:
    print(count_operations.count(small_num), ' x ', small_num)


print('\nExtra: ', amount)