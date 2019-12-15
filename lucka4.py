
# tip!: #for digit in number[1:]:# use slice to iterate thorugh parts of a list only!!!



def star1(start=136818,end=685979+1):
    

    #my_input = 136818-685979
    counter = 0
    digit_list = []
    for tal in range(start,end): 
        digit_list.append( list(map(int, str(tal))))

    # rule 1
    for number in digit_list:  
        # **check rule 1**
        rule1 = check_rule1(number)
        if rule1 == 1:

            # **check rule 2 extended**
            rule2 = check_rule2_extended(number)
            if rule2 ==1:
                counter +=1
        
    print ('int total %d'%counter)


def check_rule1(number):
    return_val = 1
    for ii in range(0,5):
        if number[ii] > number[ii+1] :           
            return_val = 0
    return return_val

def check_rule2_extended(number):
    rule2 = 0
    ii = 0
    if number[ii] == number[ii+1] and number[ii] != number[ii+2]:
        rule2 = 1

    ii = 1
    if number[ii] == number[ii+1] and number[ii] != number[ii+2] and number[ii] != number[ii-1]:
        rule2 = 1

    ii = 2
    if number[ii] == number[ii+1] and number[ii] != number[ii+2] and number[ii] != number[ii-1]:
        rule2 = 1

    ii = 3
    if number[ii] == number[ii+1] and number[ii] != number[ii+2] and number[ii] != number[ii-1]:
        rule2 = 1
    ii = 4
    if number[ii] == number[ii+1] and number[ii] != number[ii-1]:
        rule2 = 1    
      
#0 1 2 3 4 5 
    return rule2
   

def check_rule2(number):
    rule2 = 0
    for ii in range(0,5):
        if number[ii] == number[ii+1] :
            rule2 = 1
            break;
    return rule2

def test1():
    counter = 0
##    for tal in range(100,200):
##
##        for digit in tal: 
##            print digit

    
if __name__ == '__main__':
   
    #star1(111129,111137)
    star1()
    star1(112233,112233+1)
    star1(123444,123444+1)
    star1(111122,111122+1)
    #1501 too  high
    #1411 too high
   


    
