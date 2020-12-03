# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 16:37:02 2020

@author: Sanna
"""

import numpy as np

def main():
       
    with open("input4.txt", "r") as fd:
        records = fd.read().splitlines() #for lines without the \n after each line

    records.sort()

    times = {}
    
    #midnight hour
    #2D list
    #n = 1000
    n = 60
    hour = [ 0] * n 
    
    
    for line in records:
        if '#' in line:   #(try)
            guard_nbr = line.split('#')[1].split(' ')[0]    
            if guard_nbr not in times:
                times[guard_nbr] = 0

        if 'falls asleep' in line:
            sleep_time = line.split(' ')[1].split(':')[1].split(']')[0]
        elif 'wakes up' in line:
            wake_time = line.split(' ')[1].split(':')[1].split(']')[0]
            sleep_duration = int(wake_time)-int(sleep_time)
            times[guard_nbr] += sleep_duration
            
            if guard_nbr == '1021':
                for i in range(int(sleep_time),int(wake_time)):
                    hour[i] += 1
                
    #Strategy 1: Find the guard that has the most minutes asleep.
    #What minute does that guard spend asleep the most?
    max_time_guard =  max(times, key=lambda k: times[k])
    print(max_time_guard)


    max(hour)
    print('Answer: ')
    print(int(max_time_guard)*30)

def part2():

    with open("input4.txt", "r") as fd:
        records = fd.read().splitlines() #for lines without the \n after each line

    records.sort()

    times = {}    
    
    for line in records:
        if '#' in line:   #(try)
            guard_nbr = line.split('#')[1].split(' ')[0]    
            if guard_nbr not in times:
                # add new hour list for every guard
                times[guard_nbr] = [0] * 60

        if 'falls asleep' in line:
            sleep_time = line.split(' ')[1].split(':')[1].split(']')[0]
        elif 'wakes up' in line:
            wake_time = line.split(' ')[1].split(':')[1].split(']')[0]
            
            for i in range(int(sleep_time),int(wake_time)):
                times[guard_nbr][i] += 1
            
                
    #Strategy 2: Of all guards, which guard is most frequently asleep on the same minute?
    
    #find highest number in hours. output that index + minute (index of both outer and nested list)

    max_times = []
    max_minute = []
    for key in times:
        max_times.append(max(times[key]))
        max_minute.append(times[key].index(max(times[key])))   
        
        
    best_minute_index = max_times.index(max(max_times))


    single_max_min = max_minute[best_minute_index]
    
    best_guard = list(times.keys())[best_minute_index]
    
    
    print('Answer: ')
    print(single_max_min*int(best_guard))

if __name__ == '__main__':
    #main()
    part2()