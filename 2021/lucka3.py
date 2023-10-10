# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 10:49:12 2023

@author: sanna
"""
import copy

def read_input():
    
    with open('input3.txt','r') as fp:
        info = fp.read().splitlines()
        #info = f.readlines()
    return info

def read_test():    
    test_data = [
    """
    00100
    11110
    10110
    10111
    10101
    01111
    00111
    11100
    10000
    11001
    00010
    01010
    """]
    test_data = test_data[0].split('\n') # same as splitlines
    return test_data[1:-1]

data = read_input()
#data = read_test()
#data = [int(dat) for dat in data] # turn the items to ints

#part 1 
# make a matrix and use list method .count to count number of 1s and 0s
data = [dat.strip() for dat in data]
data = list(zip(*data))


gamma_rate = []

ii = 0
while ii < len(data):
    count_0 = data[ii].count('0')
    count_1 = data[ii].count('1')
    
    if count_0 > count_1:
        gamma_rate.append(0)
    else:
        gamma_rate.append(1)
    ii += 1

print(gamma_rate)

epsilon_rate = [1 if gam == 0 else 0  for gam in gamma_rate]  #snyggt!

# turn list values into base 10 ints

gamma_rate = str(gamma_rate).replace(',','').strip('[').strip(']').replace(' ','')
gamma_rate = int(gamma_rate,base=2)
epsilon_rate = str(epsilon_rate).replace(',','').strip('[').strip(']').replace(' ','')
epsilon_rate = int(epsilon_rate,base=2)

pow_cons = gamma_rate * epsilon_rate

print('result part 1: ', pow_cons)

print(data[0])
# start part 2


def calc_oxy(data_): 
    
    #data_ = data.copy()
    ii = 0
    while ii < len(data_):
        indices = []
        
        count_0 = data_[ii].count('0')
        count_1 = data_[ii].count('1')
        
        if count_0 > count_1:
            #print('there are mostly 0s here')
            #find the indices of the ones you need to delete (the 1s in this case)
            for jj in range(0,len(data_[ii])):
                if data_[ii][jj] == '1':
                    print('1')
                    indices.append(jj)
            
        else:
            #print('there are mostrly 1s here')
            #save the indices of the 0s
            for jj in range(0,len(data_[ii])):
                if data_[ii][jj] == '0':
                    indices.append(jj)
             
        #print(indices)
        # delete the indices    
        #*delete those indices in all rows (so that those numbers are deleted)
        # reverce the indices list so they can be removed one by one starting
        # from the end of the list
        indices.reverse()
        
        
        for dat in data_:
 #           print(' vilken dat')
            for ind in indices:
                dat.pop(ind)
#                print('ta bort')   
        
        ii += 1
    
    oxyg_grate = []
    for dat in data_:
        oxyg_grate.append(dat[0])
    oxyg_grate = ''.join(oxyg_grate)
    oxyg_grate = int((oxyg_grate),base=2)
    
    return oxyg_grate


def calc_CO2(data_):
    ii = 0
    while len(data_[0]) > 1:
        print(data_)
        indices = []
        
        count_0 = data_[ii].count('0')
        count_1 = data_[ii].count('1')
        
        if count_0 < count_1 or count_0 == count_1:
            print('there are fewest 0s here, keep those numbers')
            #*find the indices of the ones you need to delete (the 1s in this case)
            for jj in range(0,len(data_[ii])):
                if data_[ii][jj] == '1':
                    indices.append(jj)
            
        else:
            print('there are fewest 1s here')
            #save the indices of the 0s for removal
            for jj in range(0,len(data_[ii])):
                if data_[ii][jj] == '0':
                    indices.append(jj)
             
        print('indices',indices)
        # delete the indices    
        #*delete those indices in all rows (so that those numbers are deleted)
        # reverce the indices list so they can be removed one by one starting
        # from the end of the list
        indices.reverse()
        
        print(indices)
        
        for dat in data_:
            for ind in indices:
                dat.pop(ind)
    
        
        ii += 1
     
    CO2_grate = []
    for dat in data_:
        CO2_grate.append(dat[0])
    CO2_grate = ''.join(CO2_grate)
    CO2_grate = int((CO2_grate),base=2)
    return CO2_grate
 

# change tuples inside data to lists
data = [list(dat) for dat in data]
# OBS functions changes lists. (they are mutable)
#.copy() does not work for nested objects. need to use deepcopy


# change tuples inside data to lists
data = [list(dat) for dat in data]
# OBS functions changes lists. (they are mutable)
#.copy() does not work for nested objects. need to use deepcopy

#data_Save = copy.deepcopy(data)
# or
#data_save2 = [x[:] for x in data]
# method .copy() i think is the same as just assignind data_copy = data[:]
oxy_rate = calc_oxy(data_= copy.deepcopy(data))
print('oxy_rate is',oxy_rate)
#%%

# nu funkar det inte för data har ändrats. trodde inte den ändrades i funktionen. 
# "Because lists and dictionaries are mutable, changing them (even inside a function) changes the list or dictionary itself, which isn't the case for immutable data types."
#############################################################################
CO2_rate = calc_CO2(data_ = data)



print('result part 2: ', oxy_rate*CO2_rate)
