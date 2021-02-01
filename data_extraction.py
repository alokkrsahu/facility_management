# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 22:05:50 2021

@author: alokk

DESCRIPTION:
Day – Day of the Week name and number 
Month – Month of the year name and number 
Year – Number 
Minute – Minute of the hour 
RoomName – Name of the space 
CO2 – Carbon Dioxide in the air – Optimal below 1250 
Humidity – Humidity in the air – Optimal 40-60% 
Lux – Light levels – Optimal 200-700 lux 
Noise – dB levels – Optimal below 65dB 
Pressure – Air Pressure Levels – Mechanically driver to optimal is balance across site 
VOC – Volatile Organic Compounds in the air – Optimal below 600 
Occupancy - Count of People in the space 
Max Occupancy – Max count of people the space can hold 
Temperature – Degrees centigrade temp in the space 
Occupancy % - Occupancy/Max Occupancy 

The analysis on the data should answer the following questions: 

•	Space performance across any/all singular parameters 
•	Correlations/relationships across different parameters 
•	Specific relations of parameters as they apply to active occupied spaces 
•	Time series-based understandings 
•	Relationships to indoor performance and outdoor performance in temperature and humidity terms (Beirut/Lebanon is site location) 
•	COVID-19 performance and insight 
•	Site grouping and general space performance framework ideas 
•	Personnel/Occupied space Performance framework ideas 
•	Future Forecasting/Prediction models

"""
#   Space performance across any/all singular parameters 

from os import listdir
from os.path import isfile, join
import pandas as pd

myfiles = [f for f in listdir('./Data') if isfile(join('./Data', f))]

file_names  = list()
for each in myfiles:
    name =  each.split()    
    file_names.append(name[-1])
    

data = dict()
all_data = pd.DataFrame(columns = list(pd.read_csv('./Data/Global Workplace ' + file_names[0])))
for fn in file_names:
    data.update({fn:pd.read_csv('./Data/Global Workplace ' + fn)})
    all_data = all_data.append(pd.DataFrame(data[fn]))

    

col_names = data[fn].columns

i = 1
space = dict()
space_name = data[fn]['Space Name'].unique()

for each in space_name:
    space.update({each:i})
    i += 1

i = 1
MinZone = dict()
MinuteZone = data[fn]['MinuteZone'].unique()
for each in MinuteZone:
    MinZone.update({each:i})
    i += 1

#ENCODING SPACE NAME, MINUTE ZONE
for each in file_names:
     data[each]['MinuteZone'] = data[name[-1]]['MinuteZone'].map(MinZone)
     data[each]['Space Name'] = data[name[-1]]['Space Name'].map(space)
#df['c'] = df.apply(lambda x: max([len(x) for x in [df['a'], df['b']]]))
all_data['Date'] = pd.to_datetime((2020*10000+all_data.Month*100+all_data.Day).apply(str),format='%Y%m%d')
all_data['Weekday'] = all_data['Date'].dt.day_name()

i = 1
Weekday_num = dict()
Weekday = all_data['Weekday'].unique()
for each in Weekday:
    Weekday_num.update({each:i})
    i += 1