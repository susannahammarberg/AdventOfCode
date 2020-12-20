# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 17:48:10 2020

@author: Sanna

Dynamic programming!

"""


# dynamic programming ex:  fibonacci seq
############################################
# memorize values instead of recalculating them

def fibb_recursion(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibb_recursion(n-1)+fibb_recursion(n-2)
    
# dyn prog. for fibb(n), dont recalculate all valus that you already calculated earlier in the series
# Ex:to get fibb(5), you need fibb(3) + fibb(4),
# and to get fibb(3) you need fibb(1)+fibb(2)
# to get fibb(5), you shouldnt have to recalculate fibb(1) and fibb(2)..
# instead, store them in an array ('memoized solution')
def fibb_dyn_mem(n,memory):
    # if the value is in memory, return it
    if memory[n] is not None:
        return memory[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fibb_dyn_mem(n-1,memory)+fibb_dyn_mem(n-2,memory)
    # store that
    memory[n] = result
    return result

# simplify usage with help function
def fibb_dyn(n):
    memory = [] * (n+1)
    return fibb_dyn_mem(n,memory)

fibb_dyn(6)

############################################
# part 1

with open('input10.txt','r') as fn:
    records = fn.readlines()
    records = list(map(int,records))
    
records = [16,
10,
15,
5,
1,
11,
7,
19,
6,
12,
4]
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


#########################################
# Part II

# "The number of paths to get to this adapter from the start is equal to the
#  sum of the number of paths to get from the previous adapter to this one. "


with open('input10.txt','r') as fn:
    records = fn.readlines()
    records = list(map(int,records))
    
 
records.append(0)
set_records = []

records.sort()
#
## nbr of arrangements?
#look at the nbr of ways to get to every adapter
#
#start with 0
#to go to 1, you can go there from (0) =>  1 arr
#to get to 4, you have to go from 1 to 4 => 1 arr
#to get to 5, you have to go from 4+1 => 1 arr
#to get to 6, you can go from 4+2 or 5+1 => 2 arr
#1 4 5 6
#1 4 6
#o get to 7, you can go from 4+3, 5+2, or 6+1 => 4 arr
#
#1 4 ___ 7
#
#1 4  5 __ 7
#
#1 4 5 6  __ 7 
#1 4 6    __ 7
#
#to get to 10, you can only go from 7 => 4
#11, 10+1 => 4 arr
#
#12, 10+2 or 11+2 => 2 arr
#
#1 4 ___ 7 10 __ 12
#1 4  5 __ 7 10 __12
#1 4 5 6  __7 10 __12
#1 4 6    __ 7 10 __12
#
#
#1 4 ___ 7 10 __ 11 __12
#1 4  5 __ 7 10 __ 11__12
#1 4 5 6  __7 10 __ 11 __12
#1 4 6    __ 7 10 __ 11 __12
#
#
#
#15, 12+ 3 => 1 arr
#
#
#16, 15+1 => 1 arr
#19, 16+3 => 1 arr
#
#So, to get to 19 you look at 16, to get that you look at 15 etc  


#recursive:
#works with the exemples
def arr(n):
    if records[n] == 0:
        return 1
    
    result = 0
    for ii in range(1,4):
        # räcker att kolla 3 tidigare element, om de är -1, 2 el 3. elementen
        if records[n-ii] == records[n]-3 or records[n-ii] == records[n]-2 or records[n-ii] == records[n]-1:
            result +=  arr(n-ii)
    return result

arr(0)
arr(1)
arr(2)            
arr(3)
arr(31) #yey this works with the example but not the real input cos its too big

# need to go for dynamic programming
# save values instead of  recalculating multiple times
def arr_dyn_mem(n,memory):
    if memory[n] is not None:
        return memory[n]

    if records[n] == 0:
        return 1
    
    result = 0
    for ii in range(1,4):
        # räcker att kolla 3 tidigare element, om de är -1, 2 el 3. elementen
        if records[n-ii] == records[n]-3 or records[n-ii] == records[n]-2 or records[n-ii] == records[n]-1:
            result +=  arr_dyn_mem(n-ii,memory)
    memory[n] = result
    return result

# simplify usage with help function
def arr_dyn(n):
    memory = [None] * len(records)
    return arr_dyn_mem(n,memory)

arr_dyn(31)
arr_dyn(10)
arr_dyn(50)


print('Answer: ', arr_dyn(93))
