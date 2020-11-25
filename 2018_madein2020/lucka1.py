import numpy as np

def main():
        
    f = open('input1.txt','r')    
    content = f.readlines()  # for getting a \n after each line

    freq = 0
    for tal in content:
        print( tal)
        i = int(tal)
        freq += i
        print( freq)


def part2():
   
    
    
    #content = [+7, +7, -2, -7, -4]
    f = open('input1.txt','r')    
    content = f.readlines()  # for getting a \n after each line


    freq = 0
    freq_list = []
    
    idx = 0
    while freq not in freq_list:
        
        tal = int(content[idx%len(content)])
     #   print(tal)
        
        freq_list.append(freq)
      #  print(freq_list)
        freq += tal
       # print(freq)
       # print('\n')
        idx += 1
        
    print('Loop ready')
    print(freq)
        
#    lista = [1,2,3]
#    s=0
#    index=0
#    while s<8:
#        print(lista[index  % len(lista)])
#        s+=1
#        index+=1
           

def calc_fuel(tal):
    return int(np.floor(int(tal)/3.0)-2)

def test(tal):
    fuel = int(np.floor(int(tal)/3.0)-2)

    
if __name__ == '__main__':
    #main()
    part2()


    # 3160969 too high

#    test(12)

##    test(0)
##    test(8)
##    test(9)
##    test(10)
#    part2()
