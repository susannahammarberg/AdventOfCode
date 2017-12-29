# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 12:21:39 2017

@author: Sanna
"""

import numpy as np
data = open('C:/Users/Sanna/Documents/Github/adventofcode/2017/input7.txt')

all_words = []
held_words = []    #the words after ->
for line in data:
    linesplit = line.split()
    # append the first word in each line
    all_words.append(linesplit[0])
    
    #append the words after -> to another list
    if len(linesplit) > 2:
        for i in range(3,len(linesplit)):
            temp = linesplit[i]
            try:
                temp = temp.strip(',')
            except:
                pass
                
            held_words.append(temp)
            
            
# compare the lists
all_words_set=set(all_words)
held_words_set=set(held_words)

print( list(all_words_set - held_words_set))


