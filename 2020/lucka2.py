# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:40:00 2020

@author: Sanna
"""

import numpy as np

def main():
        
    with open("input2.txt", "r") as fd:
        lines = fd.read().splitlines() #for lines without the \n after each line
       
    valids = 0   
        
    for line in lines: 
        print(line)
        valid_letter = line.split(' ')[1][0]
        valid_range = [int(line.split(' ')[0].split('-')[0]),int(line.split(' ')[0].split('-')[1])]
        print(valid_range)
        
        password = line.split(': ')[1]
        nbr_valid_letters = 0
        for letter in password:
            if letter == valid_letter:
                nbr_valid_letters +=1
        
        #chec if nbr is in range
        if nbr_valid_letters < valid_range[0] or nbr_valid_letters > valid_range[1]:
            print('not valid')
        else:
            valids +=1#
            
            
    print(' ')
    print(valids)



def part2():
    with open("input2.txt", "r") as fd:
        lines = fd.read().splitlines() #for lines without the \n after each line
       
    valids = 0   
        
    for line in lines: 
        print(line)
        valid_letter = line.split(' ')[1][0]
        valid_range = [int(line.split(' ')[0].split('-')[0]),int(line.split(' ')[0].split('-')[1])]
        print(valid_range)
        
        password = line.split(': ')[1]
        
        check = 0
        if password[valid_range[0]-1] == valid_letter:
            check +=1
        if password[valid_range[1]-1] == valid_letter:
            check += 1
            
        
        if check == 1:
            valids +=1
        else:
            print('not valid')
            #
            
            
    print(' ')
    print(valids)

    
if __name__ == '__main__':
 #   main()
    part2()