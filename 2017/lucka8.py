# -*- coding: utf-8 -*-
"""
Created on Mon Jan 01 18:43:23 2018

@author: Sanna
"""
import numpy as np
data = open('C:/Users/Sanna/Documents/Github/adventofcode/2017/input9.txt')
data = '{{<!>},{<!>},{<!>},{<a>}}'
points = 0
left_brac = 0
print(data)
for letter in data:
    if letter == '{':
        left_brac += 1
    if letter == '}' and left_brac > 1:
        points += left_brac
        left_brac -= 1
        
        
print(points)
    


