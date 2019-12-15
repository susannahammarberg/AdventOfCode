import numpy as np
#import matplotlib.pyplot as plt

    
def star2():

    with open('input8.txt','r') as f:
        dat = f.read()
    print 'hello'
    layers = 100
    rows=6
    cols=25
    image = np.zeros((layers,rows,cols))
    indx=0
    for layer in range(0,layers):
        for row in range(0,rows):
            for col in range(0,cols):
                image[layer,row,col]=dat[indx]

                indx+=1
    #while there are 2s in the image
    test=1
    
    for layer_indx in range(1,layers):
        if test == 1:
            test = 0
            for row in range(0,rows):
                for col in range(0,cols):
                    if image[0,row,col] == 2:
                        # replace with the number 'below'
                        image[0,row,col] = image[0+layer_indx,row,col]
                        test = 1
           
                    
    print image[0]  
    #plt.figure()
    #plt.imshow(image[0])
    #plt.show()
    


def test2():
    dat = "0222112222120000"
    layers = 4
    rows=2
    cols=2
    image = np.zeros((layers,rows,cols))
    indx=0
    for layer in range(0,layers):
        for row in range(0,rows):
            for col in range(0,cols):
                image[layer,row,col]=dat[indx]

                indx+=1
    #while there are 2s in the image
    test=1
    
    for layer_indx in range(1,layers):
        if test == 1:
            test = 0
            for row in range(0,rows):
                for col in range(0,cols):
                    if image[0,row,col] == 2:
                        # replace with the number 'below'
                        image[0,row,col] = image[0+layer_indx,row,col]
                        test = 1
           
                    
    print image[0]            


def test1():

    dat = "123456789012"
    nbr_twos_list =[]
    for i in range(0,len(dat),6):
        nbr_twos = 0
        #print dat[i:i+6]
        for jj in dat[i:i+6]:
            if jj =='2':
                nbr_twos +=1
        nbr_twos_list.append(nbr_twos)
            
    print nbr_twos_list   

    
def star1():

    with open('input8.txt','r') as f:
        dat = f.read()

    nbr_zeros_list =[]
    img_size = 25*6
    
    for i in range(0,len(dat),img_size):
        nbr_zeros = 0

        for jj in dat[i:i+img_size]:
            if jj =='0':
                nbr_zeros +=1
        nbr_zeros_list.append(nbr_zeros)
        print i 
            
    print nbr_zeros_list
    print 'someting wrong with the last index. not 0'
    print len(dat)
    print (len(nbr_zeros_list))
    #find minima exept 0
    
    min_0 = nbr_zeros_list.index(min(nbr_zeros_list[0:-2]))
    ii= min_0 *(25*6)
    print ii
    nbr_ones =0
    nbr_twos=0
    for jj in dat[ii:ii+img_size]:
        print jj
        if jj =='1':
            nbr_ones+=1
        elif jj=='2':
            nbr_twos+=1
    print 'Answer \n'
    print nbr_ones*nbr_twos


def main():

    star1() #1965 right
    test2()
    star2()
    # 1000 too low
    #test1()


if __name__=='__main__':


    main()
