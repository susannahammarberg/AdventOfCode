# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 13:13:17 2020

@author: Sanna
"""

import numpy as np

#
#class Bag:  
#    
#    def __init__(self,color):
#        self.color = color
#        self.children = []
#        
#    def has_color(self,color):
#        #print(self.color)
#
#        if color == self.color:
#            return True
#        
#        if len(self.children) == 0:
#            return False
#
#        else:
#            for child in self.children:
#                #if flagga !=0:
#                if child.has_color(color):
#                    return True
#                
#        return False




class Bag:  
    
    def __init__(self, color):
        self.color = color
        self.children = []
        self.nbr_children = [] 
        
    def has_color(self,color):

        if color == self.color:
            return True
        
        if len(self.children) == 0:
            return False

        else:
            for child in self.children:
                if child.has_color(color):
                    return True
                
        return False
    
    def all_colors(self):
        
        if len(self.children) == 0:
            return self.color

        l = ' '
        for child in self.children:
            l += ' ' + child.all_colors()
        
        return self.color + ' ' + l 

   
    def nbr_bags(self):
             
        if len(self.children) == 0:
            return 1
       
        idx = 0 
        ll = 1 #current bag
        for child in self.children:
          
            ll +=   child.nbr_bags() *self.nbr_children[idx]
            idx += 1

        return   ll
        

    
    
def main():


    #ex2_day       
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
                    daughter_color = ' '.join(item.split(' ')[-3:-1])
                    daughter_number = int(item.split(' ')[-4])

                    for bag in bags:
                        if bag.color == daughter_color:
                            b3.children.append(bag)
                            b3.nbr_children.append(daughter_number)
                    
            else:
                
                for bag in bags:
                    daughter_color = ' '.join(line.split(' ')[-3:-1])
                    daughter_number = int(line.split(' ')[-4])
                    if bag.color == daughter_color:
                        b3.children.append(bag)
                        b3.nbr_children.append(daughter_number)
                                
        idx += 1
                        



    nbr = 0
    idx = 0
    for bag in bags:
        #print(idx)
        idx+=1    
        #for items in
        if bag.has_color('shiny gold') == True:
            print(bag.color)
            nbr += 1
        
    print('Answer del I: ')
    print(nbr-1) 
    
    # part 2
    
    
    for bag in bags:
   
        if bag.color == 'shiny gold':
            nbr_bags  = bag.nbr_bags()      
            
            print(nbr_bags-1)
            
            #5883833 too high
            
    
    
    
        
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