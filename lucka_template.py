# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 10:49:12 2023

@author: sanna
"""

def read_input():
    
    with open('input.txt','r') as fp:
        info = fp.read().splitlines()
        #info = f.readlines()
    return info

def read_test():    
    test_data = [
    """
    199
    200
    208
    210
    200
    207
    240
    269
    260
    263
    """]
    test_data = test_data[0].split('\n') # same as splitlines
    return test_data[1:-1]

#data = read_input()
data = read_test()
data = [int(dat) for dat in data] # turn the items to ints

# part 1

   
print('result part 1: ', )



   
print('result part 2: ', )

