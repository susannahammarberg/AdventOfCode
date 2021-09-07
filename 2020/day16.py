# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 12:05:57 2021

@author: Sanna
"""

with open('input16.txt') as fp:
    ticket = fp.read()
    
    
    
intervals = []


rules = ticket.split('your ticket')[0].splitlines()[0:-1]

for rule in rules:
    intervals.append(rule.split(': ')[1].split(' or '))
    
nearby_tickets = ticket.split('nearby tickets:')[1].splitlines()[1:]

unvalids = []
unvalid_indices = []

for idx, n in enumerate(nearby_tickets):
    times = n.split(',')
    for time in times:
        #print(time)
        check = 0
        #while check == 0:
        # does 'time' fit in in any interval?
        for interval in intervals:
            if int(time) >= int(interval[0].split('-')[0]) and int(time) <= int(interval[0].split('-')[1]):
                check = 1
            if int(time) >= int(interval[1].split('-')[0]) and int(time) <= int(interval[1].split('-')[1]):
                check = 1
        if check == 0:
            unvalids.append(time)
            unvalid_indices.append(idx)
            
        print()
sum_ = 0 
for un in unvalids:
    sum_ += int(un)
            
print('Answer: ', sum_)


#%%
# part2

valid_nearby_tickets = []

for ii, ticket in enumerate(nearby_tickets): 
    if ii not in unvalid_indices:
        valid_nearby_tickets.append(ticket)

#%%
import itertools
import copy
from collections import defaultdict


#with open('ex2_16.txt') as fp:
#    ticket = fp.read()
#    
# a dictionary to hold possible fields for each col
#    gå igenom vaje ticket
#    kolla alla fält
#    om något fält är ogiltligt ta bort de
#    
    
#possible_fields = [[class seat row][class seat row][class seat row]] 
# represented by [[0 1 2],[ 0 1 2],[ 0 1 2]]
#discard if not vaid
    

# for the example
#intervals = []
#rules = ticket.split('your ticket')[0].splitlines()[0:-1]
#for rule in rules:
#    intervals.append(rule.split(': ')[1].split(' or '))  
#nearby_tickets = ticket.split('nearby tickets:')[1].splitlines()[1:]

nearby_tickets = copy.deepcopy(valid_nearby_tickets)

# TODO this doesnt work! To large'1
possible_orders = list(itertools.permutations(list(range(len(rules)))))
#type(possible_orders[2])

while True:
    for n in nearby_tickets:
        times = n.split(',')
        
        exx = 0 
        #loopa detta på annat sätt för possible_orders blir mindre..
        for exx in range(0,len(possible_orders)):
        
            check = 0 
            for time_idx,time in enumerate(times):
                #print(time)
                       
                idx = possible_orders[exx]
                # behövs inte?
                #check_time = times[idx[time_idx]]
                #print('check time' , times[idx[time_idx]])
        
                if int(time) >= int(intervals[idx[time_idx]][0].split('-')[0]) and int(time) <= int(intervals[idx[time_idx]][0].split('-')[1]):
                    check += 1
                if int(time) >= int(intervals[idx[time_idx]][1].split('-')[0]) and int(time) <= int(intervals[idx[time_idx]][1].split('-')[1]):
                    check += 1
               
            #print()    
    
            if check != 3: 
                del possible_orders[exx]
                #print('time_idx',time_idx)
                    
                
                break
                #when one dict key only has one item. remove that item from all other keys. etc
            
    if len(possible_orders) == 1:
        break
