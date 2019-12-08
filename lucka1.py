import numpy as np

def main():
        
    f = open('input1.txt','r')    
    content = f.readlines()  # for getting a \n after each line

    fuel = 0
    for tal in content:
        print tal
        i = int(tal)
        fuel += int(np.floor(int(tal)/3.0)-2)

        print fuel


def part2():
    f = open('input1.txt','r')    
    content = f.readlines()  # for getting a \n after each line

    fuelsum = 0
    for tal in content:
        
        while tal > 8:
            tal = calc_fuel(tal)
            fuelsum += tal
    print fuelsum

def calc_fuel(tal):
    return int(np.floor(int(tal)/3.0)-2)

def test(tal):
    fuel = int(np.floor(int(tal)/3.0)-2)

    print fuel
    
def test2(tal = 14):

    fuelsum = 0
    
    print 'tal is'
    print tal
    while tal > 8:       
        tal = calc_fuel(tal)
        print tal
        fuelsum += tal
    print '\n'
    print fuelsum

    
if __name__ == '__main__':
    main()


    # 3160969 too high

    test(12)
    test(14)
    test(1969)
    test(100756)
    test2(1969)
    test2(100756)
##    test(0)
##    test(8)
##    test(9)
##    test(10)
    part2()
