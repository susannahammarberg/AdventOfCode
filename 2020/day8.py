# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 17:01:23 2020

@author: Sanna
"""

import numpy as np
       
with open("ex8.txt", "r") as fd:
    record = fd.read().splitlines() #for lines without the \n after each line
    
accumulator  = 0

check = [0] * len(record)

ii = 0
while 2 not in check:
    check[ii] += 1 
    
    inst = record[ii].split(' ')
    
    if inst[0] == 'acc':
        print(inst[1])
        accumulator += int(inst[1])
        ii += 1
    elif inst[0] == 'jmp':
        ii = ii + int(inst[1])
    else:
        ii += 1
        

# reverse the last accumulation that caused check to include a '2'
accumulator -= int(inst[1])
print('Answer: ')
print(accumulator)


# part2
with open("input8.txt", "r") as fd:
    record = fd.read().splitlines() #for lines without the \n after each line
  

#find the nop ad jump s and their indices in record
indx = []
for ll in range(0,len(record)):
    if record[ll].split(' ')[0] == 'jmp' or record[ll].split(' ')[0] == 'nop':
        indx.append(ll)


idx = 0
ll = 0
while True:
    print('try',ll)

#    change one jmo/nod
    
    if record[ll].split(' ')[0] == 'jmp':
        original = record[ll]  
        record[ll] = 'nop ' + record[ll].split(' ')[1] 
        
    elif record[ll].split(' ')[0] == 'nop':
        original = record[ll]
        record[ll] = 'jmp ' + record[ll].split(' ')[1] 
    else:
        original = record[ll]
        
        
      
    
    accumulator  = 0
    check = [0] * len(record)
    ii = 0
    while 2 not in check:
        check[ii] += 1 
        
        inst = record[ii].split(' ')
        
        if inst[0] == 'acc':
            #print(inst[1])
            accumulator += int(inst[1])
            ii += 1
        elif inst[0] == 'jmp':
            ii = ii + int(inst[1])
        else:
            ii += 1
           
    #change the one jmo/nod back
    print('original',original)
    print('record',record[ll])
    record[ll] = original
    # om det inte blir något konstigt att hv är samma sak som varanra    
    ll+=1    

# reverse the last accumulation that caused check to include a '2'
#accumulator -= int(inst[1])
print('Answer: ')
print(accumulator)

#too high 1365