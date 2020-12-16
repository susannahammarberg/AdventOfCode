# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 17:48:10 2020

@author: Sanna
"""

with open('input10.txt','r') as fn:
    records = fn.readlines()
    records = list(map(int,records))
    
records_sorted = []

diff1 = 0
diff3 = 0
jolt = 0

while len(records_sorted) < len(records):

    test = True
    while test == True :
        test = False
        for index, line in enumerate(records):
            if line == jolt + 1:
                jolt += 1
                diff1 += 1
                #print(line)
                records_sorted.append(line)
                test = True

                
    test2 = True
    for line in records: 
        
        if line == jolt + 3 and test2 == True:
            jolt += 3
            diff3 += 1
            #print('3',line)
            records_sorted.append(line)
            test2 = False


print('Answer: ', diff1* (diff3+1))
#
#for index, item in enumerate(items):
#    print(index, item)
#    