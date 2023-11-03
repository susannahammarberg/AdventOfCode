# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 10:49:12 2023

@author: sanna
"""
import numpy as np

def read_input():
    
    with open('input9.txt','r') as fp:
        info = fp.read().splitlines()
        #info = f.readlines()
    return info

def read_test():    
    test_data = [
    """
    2199943210
    3987894921
    9856789892
    8767896789
    9899965678
    """]
    test_data = test_data[0].split('\n') # same as splitlines
    return test_data[1:-1]

data = read_input()
#data = read_test()
data = [dat.strip() for dat in data]


data_array= []
for line in data:
    data_array.append([int(char) for char in line])

data_array = np.pad(np.array(data_array),1,mode='constant', constant_values=9)
                    

#%%
#part 1

# go through array and look for low points
save_heights = []
for row in range(1,data_array.shape[0]):
    for col in range(1,data_array.shape[1]):
        height = data_array[row,col]
        #above
        if height < data_array[row-1,col] and height < data_array[row+1,col] and height < data_array[row,col-1] and height < data_array[row,col+1]:
            save_heights.append(height)

risk_level = sum(save_heights) + len(save_heights)
print('\n' + 'result part 1: ',risk_level )


#%%
   
print('\n' + 'result part 2: ', )

