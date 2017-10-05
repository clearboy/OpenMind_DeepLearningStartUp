#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import re

iDebug = 4   # level of debug

filename = "happiness_seg.txt"
filename = "happiness.txt"  # for test

## load file
print("-"*20)
print("Loading file...")

file_object = open(filename,'r',encoding="UTF-8") 

try:
    file_context = file_object.read() # 文件注释
finally:
    file_object.close()

#print(file_context)

print("="*80)
print("-"*20)

print("File length:%d"%len(file_context))


## split input to wordsSplited
print("-"*40)
print("split input to wordsSplited...")

textSplit = re.split(r'[： 。 ； ， ： “ ”（ ） 、 ？ 《 》 \s \t,.-]*',file_context)
textLen = len(textSplit)
if iDebug>3:
    print("text splited:")
    print(textSplit)

print("-"*40)
print("Total wordsSplited: %d"%textLen)

wordsIndex = {}

N = 0
for word in textSplit:
    if len(word)>0:
        if not word in wordsIndex:
            wordsIndex[word]=N
            N = N+1

print("Total words: %d"%N)

if iDebug>3:
    print("words index:")
    print(wordsIndex)

## create the array
print("-"*40)
print("Create the array...")


arrayCounts = np.zeros((N,N))
listTopWords= []


# for word in textSplit:
# for iWord, word in enumerate(textSplit):
for i in range(textLen-1):
    wordCurrent = textSplit[i]
    wordNext = textSplit[i+1]

    # skip if the word is empty
    if len(wordCurrent)<1 or len(wordNext)<1:
        continue

    # update the matrix
    iRow = wordsIndex[wordCurrent]
    iCol = wordsIndex[wordNext] 
    newValue = arrayCounts[iRow,iCol] + 1
    arrayCounts[iRow,iCol] = newValue
    if iDebug>2:
        print ("(%8d,%8d)=%4d:%s %s"%(iRow,iCol,arrayCounts[iRow,iCol],wordCurrent,wordNext))

    if (len(listTopWords)<10) and  (not [iRow,iCol] in listTopWords):
        listTopWords.append([iRow,iCol])
    else:
        # find and remove the minual in top list
        iIndexMin = listTopWords[0]
        listMinvalue = arrayCounts[iIndexMin[0],iIndexMin[1]]    
        for iIndex in listTopWords:
            if arrayCounts[iIndex[0],iIndex[1]] < listMinvalue:
                print("my:%d,%d=%d"%(iIndex[0],iIndex[1],arrayCounts[iIndex[0],iIndex[1]]))
                iIndexMin = iIndex
                listMinvalue = arrayCounts[iIndex]
        if iDebug>3:
            print("the minum index is")
            print(listMinvalue)
            a = wordsIndex.keys()
            print(len(a))
            #str = a[iIndexMin[0]]
            print("(%d,%d)=%d:"%(iIndexMin[0],iIndexMin[1],arrayCounts[iIndexMin[0],iIndexMin[1]]))
            print(str)
#            print("%s %s"%(wordsIndex[iIndexMin[0]]，wordsIndex[iIndexMin[1]]))
        if newValue > listMinvalue:
            listTopWords.remove(iIndexMin)
            listTopWords.append([iRow,iCol])
        print(listTopWords)


'''
    # update the top word list
    # iTopList = N*iRow+iCol
    iTopList = [iRow,iCol]
    if not (iTopList in listTopWords):
        if (len(listTopWords)<10):
            listTopWords.append(iTopList)
        else:
            if newValue > listMinvalue:
                print(listTopWords)
                listTopWords.remove(listIndex)
                listTopWords.append(iTopList)
                print(listTopWords)
    if newValue > listMinvalue:
        print("%d-->%d"%(listMinvalue,newValue))
        listMinvalue = newValue
        listIndex = iTopList
'''

print("-"*20)
print(listTopWords)
for iIndex in listTopWords:
    print(iIndex)
    print(arrayCounts[iIndex[0],iIndex[1]])

print(arrayCounts)
print(np.size(arrayCounts))
print(np.max(arrayCounts))
# print("sum:%d"%totalCount)

