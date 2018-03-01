# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 17:48:21 2018

@author: privolin.naidoo
"""
teamName = 'Meeseeks'
import numpy as np

def hello():
    print(f'Hello, team {teamName}!')


hello()



def calc_dist (start,end):

    x = abs(start[0] - end[0])
    y = abs(start[1] - end[1])

    return x+y
'''
R – number of rows of the grid (1 ≤ R ≤ 10000)
● C – number of columns of the grid (1 ≤ C ≤ 10000)
● F – number of vehicles in the fleet (1 ≤ F ≤ 1000)
● N – number of rides (1 ≤ N ≤ 10000)
● B – per-ride bonus for starting the ride on time (1 ≤ B ≤ 10000)
● T – number of steps in the simulation (1 ≤ T ≤ 10 )
'''

data = open('a_example.in', 'r')
lines = data.readlines()
data.close()
# parameters
line1 = lines[0].split(' ')
R = int(line1[0])
C = int(line1[1])
F = int(line1[2])
N = int(line1[3])
B = int(line1[4])
T = int(line1[5][:-1])

data = []
for i in range(R + 1):
    if i == 0:
        continue
    else:
        print(lines[i][0:-1])
        data.append( (lines[i][:-1]).split(' '))

city = np.array(data)
# pizza[pizza == 'T'] = 1
# pizza[pizza == 'M'] = 0
city = city.astype(np.int64)

dists = abs(city[:,0] - city[:,2]) + abs(city[:,1] - city[:,3])
time = abs(city[:,4] - city[:,5]) 


out = np.zeros([R,C+1])
    
import pandas as pd



'''

Converting to DataFrame

'''
cols = ['x1','y1','x2','y2','start','end'] #cols for dataframe
trip_data = pd.DataFrame(city,columns = cols)

trip_data['dist'] = abs(trip_data['x1']-trip_data['x2']) +  abs(trip_data['y1']-trip_data['y2'])
trip_data['time'] = abs(trip_data['start'] - trip_data['end']) 

avail = trip_data.loc[trip_data['start'] >= 2]


cars= np.zeros([F, T])
cars.fill(-1)
cars = cars.astype(np.int64)




"""
Algotrithms
"""











def output(cars):
    wrt = ''
    trips = set([])
    for i in range(len(cars)):
        trips = set(cars[i])
        trips.remove(-1)
        print(trips)
        t =  ' '.join([str(x) for x in list(trips)])
        wrt += ' '.join([str(len(trips)),t, '\n'])
        
    
    fl = open('out.file','w')
    fl.writelines(wrt)
    fl.close()
        
    
    
output(cars)
    
    



