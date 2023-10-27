# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 10:49:12 2023

@author: sanna
"""


def read_input():
    
    with open('input7.txt','r') as fp:
        info = fp.read().split(',')
        info  = [int(item) for item in info]
        #info = fp.read().splitlines()
        #info = f.readlines()
    return info

def read_test():    
    test_data = [16,1,2,0,4,2,7,1,2,14]
    #test_data = test_data[0].split('\n') # same as splitlines
    return test_data

data = read_input()
#data = read_test()
data = [int(dat) for dat in data] # turn the items to ints
#
# part 1


def align_crabs():
    fuels = []
    for ii in range(0,max(data)):
        fuel = 0
        #print(ii)
        for dat in data:
           #print('fuel',fuel)
            fuel += (abs(dat-ii))
        fuels.append(fuel)
    return fuels
    
fuels = align_crabs()  

print('\n' + 'result part 1: ', min(fuels))

def integer_series(n):
    return(sum(list(range(0,n+1))))

def align_crabs_v2():
    fuels = []
    for ii in range(0,max(data)):
        fuel = 0
        for dat in data:
           #print('fuel',fuel)
            fuel += integer_series(abs(dat-ii))
        fuels.append(fuel)
    return fuels
    
fuels_v2 = align_crabs_v2() 
print('\n' + 'result part 2: ', min(fuels_v2) )

