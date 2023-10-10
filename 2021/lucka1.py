# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 10:49:12 2023

@author: sanna
"""

def utils():
    
    def sub_list(data_list):
        # (not used yet, did the wrong thing)
        N = 3
        sub_list = [sum(data_list[ii:ii+N]) for ii in range(0, len(data_list), N)]
        return sub_list
               
    def str2int_list(data):
        data = [int(dat) for dat in data] # turn the items to ints
    


def read_input():
    
    with open('input1.txt','r') as fp:
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

    
data = read_input()
#data = read_test()
data = [int(dat) for dat in data] # turn the items to ints

#%% day 1 solution part 1
counts = 0
past_dat = 0 
for ite, dat in enumerate(data):
    if dat > past_dat:
        counts += 1
    past_dat = dat
    
print('answer 1: ',counts-1) #dont count the first measurement


#%%
# part 2
# change to three-measurement sum

# define 3-group list

N = 3
#three_group = []
#for ii in range(len(data)):
#    three_group.append(sum(data[ii:ii+N]))
#this is written in a more compact way as:
three_group = [sum(data[ii:ii+N]) for ii in range(len(data))]

# count the number of higher sums in the list
    
counts_threesum = 0
past_group = 0
for ite, dat in enumerate(three_group):
    if dat > past_group:
        counts_threesum += 1
    past_group = dat
    
print('this', counts_threesum-1)


    


