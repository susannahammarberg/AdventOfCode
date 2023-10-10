# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 10:49:12 2023

@author: sanna
"""

def read_input():
    
    with open('input2.txt','r') as fp:
        info = fp.read().splitlines()
        #info = f.readlines()
    return info

def read_test():    
    test_data = [
    """
    forward 5
    down 5
    forward 8
    up 3
    down 8
    forward 2
    """]    
    test_data = test_data[0].split('\n') # same as splitlines
    return test_data[1:-1]



data = read_input()
#data = read_test()

# part 1
hor_pos = 0
depth_pos = 0

for dat in data:
    
   dat = dat.strip()
   
   if dat[0] == 'f':
       hor_pos += int(dat[-1])
   elif dat[0] == 'u':
       depth_pos -= int(dat[-1])
   elif dat[0] == 'd':
       depth_pos += int(dat[-1])

   
print('result part 1: ', hor_pos*depth_pos)




#part 2: 
    

hor_pos = 0
depth_pos = 0
aim = 0

for dat in data:
    
   dat = dat.strip()
   
   if dat[0] == 'f':
       hor_pos += int(dat[-1])
       depth_pos += aim * int(dat[-1])
   elif dat[0] == 'u':
       aim -= int(dat[-1])
   elif dat[0] == 'd':
       aim += int(dat[-1])

   
print('result part 2: ', hor_pos*depth_pos)
