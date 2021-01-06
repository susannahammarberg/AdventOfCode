# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 13:10:19 2020

@author: Sanna


Masking binary numbers

"""
import copy

with open('input14.txt','r') as fp:
    info = fp.read().splitlines()
    
memory = [0]*1000000   
    
for line in info:
    thing, code = line.split(' = ')
    if thing[0:4] == 'mask':
        print('its mask')
        mask = copy.deepcopy(code)
    else:
        mem = int(thing.split('[')[1].replace(']',' '))

        bin_nbr = bin(int(code))[2:].zfill(36)
        print(bin_nbr)
        print(mask)
        for idx, ma in enumerate(mask):
            if ma != 'X':
                bin_nbr =  bin_nbr[0: idx] + ma + bin_nbr[idx+1:]
        print(bin_nbr)
        print(int(bin_nbr,2))
        memory[mem] = int(bin_nbr,2)
        print(' ')
    
print('answer: ', sum(memory))

import itertools

#part2
with open('input14.txt','r') as fp:
    info = fp.read().splitlines()
    
    
# need to convert to dict with keys othewise get memory error
memory = {} #[0]*10000001   
    
for line in info:
    thing, code = line.split(' = ')
    if thing[0:4] == 'mask':
        print('its mask')
        mask = copy.deepcopy(code)
    else:
        mem = int(thing.split('[')[1].replace(']',' '))
        bin_mem = bin(int(mem))[2:].zfill(36)
        bin_nbr = bin(int(code))[2:].zfill(36)
        print(bin_nbr)
        print(mask)
        for idx, ma in enumerate(mask):
            if ma == '1' or ma == 'X':               
                bin_mem =  bin_mem[0: idx] + ma + bin_mem[idx+1:]
        
        # fin all possible values of memory adress with floating Xs   
        nbr_X = bin_mem.count('X')
        
        # create all possible combinations of 0s and 1s
        
        bin_permut = list(itertools.product([0, 1], repeat=nbr_X))
        save_adress = []
        for ii in range(0,len(bin_permut)):
            X_idx = 0
            bin_mem_copy = copy.deepcopy(bin_mem)
            for idx, letter in enumerate(bin_mem):
                if letter == 'X':
                    bin_mem_copy = bin_mem_copy[0: idx] + str(bin_permut[ii][X_idx]) + bin_mem_copy[idx+1:] 
                    X_idx += 1
                    
            save_adress.append(bin_mem_copy)
        
        # save the code in all the memory adersses
        for adress in save_adress:
            # convert to number
            adress = int(adress,2)
            memory[adress] = int(code)
            
        
        
    print(' ')
    
print('answer: ', sum(memory.values()))
# too high2754698397711229