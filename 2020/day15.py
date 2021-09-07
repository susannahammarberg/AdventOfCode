# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 20:42:07 2021

@author: Sanna
"""

start = [0,3,6]

nbrs = []
nbr = 0

#initialize starting numbers
for st in start:
    nbrs.append(st)
    nbr += 1

#the 'aga' numbers
while nbr < 20:
    
    if nbrs.count( nbrs[-1] ) == 1:
        nbrs.append(0)
        
    else: 
        
        #the next number to speak is the difference between the turn number when it was
        #last spoken (the previous turn, 4) and the turn number of the time it was 
        #most recently spoken before then (turn 1). 

        nbrs.append( nbr - (len(nbrs) - 1   - nbrs[-2::-1].index(nbrs[-1]) ))
    nbr += 1
  
    
print(nbrs[-1])

#%%     
    
# part 2
import copy

#start = [0,3]
start = [0,20,7,16,1,18] #last number defined as the first 'new_nbr'

nbrs = {}
nbr = 0

#initialize starting numbers
for new_nbr in start:
    nbrs[new_nbr] = nbr
    nbr += 1

new_nbr = 15    
#the 'aga' numbers
while nbr < 30000000 -1:
    

    # check if  new nbr bara finns en gång, alltså om det finns alls
    # starting numbers talen blir väl lite speciella
    if new_nbr in nbrs.keys():
       # print('yes')
        
        rem_num = copy.deepcopy(new_nbr)
        new_nbr = nbr-nbrs[new_nbr]
        
        nbrs[rem_num] = nbr#-nbrs[rem_num] #ska vara bara senaste va? nbr alltså
        
                
    elif new_nbr not in nbrs.keys():
        nbrs[new_nbr] = nbr
        new_nbr = 0
        
    nbr += 1

print(new_nbr)
       
        
        