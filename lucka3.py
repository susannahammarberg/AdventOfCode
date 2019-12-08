
def star1():
    

    with open('input3.txt','r') as f:
        # split up in parts the connvert every straing to int using map
        code = f.readlines()
        code1 = code[0].split(',')
        code2 = code[1].split(',')
        
        wire1_position = move(code1)
        wire2_position = move(code2)

        # check for overlap of coordinates
        inters = find_intersection(wire1_position,wire2_position)

        # calculate the Manhattan distances of itnersections
        distances = []
        for inter in inters:
            distances.append(calc_distance(inter))
        #print distances
        # find the smalles distance excluding origin
        print min(distances[1:])

def star2():

    with open('input3.txt','r') as f:
        # split up in parts the connvert every straing to int using map
        code = f.readlines()
        code1 = code[0].split(',')
        code2 = code[1].split(',')
        
        wire1_position = move(code1)
        wire2_position = move(code2)

        print 'this'

        print len(wire1_position)
        # check for overlap of coordinates
        inters = find_intersection(wire1_position,wire2_position)

        # calculate the total nbr of steps to intersections
        steps = []
        for inter in inters:
            print 'intersection'
            steps.append(wire1_position.index(inter) + wire2_position.index(inter))
        print steps
        # find the smalles distance excluding origin
        print min(steps[1:])

            

def calc_distance(coord=[2,3]):
    return abs(coord[0])+abs(coord[1])


def move(code = ['R8','U5','L5','D3']):

    # Up is positive in y. Right is positive in x.
    # (x,y)
    coord = [[0,0]]
    for item in code:
#        print item
        if item[0] == 'U':
            for ii in range(0,int(item[1:])):
                coord.append( [coord[-1][0], coord[-1][1] + 1] )
        elif item[0] == 'D':
            for ii in range(0,int(item[1:])):
                coord.append( [coord[-1][0], coord[-1][1] - 1] )           
        elif item[0] == 'R':
            for ii in range(0,int(item[1:])):
                coord.append( [coord[-1][0] + 1, coord[-1][1] ] )
        elif item[0] == 'L':
            for ii in range(0,int(item[1:])):
                coord.append( [coord[-1][0] - 1, coord[-1][1] ] )
        else:
            print 'someting went wrong'
    return coord

def find_intersection(coord1,coord2):
    intersection=[]
    print len(coord1)
    for indx in range(0,len(coord1)/10):
        for item in coord2:
            #check if coord exists in list2
            if coord1[indx] == item:
                print 'hello'
                intersection.append(coord1[indx])
                # or save the indices here
                
    return intersection
    
def test1():
    coord1 = move(['R8','U5','L5','D3'])
    coord2 = move(['U7','R6','D4','L4'])
    print coord1
    print coord2
    # check for overlap of coordinates
    inters = find_intersection(coord1,coord2)
    print inters
    # calculate the Manhattan distances of itnersections
    distances = []
    for inter in inters:
        distances.append(calc_distance(inter))
    print distances
    # find the smalles distance excluding origin
    print min(distances[1:])

def test2(a=['R8','U5','L5','D3'],b=['U7','R6','D4','L4']):
    coord1 = move(a)
    coord2 = move(b)
    print coord1
    print coord2
    # check for overlap of coordinates
    inters = find_intersection(coord1,coord2)
    print inters
    # calculate the total nbr of steps to intersections
    steps = []
    for inter in inters:
        print 'he'
        steps.append(coord1.index(inter) + coord2.index(inter))
    print steps
    # find the smalles distance excluding origin
    print min(steps[1:])  
    
if __name__ == '__main__':

    #test2()
    #star1()
    #calc_distance()
    #test1()
    #test2(['R75','D30','R83','U83','L12','D49','R71','U7','L72'],['U62','R66','U55','R34','D71','R55','D58','R83'])
    star2()
    test2(map(str,[R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51],[
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7]))
