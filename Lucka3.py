# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 14:24:06 2016

@author: HonkyT
"""
import numpy as np

#romfile(file[, dtype, count, sep])    #1631 too high(skrev fel!!) 1361 too high 1360 too high
#np.fromfile(dataLucka3[, int])

#x = open('dataLucka3.txt','rb')
countTrue = 0;

n = np.loadtxt("dataLucka3.txt",dtype='int')

#n =np.sort(n)  #uppgift 1 #sortera med avseende på rad

for col in range(0,3):
    for x in range(0,1599,3):
        print(x)
        array = n[x:x+3,col]  
        print(array)
        sortedArray = np.sort(array)
        if (sortedArray[0] + sortedArray[1]) > sortedArray[2]:
            countTrue = countTrue + 1
        print(sortedArray)
        
        
    #sortedMatrix = matris[matris[:,col].argsort()]
    #arr = arr[arr[:,n].argsort()]
    #n[np.argsort(n[x:x+3][col]),col]   #FUNKAR EJ konstiiiiigt
    #print(sortedMatrix)

    
#rad=-1
#for row in n:
#    rad = rad + 1
#    if (n[rad,0] + n[rad,1])  > n[rad,2]:
#        countTrue = countTrue + 1
    