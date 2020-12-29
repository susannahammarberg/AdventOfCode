# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 21:46:51 2020

@author: Sanna
"""


with open('input13.txt','r') as fp:
    info = fp.readlines()
        
bus_list = info[1].split(',')


for bus in bus_list:
    
    if bus != 'x':
        
    
        print(bus)