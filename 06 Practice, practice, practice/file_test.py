"""
Цифры до точки с запятой надо суммировать, потом делить на их количество. В первой строке сумма будет 11, разделить на их количество, т.е. на 3, получается 3 целых и в остатке 2. Аналогичным образом во второй строке 6 делим на три, ровно два и в сотатке ноль, в третьей строке сумма 16, на 5 делим, получаем 3 и 1 в остатке.

Задача: проверить каждую строку файла, если строка записана верно, вывести ее и после написать True, если строка не верна, вывести результат с пометкой False.
"""

with open("file-test.txt", 'r') as f:
    lines = f.read().splitlines()
    a = list(range(0, len(lines)))
    dict_read = dict(zip(a, lines))

for k, v in dict_read.items():
    v = v.replace(";", " ; ")
    v = v.split()
    index_value = v.index(";")
    sum_v = sum(list(map(int, v[0:index_value])))
    if sum_v // len(v[0:index_value]) == int(v[index_value+1]) and sum_v % len(v[0:index_value]) == int(v[index_value+2]) :
        print('Sum = ', sum_v, '\n' + lines[k], " --> True")
    else:
        print('Sum = ', sum_v, '\n' + lines[k], " --> False - should be:", 
              sum_v // len(v[0:index_value]), sum_v % len(v[0:index_value]) )