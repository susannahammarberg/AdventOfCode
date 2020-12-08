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
        print(self.color)

        if color == self.color:
            return True
        elif len(self.children) == 0:
            print('does this happen???????????????????????????????')
            return False
        else:
            for child in self.children:
                print('but this works?')
                return child.has_color(color)


bg = Bag('gold')
print(bg.children)
b1 = Bag('white')
print(bg.children)
b1.children.append(bg)
print(bg.children)

b2 = Bag('yellow')
b2.children.append(bg)    
b3 = Bag('orange')
b3.children.append(b1)
b3.children.append(b2)
b4 = Bag('red')
b4.children.append(b1)
b4.children.append(b2)

b1.has_color('white')
b1.has_color('gold')
b1.has_color('green')

def main():
       
    with open("ex7.txt", "r") as fd:
        record = fd.read().splitlines() #for lines without the \n after each line


    
    for line in record:
        
        parent_color = line.split(' ')[1]
        print('new color')
        print(parent_color)
        if not 'no other' in line:
            daughter_colors = []
            
            #TOdo fix this!!!!!rfcghn b
            
            if ',' in line: 
                line = line.strip('s.')
                for item in line.split('bag')[1:-1]:
                    print('daughters')
                    print(item.split(' ')[-2])
                    #daughter_colors.append(item.split(' ')[-2])

                    
            else:
                print(record[2].split(' ')[-2])
                print(' huhuhu')
                    
                #daughter_colors.append()
                #print(item)
            


    bags = []
    
    bg = Bag('gold')
    b1 = Bag('white')
    b1.children.append(bg)
    
    b2 = Bag('yellow')
    b2.children.append(bg)    
    b3 = Bag('orange')
    b3.children.append(b1)
    b3.children.append(b2)
    b4 = Bag('red')
    b4.children.append(b1)
    b4.children.append(b2)
    bags.append(bg)
    bags.append(b1)
    bags.append(b2)
    bags.append(b3)
    bags.append(b4)
    nbr = 0
    for bag in bags:
        print(bag.has_color('gold'))
        nbr += 1
        
    print('Answer: ')
    print(nbr-1)
        
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
    
    
fac = fakultet(4)
print(fac)

if __name__ == '__main__':
    
    main()