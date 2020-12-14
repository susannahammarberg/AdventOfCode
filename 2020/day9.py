# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 12:11:54 2020

@author: Sanna
"""

import numpy as np


#def day1()

with open('input9.txt','r') as fn:
    record = fn.readlines()
    record = list(map(int,record))
    
    
valid_check = [0]*(len(record))

prea = 25
    
for ii in range(prea,len(record)):
    #print(record[ii])
    
    
    
    # x is valid if the last 'prea' values can be summed to x
    # the values need to be different
    for jj in range(ii-prea, ii):
        for dd in range(ii-prea, ii):
            
            #print(record[jj] + record[dd])
            # is it jj and dd or record[jj] and record[dd] that need to be different?
            if record[jj]+record[dd] == record[ii] and record[jj] != record[dd]:
                #print('valid',record[jj]+record[dd])
                valid_check[ii] += 1
                
                
# index of 0 value
indx = valid_check.index(0,prea)
print('Answer: ', record[indx])



#part 2
with open('input9.txt','r') as fn:
    record = fn.readlines()
    record = list(map(int,record))
    
   
find_nbr = 1721308972#127

for ii in range(0,len(record)):
    for jj in range(ii+2,len(record)):
    
        if sum(record[ii:jj]) == find_nbr:
            find_range = record[ii:jj]
            
            
#kan vara ett index fel nu..
print('min value',min(find_range))
print('max value',max(find_range))
    
    
