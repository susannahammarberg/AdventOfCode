# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 12:21:39 2017

@author: Sanna
"""

import numpy as np
data = open('C:/Users/Sanna/Documents/Github/adventofcode/2017/input7.txt')
data2 = open('C:/Users/Sanna/Documents/Github/adventofcode/2017/input7.txt')

library = {}
#library[key] = value


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
    # remove paranthesis from the weight (88)
    nbr = linesplit[1].strip("()")
    library[linesplit[0]] = nbr 
# compare the lists
all_words_set=set(all_words)
held_words_set=set(held_words)

bottom_program = list(all_words_set - held_words_set) 
bottom_program = bottom_program[0]
print((bottom_program))



#for line in data2:
#        linesplitL = line.split('->')
#   
tree = {}     

def create_tree(data):
    for line in data:
        oneline_tree = []
        linesplit = line.split()
        #append the words after -> to tree
        if len(linesplit) > 2:
            for i in range(3,len(linesplit)):
                temp = linesplit[i]
                try:
                    temp = temp.strip(',')
                except:
                    pass
                    
                oneline_tree.append(temp)
        # insert the hole line in as a value in a dictionary
        # with the code as your key
        tree[linesplit[0]] = oneline_tree
    
    return tree          
    
tree = create_tree(data2)  

def sum_branch(branch):
   
    if len(tree[branch])==0:             # the progroms on the endge of the branch with no holding programs should just return its own weight
        #sum all progs
        
        return int(library[branch])
    else:
        s=int(library[branch])
        for i in range(0,len(tree[branch])):
            s += sum_branch(tree[branch][i])

        return s

def find_inbalance(branch):
    #find the unbalanced branch:
    balance = []
    for program in branch:
        
        summed_branch = sum_branch(program)
        
        balance.append(summed_branch)
    print(balance)
    
find_inbalance(tree[bottom_program])
print(tree['gqmls'])
find_inbalance(tree['gqmls'])
print(tree['jfdck'])
find_inbalance(tree['jfdck'])
print(tree['marnqj'])
find_inbalance(tree['marnqj'])
#guesse 40981  -too high (knew it was srong)
#1275


#summed_branch(tree['gqmls'])
  ###############################################################################
# ex on recursive function      
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
        