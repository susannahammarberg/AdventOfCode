# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 12:21:21 2017

@author: HonkyT

Find same words in text
"""
import numpy as np
#STAR 1
file1=open('C:/Users/Sanna/Documents/adventofcode2017/input4.txt','r')#.read()
##a list of the lines: are there dublicates or not
#lista=[]
#counts={}
#count_words=0
## for every line in the text
#for line in file1:
#    print('one row:')
#    print(line)
#    doublets_in_oneline=0
#    # for every word in that line (split line into words)
#    # OBS this is overly complicated!
#    
#    for word in line.split():
#        count_words+=1 
#        
#        for word2 in line.split(): #not in counts:
#            if word==word2:
#                doublets_in_oneline+=1
#    
#    # remove the number of counts that should exist (dependent on the nuber of word in one line)    
#    doublets_in_oneline -= count_words    
#            
#        # the lista will have
#        # one value for each line
#        # if it is above 0 then there are duoblets
#    lista.append(doublets_in_oneline)    
#    count_words=0
#
## done. 
##now how many 0 are there in the lista
#lista.count(0)
#STAR 2

count_valids = 0
alfabet = 'abcdefghijklmnopqrstuvxyz'
for line in file1:
    alfabet_vectors_one_line = []
    nbr_words = 0
    for word in line.split():
        print(word)
        alfabet_vector = np.zeros(25) # one for each word
        
        for letter in word:
                
            # hitta vilken plats i alfabetet som bokstaven har
            index = alfabet.find(letter)
            alfabet_vector[index] +=1
            
        print(alfabet_vector)    
        # when alfabet vector is ready, put it in a list
        alfabet_vectors_one_line.append(alfabet_vector)
    
    test_equal = 0
    #compare the alfabet vectors in one row
    for i in range(len(alfabet_vectors_one_line)):
        for j in range(len(alfabet_vectors_one_line)):
            if np.array_equal(alfabet_vectors_one_line[i],alfabet_vectors_one_line[j]) and i!=j:
                test_equal = 1
                print('Equal!')
    #when it is done comparing all words in one row, check it test_equal is 0 or 1
    if test_equal == 0:
        count_valids+=1     



##This is just atest of something else
#a = np.array([[1,2,3],[4,3,1]])
#a.argmax()
#try:
#    something
#except:
#    pass