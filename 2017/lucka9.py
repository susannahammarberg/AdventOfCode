# -*- coding: utf-8 -*-
"""
Created on Mon Jan 01 18:43:23 2018

@author: Sanna
"""
import numpy as np
data = open('C:/Users/Sanna/Documents/Github/adventofcode/2017/input9.txt',"r")
data_str = data.read()
data = data_str
#data = '{{<!!>},{<!>},{<!>},{<a>}}'
#data = '{{<!k>}{{<zs>}}}'
#data = '{{<a!>},{<a!>},{<a!>},{<ab>}}'
#data = '<{o"i!a,<{i<a>'
prev_letter = 'a'
garbage_letters = 0
points = 0
left_brac = 0
left_garb = 0
print '\n This is the data: '
print data

inside_garbage = False

for letter in data:

    # brja med att fixa så att bokstaven efte r! inside garbage ignoreras
    print 'Letter: ' + letter

    if prev_letter == '!' and inside_garbage == True:
        print 'This letter is ignored \n'
        prev_letter = letter
        if letter == '!':
            #dont save ! as previous letter when is 2 in a row
            prev_letter = 0
        # then abort this iteration
        continue

        # count the number of non-cancelled letter inside garbage
        # keep sats here to not capture letters '<' that opens garbage
    if inside_garbage == True and letter != '>' and letter != '!':
        
            # dont count the letters < that opens the garbage
         #   pass
        #else:
        garbage_letters +=1
        print 'Counting this as garbage letter'

    
    if letter == '<' and inside_garbage==False:
        
        print 'Found a garbage bracket. The following caracters should be ignored, until a rght garbage bracket comes'
        inside_garbage = True
        # exit this loop and this iteration. It works!
        #continue   # but it does not matter if I have this or not!
        # acctually should not have if because this letter should be saved as 'precious letter' in the en of the iteration

    if letter == '>':
        # closing the garbage
        inside_garbage = False
    if letter == '{' and inside_garbage == False:
        print 'We have a { and we are not inside garbage'
        left_brac += 1

    # this is just a bugtest. remove later
    if letter == '{' and inside_garbage == True:
        print 'test'
   
    if letter == '}' and left_brac > 0 and inside_garbage == False: #2nd statement unessessary because there will always be1 except for very first letter
        print( ' A ''group'' (bracket pair) is formed and ' +str(left_brac) + ' points are added to the score\n ')
        print 'The nbr of point should be equal to the number of open left square brackets'
        points += left_brac
        left_brac -= 1



    prev_letter = letter
    
print '\nTotal score is: '        
print(points)

print '\n The number of letters inside garbage is: ' + str(garbage_letters)
    


