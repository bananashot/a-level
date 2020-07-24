# -*- coding: utf-8 -*-

"""
Продолжаем идеализировать fizzbuzz, теперь применяем функции и map везде, где можно и нельзя!
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

def printmap(fb_list):
    printing_list = list(map(lambda x: print(x), fb_list))
    return

#===================================
    
fb_input()

beautysep()

result = fizz_buzz(fizz, buzz, n)

printmap(result)