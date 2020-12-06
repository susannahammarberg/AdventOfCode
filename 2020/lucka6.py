# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 18:46:53 2020

@author: Sanna
"""


import numpy as np

def main():
    
    with open("input6.txt", "r") as fd:
        records = fd.read().split('\n\n') #for lines without the \n after each line    
 
    print(records)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    nbr_per_group = []
  
    for group in records:
        group_counter = [0]*len(alphabet)
        print(group)

        for row in group:
            for letter in row:
                if letter != '\n':

                    #print('letter', letter)
                    idx = alphabet.find(letter)
                    group_counter[idx] += 1
                    #print('idx',idx)
        print(group_counter)
        #print('rader i gruppen: ', len(group.split('\n')))
        
        #hur många rader i gruppen:
        
        if group[-1] == '\n':
           # print('ends with n', group)
            #remove it
            group = group[:-1]

        group_rows = len(group.split('\n'))
        
        yes_questions = 0
        for ii in range(0,len(group_counter)):            
            if group_counter[ii] == group_rows:                 
                yes_questions += 1
        nbr_per_group.append(yes_questions)
               
                
    print(sum(nbr_per_group))
    
if __name__ == '__main__':
    
    main()
                