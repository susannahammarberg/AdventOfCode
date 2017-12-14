# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 12:21:21 2017

@author: Sanna


"""
import numpy as np
##STAR 1
#steps = 0
#position = 0 
#file1 = np.loadtxt('C:/Users/Sanna/Documents/adventofcode2017/input5.txt',dtype='int') #like a list. you can use indices
##file1=open('C:/Users/Sanna/Documents/adventofcode2017/input5.txt','r')#.read()
#
##file1 = [0, 3, 0, 1, -3]
#print(file1)
#index = 0 #index of file1
##while position <6 and position >=0: 
##while
#while position < len(file1):
#    # update index  (this index is one jump behind 'position')
#    index = position
#    #jump n nbr of steps
#    position += file1[index] 
#    # update jumping vector
#    file1[index] +=1
##    ind_file1 +=file1[position]
#    steps+=1
#
#print(file1)
#print(steps)
# star2

steps = 0
position = 0 
file1 = np.loadtxt('C:/Users/Sanna/Documents/adventofcode2017/input5.txt',dtype='int') #like a list. you can use indices
#file1=open('C:/Users/Sanna/Documents/adventofcode2017/input5.txt','r')#.read()

file1 = [0, 3, 0, 1, -3]
print(file1)
index = 0 #index of file1
#while position <6 and position >=0: 
#while
while position < len(file1):
    # update index  (this index is one jump behind 'position')
    index = position
    #jump n nbr of steps
    position += file1[index] 
    # update jumping vector
    if file1[index] >= 3:
        file1[index] -=1
    else:
        file1[index] +=1            
    steps+=1

print(file1)
print(steps)