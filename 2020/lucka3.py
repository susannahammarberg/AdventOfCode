# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 16:20:42 2020

@author: Sanna
"""

import numpy as np

def main():
      
    with open("input3.txt", "r") as fd:
        map_ = fd.read().splitlines() #for lines without the \n after each line
      
        
#    with open("ex_day3.txt", "r") as fd:
#        map_ = fd.read().splitlines() #for lines without the \n after each line

    threes = 0
    idx = 0
    for row in map_:
        print(row)
        sign = row[idx %len(row)] 
        if sign == '#':
            print(sign)
            threes += 1
        idx += 3

    print('Answer: ')
    print(threes)

def part2():

#    Right 1, down 1.
#    Right 3, down 1. (This is the slope you already checked.)
#    Right 5, down 1.
#    Right 7, down 1.
#    Right 1, down 2.
    with open("input3.txt", "r") as fd:
        map_ = fd.read().splitlines() #for lines without the \n after each line

#    with open("ex_day3.txt", "r") as fd:
#        map_ = fd.read().splitlines() #for lines without the \n after each line


    threes_1 = 0
    idx = 0
    for row in map_:
        sign = row[idx %len(row)] 
        if sign == '#':
            threes_1 += 1
        idx += 1

    threes_2 = 0
    idx = 0
    for row in map_:
        sign = row[idx %len(row)] 
        if sign == '#':
            threes_2 += 1
        idx += 3

    threes_3 = 0
    idx = 0
    for row in map_:
        sign = row[idx %len(row)] 
        if sign == '#':
            threes_3 += 1
        idx += 5
        
    threes_4 = 0
    idx = 0
    for row in map_:
        sign = row[idx %len(row)] 
        if sign == '#':
            threes_4 += 1
        idx += 7

    threes_5 = 0
    idx = 0
    idx_2 = 0
    for idx_2 in range(0,len(map_),2):
        print(idx_2)
        row = map_[idx_2]
        sign = row[idx %len(row)] 
        if sign == '#':
            threes_5 += 1
        idx += 1

    # not 7397677560
    # not 10584369432 too high
    #      5007658656

    print('Answer: ')
    print(threes_1)
    print(threes_2)
    print(threes_3)
    print(threes_4)
    print(threes_5)
    print( )         
    print(threes_1 * threes_2 * threes_3 * threes_4 * threes_5)
   
if __name__ == '__main__':
    #main()
    part2()