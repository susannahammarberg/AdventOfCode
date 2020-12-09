# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 13:13:17 2020

@author: Sanna
"""

import numpy as np


class Bag:
    
    
    def __init__(self,color):
        self.color = color
        self.children = []
        
    def has_color(self,color):
        #print(self.color)

        if color == self.color:
            return True
        elif len(self.children) == 0:
           # print('does this happen???????????????????????????????')
            return False
        else:
            for child in self.children:
                #print('but this works?')
                return child.has_color(color)


#bg = Bag('gold')
#print(bg.children)
#b1 = Bag('white')
#print(bg.children)
#b1.children.append(bg)
#print(bg.children)
#
#b2 = Bag('yellow')
#b2.children.append(bg)    
#b3 = Bag('orange')
#b3.children.append(b1)
#b3.children.append(b2)
#b4 = Bag('red')
#b4.children.append(b1)
#b4.children.append(b2)
#
#b1.has_color('white')
#b1.has_color('gold')
#b1.has_color('green')

def main():
       
    with open("input7.txt", "r") as fd:
        record = fd.read().splitlines() #for lines without the \n after each line


    bags = []
    
    #define all bags in a list before defining what bags goes in the bags
    for line in record:
        
        parent_color = line.split(' ')[0:2]
        parent_color = ' '.join(parent_color)
 
        print('new color')
        print(parent_color)
        b1 = Bag(parent_color)
        bags.append(b1)



    idx = 0
    for line in record:
        b3 = bags[idx]

        if not 'no other' in line:
            
            if ',' in line: 
                line = line.strip('s.')
                
                
                
                for item in line.split('bag')[1:-1]:
                 #    daughter_color = ' '.join(parent_color)   
                 #   print(item.split(' ')[-2])
                    #daughter_colors.append(item.split(' ')[-2])                    
                    #b1.children.append(item.split(' ')[-2])
                    daughter_color = ' '.join(item.split(' ')[-3:-1])
                    
                    #print(daughter_color)
                    for bag in bags:
                        if bag.color == daughter_color:
                            b3.children.append(bag)
                    
            else:
                #print('daughter')
                #print(record[2].split(' ')[-2])
                #b1.children.append((record[2].split(' ')[-2]))
                
                for bag in bags:
                    

                    daughter_color = ' '.join(line.split(' ')[-3:-1])
                    
                    if bag.color == daughter_color:
                        b3.children.append(bag)
                        print('this is one')
                                
        idx += 1
                        
    nbr = 0
    idx = 0
    for bag in bags:
        #print(idx)
        idx+=1        
        if bag.has_color('shiny gold') == True:
            print(bag.color)
            nbr += 1
        
    print('Answer: ')
    print(nbr-1) 
    
    # not 10
        
#def part1():
##        with open("ex7.txt", "r") as fd:
##        record = fd.read().splitlines() #for lines without the \n after each line
##
#    bags = {}
#    bags['gold'] = 0
#    bags['white'] = ['gold']
#    bags['yellow'] = ['gold']
#    bags['orange'] = ['white', 'yellow']
#    bags['red'] = ['white','yellow']
#    
#    
#    testa nu att skriva ut alla färger!
#        
#def check_bag(color):
#    
#    
#    ... check_bag(color)
  
# basic recursive function
def fakultet(number):
    
    if number == 1:
        return 1
    
    print(number + fakultet(number-1))
    return  number + fakultet(number-1)
    
    
#fac = fakultet(4)
#print(fac)

if __name__ == '__main__':
    
    main()