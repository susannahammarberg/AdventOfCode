# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 14:35:55 2020

@author: Sanna


Occupying seats
"""
import copy

with open('input11.txt','r') as fp:
    seats = fp.readlines()
    
    
#make it 2 pixels wider and higher
occupancy = []
for ii in range(0,len(seats)+2):
     occupancy.append([0]*(len(seats[0])-1+2))
     
# test: occupy
#for jj in range(1,len(seats)+1):
#    for kk in range(1,len(seats[0])-1+1):
#        occupancy[jj][kk] = 1

#If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
#If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.

def count_neighbours(y,x, occupa): 
#    1 1 1
#    1 0 1
#    1 1 1
    
    nbr_neighbours = 0
    nbr_neighbours += sum(occupa[y-1][x-1:x+2])
    nbr_neighbours += occupa[y][x-1]
    nbr_neighbours += occupa[y][x+1]
    nbr_neighbours += sum(occupa[y+1][x-1:x+2])

    return nbr_neighbours 



#isf loop, map(count_neighbours,seats)

this = True
while this is True:

    old_occupancy = copy.deepcopy(occupancy)
    
    # anpassa range to the 0-occupancy frame
    for y in range(1,len(seats)+1):
        for x in range(1,len(seats[0])-1+1):
            
            if seats[y-1][x-1] != '.':
                check = count_neighbours(y,x, old_occupancy)
                
                if check == 0:
                    occupancy[y][x] = 1
                elif check >3:
                    occupancy[y][x] = 0
                
    if occupancy == old_occupancy:
        this = False
    
sum_=0
for li in occupancy:
    sum_ += sum(li)
    
print('answer ' , sum_)
