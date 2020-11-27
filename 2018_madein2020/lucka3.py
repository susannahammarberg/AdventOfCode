import numpy as np

def main():
       
    #row,col
    fabric = np.zeros((1000,1000))
    with open("input3.txt", "r") as fd:
        claims = fd.read().splitlines() #for lines without the \n after each line
    #claims =['#1 @ 1,3: 4x4','#2 @ 3,1: 4x4','#3 @ 5,5: 2x2'  ] 
            
             
    #loop claim
    for claim in claims:
        a = claim.split('@')
        b = a[1].split(':')
        place = b[0].split(',')
        col_pos = int(place[0])
        row_pos = int(place[1])
        size = b[1].split('x')
        width = int(size[0])
        height = int(size[1])
        fabric[row_pos:row_pos + height, col_pos:col_pos+width ] += 1

    print(fabric)
    
    #occurrences of overlapping squares
    overlap = np.count_nonzero(fabric > 1)
     
    
    print('Answer: ')
    print(overlap)

def part2():

    #row,col
    fabric = np.zeros((1000,1000))
    #IDs = np.zeros((1000,1000))
    #2D list
    n = 1000
    m = 1000
    IDs = [[''] * n for i in range(m)]
    
    with open("input3.txt", "r") as fd:
        claims = fd.read().splitlines() #for lines without the \n after each line
    #claims =['#1 @ 1,3: 4x4','#2 @ 3,1: 4x4','#3 @ 5,5: 2x2'  ] 

    
    #loop claim
    for claim in claims:
        a = claim.split('@')
        ID = int(a[0].split('#')[1])
        b = a[1].split(':')
        place = b[0].split(',')
        col_pos = int(place[0])
        row_pos = int(place[1])
        size = b[1].split('x')
        width = int(size[0])
        height = int(size[1])
        fabric[row_pos:row_pos + height, col_pos:col_pos+width ] += 1
        
        #dont know hot do do this with slicing.. so just usa a loop
        for row in range(row_pos,row_pos+height):
            for col in range(col_pos,col_pos+width):
                if IDs[row][col] == '':
                    IDs[row][col] += str(ID)
                else:    
                    IDs[row][col] += '_'
                    IDs[row][col] +=  str(ID)
     
    doublets = []
    print(1) 
    for row in range(0,n):
        for col in range(0,m):
            if '_' in IDs[row][col]:
                doublets.extend(IDs[row][col].split('_'))
    print(2)
    
    
    # ta bort dubletter i doublets
    for row in range(0,n):
        for col in range(0,m):                
            if '_' not in IDs[row][col] and IDs[row][col] != '':
                if IDs[row][col] not in doublets:
                    print(IDs[row][col])
                 
    
    print('Answer: ')
   
if __name__ == '__main__':
    #main()
    part2()