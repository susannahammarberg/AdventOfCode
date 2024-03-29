# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 10:49:12 2023

@author: sanna
"""

import re #in oder to use split with several delimeters
import numpy as np

def read_input():
    
    with open('input5.txt','r') as fp:
        info = fp.read().splitlines()
        #info = f.readlines()
    return info

def read_test():    
    test_data = [
    """
    0,9 -> 5,9
    8,0 -> 0,8
    9,4 -> 3,4
    2,2 -> 2,1
    7,0 -> 7,4
    6,4 -> 2,0
    0,9 -> 2,9
    3,4 -> 1,4
    0,0 -> 8,8
    5,5 -> 8,2
    """]
    test_data = test_data[0].split('\n') # same as splitlines
    return test_data[1:-1]

data = read_input()
#data = read_test()

array = np.zeros((1000,1000),dtype=int)
def part1():
    
    for line in data:
        a = re.split(',|->' , line.strip(' '))
        

        xvalues = sorted([int(a[0]),int(a[2])])
        yvalues = sorted([int(a[1]),int(a[3])])
        
        if yvalues[0] == yvalues[1]:
        
            for xpos in range(xvalues[0],xvalues[1]+1):
                array[ yvalues[0], xpos] += 1

        elif xvalues[0] == xvalues[1]:
            for ypos in range(yvalues[0],yvalues[1]+1):
                array[ ypos, xvalues[0]] += 1
                
 
        
part1()

" calc numer of indices with more than one hit"

array[array == 1] = 0
array[array > 1] = 1
answ = np.sum(array)

print('\n' + 'result part 1: ', answ )

array = np.zeros((1000,1000),dtype=int)
def part2():
    
    for line in data:
        a = re.split(',|->' , line.strip(' '))
        

        xvalues = sorted([int(a[0]),int(a[2])])
        yvalues = sorted([int(a[1]),int(a[3])])
        
        if yvalues[0] == yvalues[1]:
        
            for xpos in range(xvalues[0],xvalues[1]+1):
                array[ yvalues[0], xpos] += 1

        elif xvalues[0] == xvalues[1]:
            for ypos in range(yvalues[0],yvalues[1]+1):
                array[ ypos, xvalues[0]] += 1
                

        else:
           #print('diagonal lines', line)
           #todo # recoding this part now so could clean up
           x1 = int(a[0]); x2 = int(a[2])
           y1 = int(a[1]); y2 = int(a[3])
           if x1 < x2:
                xvalues_unsorted = list(range(x1,x2+1))
           else:
                xvalues_unsorted = list(range(x1,x2-1,-1))
           if y1 < y2:
                yvalues_unsorted = list(range(y1,y2+1))
           else:
                yvalues_unsorted = list(range(y1,y2-1,-1))        
           j = 0
           for xpos in xvalues_unsorted:
               array[ yvalues_unsorted[j], xpos] += 1
               
               #print(yvalues_unsorted[j], xpos)
               j+=1
        
part2()

array[array == 1] = 0
array[array > 1] = 1
answ = np.sum(array)   
print('\n' + 'result part 2: ', answ )

