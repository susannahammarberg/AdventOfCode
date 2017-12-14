# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 12:21:21 2017

@author: HonkyT

Snake vector thingy!!
"""


#5 4 3
#6 1 2
#7 8 9 

#while counter<tal:   
def snakefunction(tal):
    #initialize variables on the number 3
    ###############################
    counter=3  
    x_idx=1
    y_idx=1
    varv=2  #or 'circle' or 'spiral'
    # representation but it
    # increses by 2 each turn
    ####################

    while counter<tal:
        ll=0
        dd=0
        rr=0
        uu=0
        # to the left
        while ll<varv:
            x_idx -= 1
            ll+=1
            counter+=1
            if counter==tal:
                return x_idx,y_idx
        # down
        while dd<varv:
            y_idx -= 1  
            dd+=1
            counter+=1
            #print('dd')
            if counter==tal:
                return x_idx,y_idx
           # to the right 
        while rr<(varv+1):
            x_idx +=1
            rr+=1
            counter+=1
            #print('rr')
            if counter==tal:
                return x_idx,y_idx
        # up
        while uu<(varv+1):
            y_idx+=1
            uu+=1
            counter+=1
            #print('uu')
            if counter==tal:
                return x_idx,y_idx
        
        varv+=2
        
#Choose what nbr to determine >2
tal=7#361527
xin,yin=snakefunction(tal)
#origo = [0, 0]
steps = abs(-xin) + abs(-yin)
#print('Nbr of steps:')
#print(steps)


#star2 
#koordinaterna och värdena sparas

#while counter<tal:   
def snakefunction2(tal):
    #initialize variables on the number 3
    ###############################
    counter=0
    snake = [1,1,2]
    snake_inx = []
    snake_inx.append([0,0])
    snake_inx.append([1,0])
    snake_inx.append([1,1])
       
    x_idx=1
    y_idx=1
    varv=2
    
    #or 'circle' or 'spiral'
    # representation but it
    # increses by 2 each turn
    ####################

    while counter<tal:
        ll=0
        dd=0
        rr=0
        uu=0
        b=0
        # to the left
        while ll<varv:
            print('Moving to the left')
            x_idx -= 1
            ll+=1
            # search for indeces 
            for jj in range(-1,2):
                try:
                    a=snake_inx.index([x_idx+jj,y_idx-1])
                    counter+=snake[a] # sum the values of the 3 cells below the current cell
                    print('counter in try:')
                    print(counter)
                except ValueError:
                    a=0
                    print('non')
            # add the previos value (the one to the right)
            # find the index to that value:
            b=snake_inx.index([x_idx+1,y_idx])
            counter+=snake[b] 
            snake.append(counter)
            print('counter after adding right')
            print(counter)
            snake_inx.append([x_idx,y_idx])
            if counter>tal:
                return snake
            counter=0
            
        # down
        while dd<varv:
            y_idx -= 1  
            dd+=1
            print('moving down')
            # search for indeces 
            for jj in range(-1,2):
                try:
                    a=snake_inx.index([x_idx+1,y_idx-jj])
                    counter+=snake[a]
                    print('counter in try:')
                    print(counter)
                except ValueError:
                    a=0
                    print('non')
            # add the previos value (the one above) to the counter
            a=snake_inx.index([x_idx,y_idx+1])
            counter+=snake[a] 
            snake.append(counter)
            print('counter after adding above cell')
            print(counter)
            snake_inx.append([x_idx,y_idx])
            if counter>tal:
                return snake
            counter=0
            
           # to the right 
        while rr<(varv+1):
            x_idx +=1
            rr+=1
            print('move to the right')
            # search for indeces 
            for jj in range(-1,2):
                try:
                    a=snake_inx.index([x_idx+jj,y_idx+1])
                    counter+=snake[a]
                    print(snake[a])
                except ValueError:
                    a=0
                    print('non')
            # add the previos value (the one to the right)
            a=snake_inx.index([x_idx-1,y_idx])
            counter+=snake[a] 
            snake.append(counter)
            snake_inx.append([x_idx,y_idx])
            if counter>tal:
                return snake
            counter=0
            
        # up
        while uu<(varv+1):
            y_idx+=1
            uu+=1
            print('move up')
            # search for indeces 
            for jj in range(-1,2):
                try:
                    a=snake_inx.index([x_idx-1,y_idx-jj])
                    counter+=snake[a]
                    print(snake[a])
                except ValueError:
                    a=0
                    print('non')
            # add the previos value (the one below) but if you are in the corner there is nothing there
            try:
                a=snake_inx.index([x_idx,y_idx-1])
                counter+=snake[a] 
                snake.append(counter)
            except ValueError:
                a=0
            snake_inx.append([x_idx,y_idx])
            if counter>tal:
                return snake
            counter=0
        # for every 'varv' there are two more cells
        varv+=2
        
#Choose what nbr to determine >2
tal=361527
snake=snakefunction2(tal)

