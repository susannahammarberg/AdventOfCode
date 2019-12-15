import numpy as np

def star2():
    linked_list = []
    with open('input6.txt','r') as f:
        for line in f:
            linked_list.append(line.rstrip('\n').split(')'))
    #print linked_list

    test = 0
    orbits = 0
    # look for ends of list (entry found in column 1 but not 0)
    #while len(linked_list)>1:
    my_list = []
    san_list = []
    for elementL in linked_list:
        pek = elementL[1]
        if pek == 'YOU':
            #print elementL
            while pek != 'COM':
                pek = find_pointer(pek,linked_list)
                my_list.append( pek)
        elif pek == 'SAN':
            while pek != 'COM':
                pek = find_pointer(pek,linked_list)
                san_list.append( pek)            
        

    
#    print my_list
#    print san_list

    same = 0
    
    for item in my_list:
        for item2 in san_list:
            if item ==item2:
                a = my_list.index(item)
                b= san_list.index(item2)
                same = 1
                break
            if same == 1:
                break
        if same == 1:
            break
    

    kk = a + b
    print kk
                
            
        
    

def main():
    linked_list = []
    with open('input6.txt','r') as f:
        for line in f:
            linked_list.append(line.rstrip('\n').split(')'))
    #print linked_list



    test = 0
    orbits = 0
    # look for ends of list (entry found in column 1 but not 0)
    while len(linked_list)>1:
        for elementL in linked_list:
            test=0
            for elementR in linked_list:
                if elementL[1] == elementR[0]:
                    test = 1
            if test == 0:
                #print 'this is an end of a branch'
                #print elementL
                # start counting orbits
                pek = elementL[1]
                while pek != 'COM':              
                    pek = find_pointer(  pek,linked_list)
                    #print 'it is pointing to'
                    #print pek
                    orbits +=1
                    #print linked_list
                    #print elementL
                    #if nothing is pointing to it, remove it
                linked_list.remove(elementL)


    print 'orbits'
       
    print orbits + 1
    print linked_list
# for a given index. find the index inhe linked list and return the other value

def find_pointer(find_item,linked_list):
    for item in linked_list:
        if item[1] == find_item:
            return item[0]
        
def arit_sum(series):
    return len(series)*(series[0]+series[-1])/2
    

if __name__=='__main__':

    star2()
    #main()
    #correct! 160040
