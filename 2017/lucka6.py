# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 15:00:26 2017

@author: Sanna
"""
import numpy as np
bank = np.loadtxt('C:/Users/Sanna/Documents/adventofcode2017/input6.txt',dtype='int') 
print(bank[0:6])
#bank = [0, 2, 7, 0]
history = []
#index for 
test_equal=0
#history=np.matrix((4,100))
index=0
while test_equal==0:
    print('Newmaxima')
    print(max(bank))
    print(bank[0:6])
    j=np.argmax(bank)
    steps=max(bank)
    bank[j]=0
    for i in range(steps):
        j+=1
        
        # if you reach the last bank, start om from the beginning
        if j > len(bank)-1:
            j-=len(bank)
        
        bank[j]+=1
        print(bank[0:6])
    print('this is what a append:')
    print(bank[0:6])
    history.append(bank[1:16])
    #history[:,index]=bank
    
    # compare the vectors in the list history
        #compare the alfabet vectors in one row
    
    for ii in range(len(history)):
        for jj in range(len(history)):
            if np.array_equal(history[ii],history[jj]) and ii!=jj:
                test_equal = 1
                print('Equal!')
                print(ii)
                print(jj)
        

