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
    """
    acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
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
    data = []
    for dat in test_data:        
        data.append(dat.split('|'))
           
    return data

#data = read_input()
data = read_test()

def extract_output_values(data):
    output = []
    for dat in data:
        output.append(dat[1][1:].split(' '))
    return output

output = extract_output_values(data)


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
        j=5
        numbers.append(code)
        
        
         

    return numbers
        
decoded = decode_easy_digits(output) 


   
print('\n' + 'result part 2: ',decoded )

