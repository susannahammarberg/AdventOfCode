from itertools import permutations


# amplifier should halt when its lacking an input



" obs, based on day 5 "
def read_input():

    with open('input9.txt','r') as f:
#         split up in parts the onvert every straing to int using map
#         add bigger memory with " + [0]*500"
        return map(int, f.read().split(',')) + [0]*500
    #return [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]


    #9
    #return [104,1125899906842624,99] + [0]*500
    #return [1102,34915192,34915192,7,4,7,99,0]+ [0]*500

    #return [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]  + [0]*500
   
def interpret_opcode(code):
    A = code // 10000 % 10 #governs  ii+3
    B = code // 1000  % 10  # ii+2
    C = code // 100   % 10  #ii+1
    DE = code % 10
    return (A,B,C,DE)


class Amplifier:

    def __init__(self):        
        self.code = read_input() #obs, not text file
        self.phase = 0
        self.input_ = 0
        self.input_iter = 0
        self.inst_pointer = 0
        self.output_val = 0
        
#    def set_phase(self,value):
#        self.phase = value
        
    def set_input(self,value):
        self.input_ = value 
        
    def get_input(self):
        
        return self.input_
#        
#        if self.input_iter == 0:
#            input_ = self.phase
#            self.input_iter = 1
#        elif self.input_iter == 1:
#            input_ = self.input_
#            #self.input_iter = 0
#        else:
#            print 'someting whent wrong 2'      
#        return input_
     
    def computer(self):  
        ii = 0#self.inst_pointer
        code = self.code
        finished = 0
        
        rel_base = 0
        print code
        
        while ii<len(code):
            #print('index', ii)
            operation = code[ii]
            A, B, C, op = interpret_opcode(code[ii])  
            
            #print operation
            
            if C == 0:
                indx1 = code[ii+1]
            elif C == 1:
                indx1 = ii+1
            else:
                indx1 = code[ii+1] + rel_base        
                
            if B == 0:
                indx2 = code[ii+2] 
            elif B==1:
                indx2 = ii+2 
            else:
                indx2 = code[ii+2] + rel_base  # or + rel base inside?
                          
            if A == 0:
                indx3 = code[ii+3] 
            elif A == 1:    
                indx3 = ii+3
            else:
                indx3 = code[ii+3] + rel_base
            #print('operation',operation)
            if operation == 99:
                self.inst_pointer = 0 
                finished = 1
                ii = len(code)+1
                break;          

            elif op == 1:            
                param1 = code[indx1]
                param2 = code[indx2]                
                code[indx3] = param1 + param2
                ii +=4
            
            elif op == 2:  
                param1 = code[indx1]
                param2 = code[indx2]               
                code[indx3] = param1 * param2
                ii += 4
                
            elif op == 3:
                #code[ code[ii+1]] = self.get_input()
                code[indx1] = self.get_input()
                ii += 2
                
            elif op == 4:
                self.output_val = code[indx1]
                print('output from 4',code[indx1])
                ii += 2
                #self.inst_pointer = ii
                   
            elif op == 5:
                value = code[indx1]
                if value > 0:
                    ii = code[indx2]
                else:
                    ii += 3
                    
            elif op == 6:
                par1 = code[indx1]
                if par1 == 0:
                    ii = code[indx2]
                else:
                    ii += 3
                    
            elif op == 7:
                par1 = code[indx1]
                par2 = code[indx2]
                if par1 < par2:
                    code[indx3] = 1
                else:
                    code[indx3] = 0
                ii += 4
                
            elif op == 8:
                par1 = code[indx1]
                par2 = code[indx2]
                if par1 == par2:
                    code[indx3] = 1
                else:
                    code[indx3] = 0
                ii += 4
                
            elif op == 9:          
                rel_base += code[indx1]
                #print('Changing the relative base',rel_base)
                ii += 2
                
            else:
                print 'something went wrong'
            #print('code', code)
        self.code = code             
        return (self.output_val,code)   

def star1(): 
    ampA = Amplifier()     
    ampA.set_input(1)
    out,code = ampA.computer()
    print('OUTPUT IS', out)
    
    #print('output code is:', code)

    # CORRECT: 2594708277L
    
    # 203 TOO LOW
    
def star2():

    ampA = Amplifier()     
    ampA.set_input(2)
    out,code = ampA.computer()
    print('OUTPUT IS', out)
    
def test():
    
    ampA = Amplifier()
    out, code = ampA.computer()
    #code = [1002,4,3,4,33]

    #print computer([3,0,4,33,99],0)
    #print computer([1002,4,3,4,33],0)
    # jump tests
    #assert computer([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9],0) == 0
    print('OUTPUT IS', out)
    print('outb´put code is:', code)



#    assert computer([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9],4) == 1
#
#    assert computer([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
#1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
#999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99],2) == 999
#    assert computer([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
#1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
#999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99],8) == 1000
#    assert computer([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
#1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
#999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99],9) == 1001

        
if __name__=='__main__':

    #star1() # not 1
    star2()
    #test()
    #too low  4880388)

