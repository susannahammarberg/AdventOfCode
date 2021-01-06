# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 21:46:51 2020

@author: Sanna
"""


with open('input13.txt','r') as fp:
    info = fp.readlines()
        
bus_list = info[1].split(',')
time = int(info[0])

waiting_times = []

for bus in bus_list:
    
    if bus != 'x':
          
        print(bus)
        n=0
        while int(bus)*n < time:
            
            n += 1
            waiting_time = (int(bus)*n) - time
        waiting_times.append(waiting_time)
        print(n)
        
        
        
        

#bus_list = ['7','13','x','x','59','x','31','19']
bus_list = [17,'x',13,19]
bus_list = [67,7,59,61]
bus_list = [67,'x',7,59,61]
bus_list = [67,7,'x',59,61]
bus_list = [1789,37,47,1889]



#count number of buses not 'x'
nbr_bus = 0
for bus in bus_list:
    if bus != 'x':
        nbr_bus += 1

this = True
t0 = 1202161480
while this == True:
    test = 0
    for ii in range(0,len(bus_list)):
        if bus_list[ii] != 'x':
            if (t0+ii) % int(bus_list[ii]) == 0:
                #print('True',t0+ii)
                test += 1
    if test == nbr_bus:
        this = False
        
    #print(t0)
    t0 += 1

print('Answer: ', t0-1)

# Chinese remainder theorem   .. something something
