# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 21:24:41 2020

@author: Sanna
"""

with open('input12.txt','r') as fp:
    instr = fp.readlines()
 
#clockwise rotation math trick
def rotate90degCW(y,x):
    return(-x,y)
#counterclockwise rotation math trick
def rotate90degCCW(y,x):
    return(x,-y)
    
def part1():
    #"starts by facing east"
    # 0 is to the east 90 is to the south, 180 to the west, 270 to the north
    direction = 0
    ycoord = 0
    xcoord = 0
    for ins in instr:
        print(ins)
        action = ins[0]
        value = int(ins[1:])
        print('action',action)
        print('value',value)
        
        if action == 'N':
            ycoord -= value
        elif action == 'S':
            ycoord += value
        elif action == 'W':
            xcoord -= value
        elif action == 'E':
            xcoord += value
        elif action == 'L':
            direction = (direction - value) % 360
            print('new direction:',direction)
        elif action == 'R':
            direction = (direction + value) % 360
            print('new direction:',direction)        
        elif action == 'F':
            if direction == 0:
                xcoord += value
            elif direction == 90:
                ycoord += value
            elif direction == 180:
                xcoord -= value
            elif direction == 270:
                ycoord -= value
    
    
    # calc manhattan distance
    print('MAnhattan distance: ', ycoord + xcoord)           
#part1()


def part2():
    #instr = ['F10',
    #'N3',
    #'F7',
    #'R90',
    #'F11']
    
    # part 2 13:56
    
    #The waypoint starts 10 units east and 1 unit north relative to the ship.
    w_direction = 0
    w_ycoord = -1
    w_xcoord = 10
    
    s_ycoord = 0
    s_xcoord = 0
    
    for ins in instr:
        print(ins)
        action = ins[0]
        value = int(ins[1:])
        print('action',action)
        print('value',value)
        
        y_rel = w_ycoord-s_ycoord
        x_rel = w_xcoord-s_xcoord
        
        if action == 'N':
            w_ycoord -= value
        elif action == 'S':
            w_ycoord += value
        elif action == 'W':
            w_xcoord -= value
        elif action == 'E':
            w_xcoord += value
        elif action == 'L':
            rot = int(value/90) 
            # rot 90 deg multiple times
            for ii in range(0,rot):
                y_rel, x_rel = rotate90degCW(y_rel,x_rel)
            w_ycoord = y_rel + s_ycoord
            w_xcoord = x_rel + s_xcoord
            
        elif action == 'R':
            rot = int(value/90) 
            # rot 90 deg multiple times
            for ii in range(0,rot):
                y_rel, x_rel = rotate90degCCW(y_rel,x_rel)
                print(value)
                print(y_rel,x_rel)
            w_ycoord = y_rel + s_ycoord
            w_xcoord = x_rel + s_xcoord
            
        elif action == 'F':        
            s_ycoord += value*y_rel
            w_ycoord += value*y_rel
            
            s_xcoord += value*x_rel
            w_xcoord += value*x_rel
                
        print('ships coordinates: ', s_ycoord, s_xcoord)
        print('waypoint coordinates relative to ship: ', w_ycoord-s_ycoord, w_xcoord-s_xcoord)
        print()
    
    print('Manhattan distance: ', abs(s_ycoord) + abs(s_xcoord))           
part2()