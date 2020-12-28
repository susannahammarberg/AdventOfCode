# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 14:35:55 2020

@author: Sanna


Occupying seats
"""
import copy

with open('input11.txt','r') as fp:
    seats = fp.readlines()
    
    
#make grid 2 pixels wider and higher
occupancy = []
for ii in range(0,len(seats)+2):
     occupancy.append([0]*(len(seats[0])-1+2))
     

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







#part2

with open('ex11.txt','r') as fp:
    seats = fp.readlines()
    
    
#make grid 2 pixels wider and higher
# all 'L' or '.' will be 0
occupancy = []
for ii in range(0,len(seats)+2):
     occupancy.append([0]*(len(seats[0])+2))
     
for yy in range(0,len(seats)):
    for xx in range(0,len(seats[0])-1): #-1 becauce of \n
        if seats[yy][xx] == 'L':
            print('hh')
            occupancy[yy+1][xx+1] = 33
        elif seats[yy][xx] == '#': 
            occupancy[yy+1][xx+1] = 1


def count_visible_neighbours(y,x, old_occupancy):
   
    nbr_neighbours = 0
    print(' ')

    # naighbours to the left:
    neighbour = 0
    xx = copy.deepcopy(x)
    while xx>1 and neighbour == 0:
        xx -= 1
        if old_occupancy[y][xx] == 33:
            print('L')
            xx = -10000
        elif old_occupancy[y][xx] == 1:
                neighbour = 1
                      
    print('leftneighbiur',str(neighbour))
    nbr_neighbours += neighbour
        
    #right
    neighbour = 0
    xx = copy.deepcopy(x)
    while xx<len(old_occupancy[0])-2 and neighbour == 0:
        xx += 1
        if old_occupancy[y][xx] == 33:
            print('L')
            xx = 10000       
        elif old_occupancy[y][xx] == 1:
                neighbour = 1
                print('right')

    print('right neighbiur',str(neighbour))
    nbr_neighbours += neighbour
    
    # above
    neighbour = 0
    yy = copy.deepcopy(y)
    while yy > 1 and neighbour == 0:
        yy -= 1 
        if old_occupancy[yy][x] == 33:
            yy = -1000
        elif old_occupancy[yy][x] == 1:
            neighbour = 1
    print('above neighbiur',str(neighbour))
    nbr_neighbours += neighbour
    
    #below
    neighbour = 0
    yy = copy.deepcopy(y)
    while yy < len(old_occupancy)-1 and neighbour == 0:
        yy += 1
        print('x in below',x)
        print('yy in below',yy)
        if old_occupancy[yy][x] == 33:
            yy = 1000
        elif old_occupancy[yy][x] == 1:            
            neighbour = 1

    print('below neighbiur',str(neighbour))
    nbr_neighbours += neighbour      

    #diagonal top left      
    neighbour = 0
    yy = copy.deepcopy(y)
    xx = copy.deepcopy(x)
    while yy > 1 and xx > 1 and neighbour == 0:
        yy -= 1
        xx -= 1
        if old_occupancy[yy][xx] == 33:
            yy = -1000
        elif old_occupancy[yy][xx] == 1:            
            neighbour = 1

    print('top left neighbour',str(neighbour))
    nbr_neighbours += neighbour      

    #diagonal top right      
    neighbour = 0
    yy = copy.deepcopy(y)
    xx = copy.deepcopy(x)
    while yy > 1 and xx<len(old_occupancy[0])-2 and neighbour == 0:
        yy -= 1
        xx += 1
        if old_occupancy[yy][xx] == 33:
            yy = -1000
        elif old_occupancy[yy][xx] == 1:            
            neighbour = 1

    print('top right neighbour',str(neighbour))
    nbr_neighbours += neighbour      

    #diagonal bottom left
    neighbour = 0
    yy = copy.deepcopy(y)
    xx = copy.deepcopy(x)
    while yy < len(old_occupancy)-1  and xx > 1 and neighbour == 0:
        yy += 1
        xx -= 1
        if old_occupancy[yy][xx] == 33:
            yy = 1000
        elif old_occupancy[yy][xx] == 1:            
            neighbour = 1

    print('bottom left neighbour',str(neighbour))
    nbr_neighbours += neighbour      
    
    #diagonal bottom right
    neighbour = 0
    yy = copy.deepcopy(y)
    xx = copy.deepcopy(x)
    while yy < len(old_occupancy)-1  and xx < len(old_occupancy[0])-2 and neighbour == 0:
        yy += 1
        xx += 1
        if old_occupancy[yy][xx] == 33:
            yy = 1000
        elif old_occupancy[yy][xx] == 1:            
            neighbour = 1

    print('bottom right neighbour',str(neighbour))
    nbr_neighbours += neighbour      
    
    
            
        

    return nbr_neighbours 
  
#print(count_visible_neighbours(5,4,old_occupancy))

this = True
while this is True:

    old_occupancy = copy.deepcopy(occupancy)
    
    # anpassa range to the 0-occupancy frame
    for y in range(1,len(seats)+1):
        for x in range(1,len(seats[0])-1+1):
            
            if seats[y-1][x-1] != '.':
                print('x',x)
                print('y',y)
                check = count_visible_neighbours(y,x, old_occupancy)
                
                if check == 0:
                    occupancy[y][x] = 1
                elif check >4:
                    occupancy[y][x] = 33
                
    if occupancy == old_occupancy:
        this = False
    
    
        
sum_= 0
for li in occupancy:
    # make all '33' to '0'
    li[li==33] = 1
    sum_ += sum(li)
    
print('answer ' , sum_)

#TODO 
# det ska inte vara nån 1 a i occupancys "ram"
