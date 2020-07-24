# -*- coding: utf-8 -*-

"""
Разбираемся, что делает функция zip, и пробуем написать свой собственный zip.
"""

def fb_input():
    global fizz, buzz, n
    fizz = int(input('For Fizz: '))
    buzz = int(input('For Buzz: '))
    n = int(input('Third value: '))
    return 

def fizz_buzz(fizz, buzz, n):
    result = list(map(lambda i: 
                      'FB' if not i % fizz and not i % buzz 
                      else ( 'F' if  not i % fizz 
                      else ( 'B' if  not i % buzz 
                      else i)), 
                      list(range(1, n+1))
                      ))
    return result

def beautysep():
    print('\n---- result ----\n')
    return

def print_zip(n, fb_list):
    zip_dict = dict(zip(list(range(1, n + 1)), fb_list))
    for k,v in zip_dict.items():
        print(k, ' --> ', v)
    return

#===================================
    
fb_input()

beautysep()

result = fizz_buzz(fizz, buzz, n)

print_zip(n, result)