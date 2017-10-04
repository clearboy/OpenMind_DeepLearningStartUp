#!/usr/bin/python
# -*- coding: UTF-8 -*-

#import numpy as np
import re

filename = "happiness_seg.txt"
filename = "happiness.txt"  # for test

file_object = open(filename,'r',encoding="UTF-8") 

try:
    file_context = file_object.read() # 文件注释
finally:
    file_object.close()

print(file_context)

print(len(file_context))


'''
words = file_context.split() #) # ('，|,|; |\*|\n|\l| ')

for word in words:
    print ('%d:%s' %(len(word),word))

'''

print("==================")
words2 = re.split(r'[： 。 ； ， ： “ ”（ ） 、 ？ 《 》 \s \t]',file_context)

arrayWord = {}
index = 0
for word in words2:
    if len(word)>0:
        if word in arrayWord:
            arrayWord[word] = arrayWord[word] +1
        else:
            arrayWord[word] = 1
        
    print ('%d:%s' %(len(word),word))
    

print(arrayWord)

