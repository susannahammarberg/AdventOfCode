# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 10:49:12 2023

@author: sanna
"""

def read_input():
    
    with open('input6.txt','r') as fp:
        info = fp.read().split(',')
        info  = [int(item) for item in info]
        #info = fp.read().splitlines()
        #info = f.readlines()
    return info

def read_test():    
    test_data = [3,4,3,1,2]
    
    #test_data = test_data[0].split('\n') # same as splitlines
    return test_data

data = read_input()
#data = read_test()
#data = [int(dat) for dat in data] # turn the items to ints

print('starting potint fishes',data)
# part 1
"""
Each day, a 0 becomes a 6 and adds a new 8 to the end of the list,
while each other number decreases by 1 if it was present at the start of the day.
"""

days = 80
for day in range(days):
    add_fishes = 0
    add_fishes_idx = []
    
    for idx, fish in enumerate(data):
        if fish == 0:
            add_fishes += 1
            add_fishes_idx.append(idx)


    # update fish count
    data = [fish-1 for fish in data]
    
    # reset fishes to 6 and add new fish
    for idx in add_fishes_idx:
        data[idx] = 6
        data.append(8)
        
   # print('at the end of the day',data)
        

print('\n' + 'result part 1: ', len(data) )



   
print('\n' + 'result part 2: ', )

