<<<<<<< HEAD

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 15:00:26 2017

@author: Sanna
"""
import numpy as np
import matplotlib  as plt
bank = np.loadtxt('C:/Users/Sanna/Documents/Github/adventofcode/2017/input6.txt',dtype='int') 
#bank = np.loadtxt('C:/Users/Sanna/Documents/adventofcode2017/input6.txt',dtype='int') 

def solve(permutation_set,permutation,bank):

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

    print(len(permutation_set))
    return permutation,permutation_set

permutation_set = set()
permutation = tuple(bank)
xx, xxset= solve(permutation_set,permutation,bank)
#part2 : 
permutation_set = set()
bank2= np.array((0, 14, 13, 12, 11, 10, 8, 8, 6, 6, 5, 3, 3, 2, 1, 10))
permutation2 = tuple(bank2)
x2, x2set = solve( permutation_set,permutation2,bank2)
answer=len(x2set)  #right answer


# This gives the wrong answer, why?!
#1360
#1359
#1358


#1371
#1370
#1372
index=0
print('xx is')
print(xx)
for perm in xxset:
    #print(perm)
    if perm==xx:
        print('index:')
        print(index)
        print(len(xxset)-index)
        print(perm)

    index+=1

=======

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 15:00:26 2017

@author: Sanna
"""
import numpy as np
import matplotlib  as plt
bank = np.loadtxt('C:/Users/Sanna/Documents/Github/adventofcode/2017/input6.txt',dtype='int') 
#bank = np.loadtxt('C:/Users/Sanna/Documents/adventofcode2017/input6.txt',dtype='int') 

def solve(permutation_set,permutation,bank):

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

    print(len(permutation_set))
    return permutation,permutation_set

permutation_set = set()
permutation = tuple(bank)
xx, xxset= solve(permutation_set,permutation,bank)
#part2 : 
permutation_set = set()
bank2= np.array((0, 14, 13, 12, 11, 10, 8, 8, 6, 6, 5, 3, 3, 2, 1, 10))
permutation2 = tuple(bank2)
x2, x2set = solve( permutation_set,permutation2,bank2)
answer=len(x2set)  #right answer


# This gives the wrong answer, why?!
#1360
#1359
#1358


#1371
#1370
#1372
index=0
print('xx is')
print(xx)
for perm in xxset:
    #print(perm)
    if perm==xx:
        print('index:')
        print(index)
        print(len(xxset)-index)
        print(perm)

    index+=1

>>>>>>> 753024674118819cd7079b0605d7d83fe5722123
#print(xx)len()