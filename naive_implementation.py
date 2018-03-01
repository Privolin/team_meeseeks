# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 22:14:14 2018

@author: privolin.naidoo
"""

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




'''
R – number of rows of the grid (1 ≤ R ≤ 10000)
● C – number of columns of the grid (1 ≤ C ≤ 10000)
● F – number of vehicles in the fleet (1 ≤ F ≤ 1000)
● N – number of rides (1 ≤ N ≤ 10000)
● B – per-ride bonus for starting the ride on time (1 ≤ B ≤ 10000)
● T – number of steps in the simulation (1 ≤ T ≤ 10 )
'''
#data = open('a_example.in','r')
data = open('b_should_be_easy.in', 'r')
#data = open('c_no_hurry.in','r')
#data = open('d_metropolis.in','r')
#data = open('e_high_bonus.in','r')

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
for i in range(N + 1):
    if i == 0:
        continue
    else:
        #print(lines[i][0:-1])
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
cols = ['x1','y1','x2','y2','early_start','end'] #cols for dataframe
trip_data = pd.DataFrame(city,columns = cols)

trip_data['dist'] = abs(trip_data['x1']-trip_data['x2']) +  abs(trip_data['y1']-trip_data['y2'])
trip_data['time'] = abs(trip_data['early_start'] - trip_data['end']) 
trip_data['late_start'] = (trip_data['time'] - trip_data['dist']) + trip_data['early_start']
trip_data['possible'] = trip_data['late_start'] - trip_data['x1'] - trip_data['y1']
trip_data['orig_index'] = np.arange(len(trip_data))
sorted_data = trip_data.loc[trip_data['possible'] >= 0].sort_values(['early_start','dist','late_start'])#.sort_values(['dist'],ascending=False)
sorted_data['new_index'] = np.arange(len(sorted_data))
sorted_data['used'] = 0
sorted_data
cars= np.zeros([F, T])
cars.fill(-1)
cars = cars.astype(np.int64)


def get_trip():
    return 0

"""
Algotrithms

"""


#for i in range(len(sorted_data)):
#    cars[i%F,i] = sorted_data.loc[sorted_data['new_index'] == i,'orig_index']
    
for i in range(T):
    for k in range(F):
        if cars[k,i] == -1:
            trips = set(cars[k])
            trips.remove(-1)
            pos = []
            if len(trips) == 0:
                pos = np.array([[0,0]])
            else:
                pos = np.array(sorted_data.loc[sorted_data['orig_index'] == max(trips), ['x2','y2']])
            
            temp = sorted_data.loc[sorted_data['used'] == 0 ]
            
            temp['temp'] = abs(pos[0][0]-temp['x1']) +  abs(pos[0][1]-temp['y1'])
            temp = temp.loc[temp['temp'] == (temp['temp'].min())]
            temp = (temp.loc[sorted_data['used'] == 0 ]).head(1)
            if len(temp) == 0:
                continue
            else:
                dist = list(temp['dist'])[0]
                cars[k,(i+dist)] = temp['orig_index']
                sorted_data.loc[sorted_data['new_index'] == list(temp['new_index'])[0],'used'] = 1
                
        else:
            continue
    







"""
Output File

"""

def output(cars):
    wrt = ''
    trips = set([])
    for i in range(len(cars)):
        trips = set(cars[i])
        trips.remove(-1)
        #print(trips)
        t =  ' '.join([str(x) for x in list(trips)])
        wrt += ' '.join([str(len(trips)),t, '\n'])
        
    
    fl = open('out.file','w')
    fl.writelines(wrt)
    fl.close()
        
    
    
output(cars)
    
    



