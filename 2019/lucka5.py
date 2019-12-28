

def read_input():

    with open('input5.txt','r') as f:
        # split up in parts the onvert every straing to int using map
        return map(int, f.read().split(','))


def interpret_opcode(code):
    A = code // 10000 % 10 #governs  ii+3
    B = code // 1000  % 10  # ii+2
    C = code // 100   % 10  #ii+1
    DE = code % 10
    return (A,B,C,DE)

def computer(code, input_val):
    

    ii = 0
    while ii<len(code):


        operation = code[ii]
        print('the instruction before is',operation)
        A, B, C, op = interpret_opcode(code[ii])    
        print('the instruction after is',op)

        if operation == 99:
            print 99
            break;
        
        elif op == 1:
            
            do = code[code[ii+1]] if C == 0 else code[ii+1]
            re = code[code[ii+2]] if B == 0 else code[ii+2]
            
            if A==0: 
                code[code[ii+3]] = do + re
            else:
                code[ii+3]= do + re

            print(code[ii+1],code[ii+2])
            ii +=4
            
        elif op == 2:

            do = code[code[ii+1]] if C == 0 else code[ii+1]
            re = code[code[ii+2]] if B == 0 else code[ii+2]
            if A==0: 
                code[code[ii+3]] = do * re
            else:
                code[ii+3] = do * re      
            ii += 4
            
        elif op == 3:
            code[ code[ii+1]] = input_val
            ii += 2
            
        elif op == 4:
            output_val = code[code[ii+1]] if C == 0 else code[ii+1]#??
            ii += 2

        elif op == 5:
            value = code[code[ii+1]] if C == 0 else code[ii+1]
            if value>0:
                ii = code[code[ii+2]] if B == 0 else code[ii+2]
            else:
                ii += 3
        elif op == 6:
            par1 = code[code[ii+1]] if C == 0 else code[ii+1]
            if par1 == 0:
                ii = code[code[ii+2]] if B == 0 else code[ii+2]
            else:
                ii += 3
        elif op == 7:
            par1 = code[code[ii+1]] if C == 0 else code[ii+1]
            par2 = code[code[ii+2]] if B == 0 else code[ii+2]
            index3 = code[ii+3] if A == 0 else ii+3
            if par1 < par2:
                code[index3] = 1
            else:
                code[index3] = 0
            ii += 4
        elif op == 8:
            par1 = code[code[ii+1]] if C == 0 else code[ii+1]
            par2 = code[code[ii+2]] if B == 0 else code[ii+2]
            index3 = code[ii+3] if A == 0 else ii+3
            if par1 == par2:
                code[index3] = 1
            else:
                code[index3] = 0
            ii += 4
        else:
            print 'something went wrong'
            print code[ii]
       
    return output_val   

def star1():

    # Day 5 input value
    input_val = 1
    code = read_input()
    out = computer(code, input_val = 1)
    print('the output from the computer is',out)

    #1502 too low

    #13285749

def star2():
    code = read_input()
    out = computer(code, input_val = 5)

    print('the output 2 from the computer is',out)
    
def test():
    #code = [1002,4,3,4,33]

    #print computer([3,0,4,33,99],0)
    #print computer([1002,4,3,4,33],0)
    # jump tests
    assert computer([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9],0) == 0
    assert computer([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9],4) == 1

    assert computer([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99],2) == 999
    assert computer([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99],8) == 1000
    assert computer([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99],9) == 1001

        
if __name__=='__main__':

    #star1() # not 1
    star2()
    #test()
    #too low  4880388)

