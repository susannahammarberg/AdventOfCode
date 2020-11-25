import numpy as np

def main():
        
    with open("input2.txt", "r") as fd:
        lines = fd.read().splitlines() #for lines without the \n after each line
       
    doubles = 0
    triplets = 0    
        
    for line in lines: 
        print(line)
        
        row_dictionary = {}
        
        for letter in line:
            print(letter) 
            
            # to add an item to a dictionnary, you must initialize it to a value
            if letter not in row_dictionary:
                row_dictionary[letter] = 0

            row_dictionary[letter] += 1
        
        # check for doublets and triplets        
        if 2 in list(row_dictionary.values()):
            doubles += 1
            
        if 3 in list(row_dictionary.values()):
            triplets += 1

    print(doubles)
    print(triplets)        

    print('Answer: ')
    print(doubles*triplets)
#


def part2():
    with open("input2.txt", "r") as fd:
       lines = fd.read().splitlines() #for lines without the \n after each line
   
    #lines = ['abcde', 'xbxxx', 'fghij', 'klmno','abbde','pqrst','fguij']

    while len(lines)>0:           
            for line in lines:        
                check = 0
                idx=0
                
                while check < 2  and idx<len(line):                          
                    #also checks with itself
                    if lines[0][idx] != line[idx]:
                        check+=1
                        
                    if idx==len(line)-1 and lines[0] != line:
                        print('you found the right one')
                        print(lines[0])
                        print(line)
                        print('************')
                    idx+=1
                    
            del lines[0]

    
if __name__ == '__main__':
    #m#ain()
    part2()