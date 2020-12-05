# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 16:03:16 2020

@author: Sanna
"""

import numpy as np

def main():
       
    with open("input5.txt", "r") as fd:
        record = fd.read().splitlines() #for lines without the \n after each line

    #record = 'BBFFBBFRLL'
    
    IDs = []
    
    for item in record:
        
        row = np.arange(0,128)
        col = np.arange(0,8)
        for letter in item:
            #print(letter)
            #upper half
            if letter == 'B':
                row = row[int(len(row)/2):]
                
            # lower half    
            elif letter == 'F':
                row = row[:int(len(row)/2)]
                
            elif letter =='R':
                col = col[int(len(col)/2):]
            elif letter =='L':
                col = col[:int(len(col)/2)]
                
        IDs.append(row[0]*8 +col[0])
            
        
    IDs.sort()
    for ii in range(0,len(IDs)-1):
        if IDs[ii+1]-IDs[ii] != 1:
            print(IDs[ii]+1)
            
            ii=9000
        

    print('Answer: ')
    print(max(IDs))


if __name__ == '__main__':
    
    main()