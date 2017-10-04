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

#print(file_context)

print("="*80)
print("-"*20)

print("File length:%d"%len(file_context))


'''
words = file_context.split() #) # ('，|,|; |\*|\n|\l| ')

for word in words:
    print ('%d:%s' %(len(word),word))

'''

print("-"*20)
words2 = re.split(r'[： 。 ； ， ： “ ”（ ） 、 ？ 《 》 \s \t]',file_context)

arrayWord = {}
index = 0
indexWords ={}
for word in words2:
    if len(word)>0:
        if word in arrayWord:
            arrayWord[word] = arrayWord[word] +1
        else:
            arrayWord[word] = 1
        if not word in indexWords:
            indexWords[word] =  index
            index = index + 1

wordCount = index
# print(arrayWord)

print(indexWords)

print("-"*20)
print("Total words: %d"%wordCount)


## create the array

#np.zeros(wordCount,wordCount)

#for word in words2:
# for iWord, word in enumerate(words2):
for i in range(len(words2)-1):
    if len(words2[i])<1 or len(words2[i+1])<1:
        continue
    print("%s-%s"%(words2[i],words2[i+1]))
    #iRow = indexWords[words2[i]]
    #iCol = indexWords[words2[i+1]] #   np(iRow,iCol) = np(iRow,iCol) + 1
    #print ("(%d,%d)"%(iRow,iCol))

 

