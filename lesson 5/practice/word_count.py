# -*- coding: utf-8 -*-
"""
Вспоминаем работу с файлом. Есть файл, в котором много англоязычных текстовых строк. Считаем частоту встретившихся слов в файле, но через функции и map, без единого цикла!
"""

import functools

def file_proc(filename):
    with open (filename) as f:
        newlist = list(map(lambda x: x.split(), f.readlines()))
        newlist = functools.reduce(lambda x,y: x + y, newlist)
        newlist = list(map(lambda x: x.lower(), newlist))
        newlist = list(map(lambda x: x.replace('.', ''), newlist))
        return newlist

        
def count_words(words):
    unique_words = {x: words.count(x) for x in words}
    return unique_words
    
result = count_words(file_proc('text.txt'))
    
for k,v in result.items():
    print(k, ' -> ', v )