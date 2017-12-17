# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 15:00:26 2017

@author: Sanna
"""
import numpy as np
bank = np.loadtxt('C:/Users/HonkyT/Documents/AdventOfCode-master/2017/input6.txt',dtype='int')
#bank = np.loadtxt('C:/Users/Sanna/Documents/adventofcode2017/input6.txt',dtype='int') 

def solve(permutation_set,permutation,bank):
    counter=0    
    while permutation not in permutation_set:
        #print('Newmaxima')
        #print(max(bank))
        j=np.argmax(bank)
        steps=max(bank)
        bank[j]=0
        for i in range(steps):        
            j+=1        
            # if you reach the last bank, start om from the beginning
            if j > len(bank)-1:
                j-=len(bank)
                #print('j')
            bank[j]+=1
    
        #print('this is what a append:')
        #print((bank))
        permutation_set.add(permutation)
        permutation = tuple(bank)
        counter+=1
    print(counter)
    return permutation,permutation_set

permutation_set = set()
permutation = tuple(bank)
xx, xxset= solve(permutation_set,permutation,bank)
#1360
#1359
#1358
index=0
for perm in xxset:
    if perm==xx:
        print(index)
        print(perm)

    index+=1
print(xx)
#print(xx)

