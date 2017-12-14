# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 14:05:05 2017

@author: HonkyT
"""
import numpy as np

#file = np.loadtxt("C:/Users/HonkyT/Documents/adventofcode2017/input2.txt",dtype='int')
#checksum = 0
#for row in file:
#    checksum = checksum + (np.max(row)-np.min(row))


#star2
file = np.loadtxt("C:/Users/HonkyT/Documents/adventofcode2017/input2.txt",dtype='int')
checksum = 0
count=0
for row in file:
    for i in range(0,len(file)):
        for j in range(0,len(file)):
            if np.mod(row[i],row[j])==0 and i!=j:
                checksum = checksum + row[i]/row[j]
                print(row[i])
                print(row[j])
                count+=1
                break
                #checksum = checksum + row[i]



    #print(row[0])