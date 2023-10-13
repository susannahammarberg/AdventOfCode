# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 10:49:12 2023

@author: sanna
"""


import numpy as np

def read_input():
    
    with open('input4.txt','r') as fp:
        #info = fp.read().splitlines()
        #dont wanna split the bingo cards up
        info = fp.read().splitlines()
        #info = f.readlines()
    return info

def read_test():    
    test_data = [
    """
    7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1
    
    22 13 17 11  0
     8  2 23  4 24
    21  9 14 16  7
     6 10  3 18  5
     1 12 20 15 19
    
     3 15  0  2 22
     9 18 13 17  5
    19  8  7 25 23
    20 11 10 24  4
    14 21 16 12  6
    
    14 21 17 24  4
    10 16 15  9 19
    18  8 23 26 20
    22 11 13  6  5
     2  0 12  3  7
    """]
    test_data = test_data[0].split('\n') # same as splitlines
    return test_data[1:-1]



data = read_input()
#data = read_test()
callout = data[0]
callout = [int(x) for x in callout.split(',')]

data = [row.strip().split(' ') for row in data]

#%%
## ta bort de tomma
for row in data:
    while len(row) > 5:
        row.remove('')

#%%
cards = []
 
x = 2         
while x < len(data)-4: #typ
    cards.append(np.array(data[x:x+5], dtype=int))
    x += 6   
    
    
# input data  sorted

#%%
# part 1
def play_bingo():
    found_bingo = False
    for num in callout:
    
        for card in cards:
            card[card == num] = 100
            
            for col_sum in np.sum(card,axis=0):
                if col_sum == 500:
                    print('col bingo!!')
                    found_bingo = True
                    break
            for row_sum in np.sum(card,axis=1):
                if row_sum == 500:
                    print('row bingo!!')
                    found_bingo = True
                    break
    
            if found_bingo == True:
                break
        if found_bingo == True:
            break
    
    return card,num
    
card, num = play_bingo()
#set all the callouted numberes to 0
card[card==100] = 0 

sum_ = np.sum(card)    
    
score = num * sum_

   
print('result part 1: ', score)

#%%
#part 2
def play_bingo_again():
    remove_card_nbrs = []
    for num in callout:
        found_bingo = False   
        for count, card in enumerate(cards):
            card[card == num] = 100
            
            for col_sum in np.sum(card,axis=0):
                if col_sum == 500:
                    print('col bingo!!')
                    found_bingo = True
                    remove_card_nbrs.append(count)
                    break
            for row_sum in np.sum(card,axis=1):
                if row_sum == 500:
                    print('row bingo!!')
                    found_bingo = True
                    remove_card_nbrs.append(count)
                    break

        #if one card had bingo, remove it from the deck, if its not the last one
        if found_bingo == True and len(cards) > 1:      
            #reverse the order so its easier to remove from the deck   
            remove_card_nbrs.reverse()
            for rem_nbr in remove_card_nbrs:
                cards.pop(rem_nbr)
            # set found_bingo to false so that the game continues when
            # a card/cards are chucked out
            found_bingo = False 
            remove_card_nbrs = []
                
        #Stop going thourgh the numbers when the last card has got a bingo!
        if len(cards) < 2 and found_bingo == True:
            break
    
    return card,num
    
card, num = play_bingo_again()
#so if the card wins, you delete it or set everything to 0 or something

# #set all the callouted numberes to 0
card[card==100] = 0 

sum_ = np.sum(card)    
    
score = num * sum_
print('result part 2: ', score )


