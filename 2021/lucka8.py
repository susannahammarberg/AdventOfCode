# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 10:49:12 2023

@author: sanna
"""

def read_input():
    
    with open('input8.txt','r') as fp:
        info = fp.read().splitlines()
        data = []
        for dat in info:        
            data.append(dat.split('|'))
        #info = f.readlines()
    return data

def read_test():    
    test_data = [
    #acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf 
    """
    be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
    edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
    fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
    fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
    aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
    fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
    dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
    bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
    egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
    gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""]

    
    test_data = test_data[0].split('\n')[1:] # same as splitlines
    output_data = []
    for dat in test_data:        
        output_data.append(dat.split('|'))
           
    return output_data

#data = read_input()
data = read_test()

#TODO
#Dort input values acc to length
def extract_input_output_values(data):
    output = []
    input_ = []
    for dat in data:
        input_.append(dat[0][4:-1].split(' '))
        output.append(dat[1][1:].split(' '))
    return input_, output

input_, output = extract_input_output_values(data)


# part 1

"In the output values, how many times do digits 1, 4, 7, or 8 appear?" 

def decode_easy_digits(output):
    code = []
    for data in output:
        for dat in data:
            length = len(dat)
            if length == 2:
                code.append(1)
            elif length == 4:
                code.append(4)
            elif length == 3 :
                code.append(7)
            elif length == 7:
                code.append(8)

    return code
        
decoded = decode_easy_digits(output)    

# output = after "|"
print('\n' + 'result part 1: ',len(decoded) )



#part 2 
"""
you now have this decoding pattern:

acedgfb: 8
cdfbe: 5
gcdfa: 2
fbcad: 3
dab: 7
cefabd: 9
cdfgeb: 6
eafb: 4
cagedb: 0
ab: 1
"""


def sort_string(string):
    return "".join(sorted(string))

for inp in input_:
    inp.sort()

two_code = sort_string('gcdfa')
three_code = sort_string('fbcad')   
five_code = sort_string('cdfbe')
six_code = sort_string('cdfgeb')
nine_code = sort_string('cefabd')

def decode_easy_digits(output):
    numbers = []
    
    for data in output:
        code = []
        for dat in data:
            length = len(dat)
            dat = sort_string(dat)
            if length == 2:
                code.append(1)
            elif dat == two_code:
                code.append(2)
                print('two')
            elif dat == three_code:
                code.append(3)
            elif length == 4:
                code.append(4)
            elif dat == five_code:
                code.append(5)
            elif dat == six_code:
                code.append(6)
            elif length == 3:
                code.append(7)
            elif length == 7:
                code.append(8)
            elif dat == nine_code:
                code.append(9)
            else:
                print('could not decode')
        code = str(code).replace(', ','').strip('[').strip(']')
        numbers.append(code)

    return numbers

# use this as a guide
"""
   aaaa
b       c
b       c
   dddd
e       f
e       f
   gggg
   
 """
 
def decode_input(data):

    #sort the input values after lenngth
    data = sorted(data, key=len)
    code = []
    for dat in data:
        length = len(dat)
        dat = sort_string(dat)
        
        if length == 2: #then == '1'
            code.append(1)
            # save the information that these two letters
            # encodes the two diodes to the right (c and f)
            # save the 2 letters that coresponds to c and f
            cf_save = dat

        
        elif length == 3:
            code.append(7)
            # the letter that is not included in "1" is the top diod (a)

            # it is not the dat[2] that equals the a, it is the one that is different from 2 but it could be the dirst letter
            a_save = dat.replace(cf_save[0],'').replace(cf_save[1],'')

        
        elif length == 4:
            code.append(4)
            # save the diodes that are not included in '1'
            bd_save = dat.replace(cf_save[0],'').replace(cf_save[1],'')
                
        elif length == 5:
            
            #if the letters cf_sSave exist in dat:
            #(    that is, if the length of dat is 3 when cf is removed)
            if len(dat.replace(cf_save[0],'').replace(cf_save[1],'')) == 3:
                code.append(3)
            #elif bd from 4 exist in dat:
            elif len(dat.replace(bd_save[0],'').replace(bd_save[1],'')) == 3:
                code.append(5)
            else:
                code.append(2)
        
        elif length == 6:
            #todo wrong i thing indeces in dat
            dat = dat.replace(cf_save[0],'').replace(cf_save[1],'')
            if len(dat) == 4:
                #check if 0 or 9
                dat = dat.replace(bd_save[0],'').replace(bd_save[1],'')
                if len(dat) == 2:
                    code.append(9)
                else: #(if that thing is 3)
                    code.append(0)
                
            else: # (if that thing ==5)
                code.append(6)
        
        elif length == 7:
            code.append(8)
            
        else:
            print('could not decode')
    
        
        #code = str(code).replace(', ','').strip('[').strip(']')


    return code, a_save, bd_save, cf_save

#
def decode_output(data, a_save, bd_save, cf_save):

    #this time dont sort the values, they must be in the 
    # right order to produce the right number
    #data = sorted(data, key=len)
    code = []
    for dat in data:
        length = len(dat)
        dat = sort_string(dat)
        
        if length == 2:
            code.append(1)
       
        elif length == 3:
            code.append(7)
        
        elif length == 4:
            code.append(4)
             
        elif length == 5:            
            #if the letters cf_sSave exist in dat:
            #(    that is, if the length of dat is 3 when cf is removed)
            if len(dat.replace(cf_save[0],'').replace(cf_save[1],'')) == 3:
                code.append(3)
            #elif bd from 4 exist in dat:
            elif len(dat.replace(bd_save[0],'').replace(bd_save[1],'')) == 3:
                code.append(5)
            else:
                code.append(2)
        
        elif length == 6:
            #todo wrong i thing indeces in dat
            dat = dat.replace(cf_save[0],'').replace(cf_save[1],'')
            if len(dat) == 4:
                #check if 0 or 9
                dat = dat.replace(bd_save[0],'').replace(bd_save[1],'')
                if len(dat) == 2:
                    code.append(9)
                else: #(if that thing is 3)
                    code.append(0)
                
            else: # (if that thing ==5)
                code.append(6)
        
        elif length == 7:
            code.append(8)
            
        else:
            print('could not decode')

    return code

outputs = []
for ii in range(0,len(output)):

    decoded_input, a_save, bd_save, cf_save = decode_input(input_[ii]) 

    decoded_output = decode_output(output[ii], a_save, bd_save, cf_save )
    outputs.append(str(decoded_output).replace(', ','').strip('[').strip(']'))
    
    
outputs = [int(out) for out in outputs]
   
print('\n' + 'result part 2: ',sum(outputs))

