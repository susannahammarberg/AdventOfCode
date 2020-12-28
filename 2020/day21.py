# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 07:58:09 2020

@author: Sanna
"""

import copy

with open("ex21.txt", "r") as fd:
    record = fd.read().splitlines()
    

#restructure data    
rec = []
for line in record:
    temp = [0]*2
    temp[0]=(line.split(' (contains ')[0].split(' '))
    temp[1] = (line.split(' (contains ')[1].replace(')','').split(','))
    rec.append(temp)

#om 2st ingrediennter överenstämmer, men inga andra då har man hittat en ingrediens
#då kan man ta bort den från båda ingrediens och allergen listan

 

                
row0 = rec[0]                
#alle = 'dairy' # first row
for ii in range(1,len(rec)):
    row = rec[ii]
    for alle in row[1]:
        print(alle)
        #now you know that allergen word match, now compare the other words
        #check for singular match!
        match = 0 
        #TODO kolla into mot sig själv
        
        for index, words in enumerate(row[0]):
            #check against all other rows
            for ii in range(1,len(rec)):
                line = rec[ii][0]
                for jj,words2 in enumerate(line):
                    if words == words2 and ii != jj:
                        match += 1
                        print('Match!', words)
                        print('For line ' + str(ii) + ' and ' + str(jj)  )
                        del_word = copy.deepcopy(words)
        print(match)
        if match == 1:
            # now you know what this word is so you can remove it from every row
            # maybe some easy way?
            
            for row in rec:
                if del_word in row[0]:
                    print('deleted')
                    row[0].remove(del_word)
                
        