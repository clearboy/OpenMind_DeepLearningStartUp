#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import re

iDebug = 2   # level of debug

filename = "happiness_seg.txt"
if iDebug>3:
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

textSplit = re.split(r'[： 。 ； ， ： “ ”（ ） 、 ？ 《 》 \s \t,.-―]*',file_context)
textLen = len(textSplit)
if iDebug>3:
    print("text splited:")
    print(textSplit)

print("-"*40)
print("Total wordsSplited: %d"%textLen)

wordsArray =[]
N = 0
for word in textSplit:
    if len(word)>0:
        if not word in wordsArray:
            wordsArray.append(word)
            N = N+1

print("Total words: %d"%N)

if iDebug>3:
    print("words array:")
    print(wordsArray)

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
    iRow = wordsArray.index(wordCurrent)
    iCol = wordsArray.index(wordNext)
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
            iValue = arrayCounts[iIndex[0],iIndex[1]]
            if  iValue < listMinvalue:
                #print("my:%d,%d=%d"%(iIndex[0],iIndex[1],arrayCounts[iIndex[0],iIndex[1]]))
                iIndexMin = iIndex
                listMinvalue = iValue
        if iDebug>3:
            print("the minum index is")
            print(listMinvalue)
            print("(%d,%d)=%d:%s %s"%(iIndexMin[0],iIndexMin[1],arrayCounts[iIndexMin[0],iIndexMin[1]],wordsArray[iIndexMin[0]],wordsArray[iIndexMin[1]]))
        if (newValue > listMinvalue) and (not [iRow,iCol] in listTopWords):
            listTopWords.remove(iIndexMin)
            listTopWords.append([iRow,iCol])
            if iDebug>3:
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

totalCount = np.sum(arrayCounts)

print("-"*20)
print("Final top words:")

for iIndex in listTopWords:
    cnt = arrayCounts[iIndex[0],iIndex[1]]
    print("%s %s\t:%.2f%%(%d of %d)"%(wordsArray[iIndex[0]],wordsArray[iIndex[1]],100*cnt/totalCount,cnt,totalCount))

if iDebug>3:
    print(arrayCounts)
    print(np.max(arrayCounts))
    print(listTopWords)
    for iIndex in listTopWords:
        print("(%d,%d)=%d/%d:%s %s"%(iIndex[0],iIndex[1],arrayCounts[iIndex[0],iIndex[1]],totalCount,wordsArray[iIndex[0]],wordsArray[iIndex[1]]))

# print("sum:%d"%totalCount)

