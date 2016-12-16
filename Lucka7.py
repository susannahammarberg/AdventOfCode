# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 15:58:31 2016

@author: HonkyT
"""
import re
import string
alfabet = list(string.ascii_lowercase[:26])

testData = 'wysextplwqpvipxdv[srzvtwbfzqtspxnethm]syqbzgtboxxzpwr[kljvjjkjyojzrstfgrw]obdhcczonzvbfby[svotajtpttohxsh]cooktbyumlpxostt'
#två likadana bokstäver: (.)\1{1}
#dela up inside and outside [] vartannat index i vektorn lines:
lines = [re.split(r'\[([^\]]+)\]', line) for line in open('dataLucka7.txt')]
     #match isf search: då börjar den bara titta i början avstringen    
obj = re.search(r'(.)\1{1}',str(lines[0]))
#save the index of the pair (the pairs placement in the string list)
placement = obj.start()
#look for which letter has been found to be in a pair
dubletter = obj.group(1)
# check what index the letter has in the alphabet
index = alfabet.index(dubletter)
# check if the pair is souranded by the letter that comes before in alphabet
#gör först for loopen
print(index)