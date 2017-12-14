# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 11:49:01 2017

@author: HonkyT
"""
import numpy as np
#star1
#file1=open("C:/Users/HonkyT/Documents/adventofcode2017/input1.txt",'r').read()
#file1=file1[0:-1]
#suma=0
#for i in range(0,len(file1)-2):
#    if file1[i] == file1[i+1]:
#        print(file1[i])
#        suma = suma + int(file1[i])
#        
#                            
##special case for last digit matches the first
#if file1[0] == file1[-1]:
#    suma = suma + int(file1[-1])
#    print(file1[0])

#star2
file1=open("C:/Users/HonkyT/Documents/adventofcode2017/input1.txt",'r').read()
file1=file1[0:-1]

#file1 = '1111111111'
ss=int(len(file1)/2)
suma=0 
for i in range(0,ss):
    if file1[i] == file1[i+ss]:
        print(file1[i])
        print(file1[i+ss])
        suma = suma + int(file1[i])
        
suma=suma*2                        
#special case for last digit matches the first

#Ans:suma=1146
                        
                        
                        