
def star1(noun=12,verb=2):
    

    with open('input2.txt','r') as f:
        # split up in parts the onvert every straing to int using map
        code = map(int, f.read().split(','))


    #restore to "1202 program alarm"
    code[1]= noun
    code[2]= verb 

    #print code
    # instruction pointer
    for ii in range(0,len(code),4):

        if code[ii] == 1:
            #print ('This %d and this %d'%(code[ii+1],code[ii+2]))
            #print ('The numbers in these positions are %d and %d'%(code[code[ii+1]],code[code[ii+2]]))
            # store the following indeces'ss values at the outout
            code[code[ii+3]] = code[code[ii+1]] + code[code[ii+2]]
        elif code[ii] == 2:
            code[code[ii+3]] = code[code[ii+1]] * code[code[ii+2]]
        elif code[ii] == 99:
            #print 99
            break;
        else:
            print 'something whent wrong'
            print code[ii]
            
    #print code
    #print 'last is the code\n'
    return code[0]

def star2():
    for noun in range(0,99):
        for verb in range(0,99):
            code0 = star1(noun,verb)
            if code0==19690720:
                print 'found it!'
                print code0
                print 'noun and ver'
                print noun
                print verb
                break;
        
    
def test1(code = [1,1,1,4,99,5,6,0,99]):
     #[1,9,10,3,2,3,11,0,99,30,40,50]
    print code
    for ii in range(0,len(code),4):
        if code[ii] == 1:
            print ('This %d and this %d'%(code[ii+1],code[ii+2]))
            print ('The numbers in these positions are %d and %d'%(code[code[ii+1]],code[code[ii+2]]))
            # store the following indeces'ss values at the outout
            code[code[ii+3]] = code[code[ii+1]] + code[code[ii+2]] 
        elif code[ii] == 2:
            code[code[ii+3]] = code[code[ii+1]] * code[code[ii+2]]

        elif code[ii]==99:
            print 99
            break;
        else:
            print 'something whent wrong'
            print code[ii]

            
    print code

        
if __name__=='__main__':

    star1() # not 1
    test1([1,0,0,0,99])
    test1(code=[2,4,4,5,99,0])
    star2()
