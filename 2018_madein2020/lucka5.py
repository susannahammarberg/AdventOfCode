# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 16:37:02 2020

@author: Sanna
"""

import numpy as np

import string



def main():
       
    with open("input5.txt", "r") as fd:
        records = fd.read().splitlines() #for lines without the \n after each line

    #records = ['dabAcCaCBAcCcaDA']    
    
    i=0
    iter_ = 0
    
    #did this nicer in part2
    while (iter_ < 20000000):
       
        
            if records[0][i].isupper() is not records[0][i+1].isupper():
                #print(records[0][i])
                if records[0][i].lower() == records[0][i+1].lower():
                    #print(records[0][i], records[0][i+1])
                    records[0] = records[0][:i] + records[0][i+2:] 
                    #print(records[0])
                    
            i += 1
            iter_+=1
            if i > len(records[0])-2:
                i = 0
    print(len(records[0]))

def part2():
    with open("input5.txt", "r") as fd:
        records = fd.read().splitlines() #for lines without the \n after each line

   # records = ['dabAcCaCBAcCcaDA']    
    
    i=0
    #iter_ = 0
    
    alphabet = string.ascii_lowercase
    
    
    lengths = []
    check = 0
    stop_loop = False
    while stop_loop == False:
        
        #iterate thorugh alphabet

#        if records[0][i]..lower() == records[0][i+1].lower():
#            print(records[0][i], records[0][i+1])
#            records[0] = records[0][:i] + records[0][i+2:] 
        
        if records[0][i].isupper() is not records[0][i+1].isupper():
            #print(records[0][i])
            if records[0][i].lower() == records[0][i+1].lower():
                #print(records[0][i], records[0][i+1])
                records[0] = records[0][:i] + records[0][i+2:] 
                #print(records[0])
                check += 1
                    
        i += 1
 
        # if the whole string as been searched 
        if i > len(records[0])-2:
            i = 0            
            if check < 1: 
                stop_loop = True
            
            check = 0
            
    print('answer')
    print(len(records[0]))

if __name__ == '__main__':
    #main()
    part2()