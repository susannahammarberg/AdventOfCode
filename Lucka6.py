# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 15:35:58 2016

@author: HonkyT
"""
                        # clear variable explorer:    %reset
import numpy as np
import collections
s = "bbbaa"
p = collections.Counter(s).most_common(3)[0] #perfekt
print(p)

testData = np.array(['egh','aaa','egh'])
#matrix = np.chararray((3,3))
#for i in range(0,3):
#    matrix[i,:] = list(testData[i])

mostCommon = []

data = np.genfromtxt("dataLucka6.txt",dtype='str')
matrix = np.chararray((572,8))  #skapa en tom char matris
for i in range(0,572):
    matrix[i,:] = list(data[i])

matrixTrans = matrix.conj().T
#saveList = list()
for i in range(0,8):
    print(i)
    rowOne = matrixTrans[i]
    #print(rowOne)
    #mostCommon.append(collections.Counter(rowOne).most_common(2)[1]) #perfekt
    #ej i alfabetisk ordning utan tvärtom
    mostCommon = collections.Counter(rowOne).most_common()
    print(mostCommon)
 
    
 #bjosfbce
 #veqfxzfx
   
    
    
#col=0
#letterIndex = 0
#for letterIndex rande(0,7) #el 8?
#rowIndex = 0
#for row in testData:
#    rad = data[rowIndex]    #välj ut textraden i text-"matrisen"
#    firstLetter = rad[letterIndex] #välj första bokstaven i raden
    # spara bokstaven i en matris
    #tex  a 2
    #     g 4
    #     h 3
#    rowIndex = rowIndex + 1