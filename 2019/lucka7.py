from itertools import permutations


# amplifier should halt when its lacking an input

def read_input():

    with open('input7.txt','r') as f:
        # split up in parts the onvert every straing to int using map
        return map(int, f.read().split(','))
    #return [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
   
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
        
    def set_phase(self,value):
        self.phase = value
        
    def set_input(self,value):
        self.input_ = value 
        
    def get_input(self):
        if self.input_iter == 0:
            input_ = self.phase
            self.input_iter = 1
        elif self.input_iter == 1:
            input_ = self.input_
            #self.input_iter = 0
        else:
            print 'someting whent wrong 2'
        
        return input_
     
    def computer(self):  
        ii = self.inst_pointer
        code = self.code
        finished = 0
        #print('code at first',code)
        while ii<len(code):
            #print('index', ii)
            operation = code[ii]
            A, B, C, op = interpret_opcode(code[ii])    
            #print('operation',operation)
            if operation == 99:
                self.inst_pointer = 0 
                finished = 1
                ii = len(code)+1
                break;
            
            elif op == 1:            
                do = code[code[ii+1]] if C == 0 else code[ii+1]
                re = code[code[ii+2]] if B == 0 else code[ii+2]            
                if A==0: 
                    code[code[ii+3]] = do + re
                else:
                    code[ii+3]= do + re
                ii +=4
                
            elif op == 2:  
                do = code[code[ii+1]] if C == 0 else code[ii+1]
                re = code[code[ii+2]] if B == 0 else code[ii+2]
                if A==0: 
                    code[code[ii+3]] = do * re
                   # print('code A=0 do och re',code[ii+1],re)
                else:
                    code[ii+3] = do * re      
                ii += 4
                
            elif op == 3:
                code[ code[ii+1]] = self.get_input()
                ii += 2
                
            elif op == 4:
                self.output_val = code[code[ii+1]] if C == 0 else code[ii+1]
                ii += 2
                self.inst_pointer = ii
                #print('breaks at op 4 at index: ', ii)
                break;
    
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
            #print('code', code)
        self.code = code 
            
        return (self.output_val,finished)   

def star1(): #doesnt work anymore, changed computer()
    
    phases = list(permutations([0, 1, 2, 3, 4]))    
    #phase = [4,3,2,1,0]
    
    ampA = Amplifier()
    ampB = Amplifier()
    ampC = Amplifier()
    ampD = Amplifier()
    ampE = Amplifier()

    outputs = []
    for phase in phases:                
        ampA.set_phase(phase[0])
        ampB.set_phase(phase[1])
        ampC.set_phase(phase[2])
        ampD.set_phase(phase[3])
        ampE.set_phase(phase[4])
        
        ampA.set_input(0)
        outA = ampA.computer()
        #print type(outA)
        #print('output A',outA)
        ampB.set_input(outA)        
        outB, test = ampB.computer()
        
        ampC.set_input(outB)
        outC = ampC.computer()
        
        ampD.set_input(outC)
        outD = ampD.computer()
        
        ampE.set_input(outD)
        outE = ampE.computer()
               
        outputs.append(outE)

    print('the highest output from amplification is', max(outputs))
    
    #239312 too low
    #844468 correct
def star2():

    #phases = list(permutations([0, 1, 2, 3, 4]))
    #in feedback loop mode    
    phases_fb = list(permutations([5, 6, 7, 8, 9]))
    
    #phases_fb = [[ 5,6,7,8,9],[5,6,7,8,9]]


    outputs = []
     

       
    # Feedback loop mode
    for phase in phases_fb:
            
            #initial input to the loop
        outE = 0
        
        #se till så att allt är reset innan du kör allt igen?
        
        # ja, något med det är fel
              
        ampA = Amplifier()
        ampB = Amplifier()
        ampC = Amplifier()
        ampD = Amplifier()
        ampE = Amplifier()
     
        ampA.set_phase(phase[0])
        ampB.set_phase(phase[1])
        ampC.set_phase(phase[2])
        ampD.set_phase(phase[3])
        ampE.set_phase(phase[4])
        
        iter_ = 0
        print phase
        feedback = 0
        while feedback < 1:  # until amplifier E reaches its 99 code
        
        #while iter_ <2:
        
            ampA.set_input(outE)
            outA, test = ampA.computer()
            print('output A',outA)

            ampB.set_input(outA)        
            outB, test = ampB.computer()
            print('output B',outB)
            
            ampC.set_input(outB)
            outC, test = ampC.computer()
            print('output C',outC)
            
            ampD.set_input(outC)
            outD, test = ampD.computer()
            print('output D',outD)
            
            ampE.set_input(outD)
            outE, E_finish = ampE.computer()
            print('output E',outE)            
            print('E_finish',E_finish)
            
            iter_ += 1
            
            if E_finish == 1:
                print 'e finish is true'
                feedback = 1

        outputs.append(outE)
    print('the highest output from amplification is', max(outputs))
    
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

