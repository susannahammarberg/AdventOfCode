# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 15:28:38 2020

@author: Sanna
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 16:37:02 2020

@author: Sanna
"""

import numpy as np

def main():
       
    with open("input4.txt", "r") as fd:
        records = fd.read().split('\n\n') #for lines without the \n after each line

    valid_passports = 0
    
    # p passport
    for p in records:
        print(p)
        print()
        if 'ecl:' in p and 'pid:' in p and 'eyr:' in p and 'hcl:' in p and 'byr:' in p and 'iyr:' in p and 'hgt:' in p:
            print('valid')
            print()
            valid_passports += 1
    print('Answer: ')
    print(valid_passports)

def part2():

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.


    with open("ex_4.txt", "r") as fd:
        records = fd.read().split('\n\n') #for lines without the \n after each line    
    valid_passports = 0
    for p in records:
        print(p)
        print()
        if 'ecl:' in p and 'pid:' in p and 'eyr:' in p and 'hcl:' in p and 'byr:' in p and 'iyr:' in p and 'hgt:' in p:
            if '\n' in p:
                p = p.replace('\n',' ', 1000)
                
            p = p.split(' ')
            
            check = 0
            for things in p:
                mm = things.split(':')
                print('hej')
                print(things.split(':'))
                if mm[0] == 'hcl':
                    if mm[1][0]=='#' and len(mm)==7:
                        for char in k[1][1:]:
                            if char in ['a','b','c','d','e','f'] or char in ['0','1','2','3','4','5','6','7','8','9']:
                                check = 1
                
                
 
            
            print('valid')
            print()
            valid_passports += 1
    print('Answer: ')
    print(valid_passports)

if __name__ == '__main__':
    main()
    #part2()