# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 14:32:34 2021

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
"""


import data_extraction as de
import matplotlib.pyplot as plt
import seaborn as sns

all_data = de.all_data
data = de.data
files = de.file_names
col = de.col_names

# ANALYSIS AND VISUALIZATION CREATED BY PANDAS PIVOT TABLE
all_data = all_data.sort_values(by = ['Month','Day','Hr'], )
all_data.pivot_table(index=['Weekday'], values=['Average of Presence'], aggfunc='sum').sort_values(by='Average of Presence',ascending = False).plot(subplots=True)
all_data.pivot_table(index=['Month'], values=['Average of Presence'], aggfunc='sum').plot(subplots=True)
all_data.pivot_table(index=['Space Name'], values=['Average of MaxOccupants','Average of Presence'], aggfunc='sum').sort_values(by=['Average of Presence','Average of MaxOccupants'],ascending = False).plot(subplots=True)
all_data.pivot_table(index=['Space Name'], values=['Average of Lux'], aggfunc='sum').sort_values(by=['Space Name'],ascending = False).plot(subplots=True)
all_data.pivot_table(index=['Space Name'], values=['Average of Noise','Average of CO2','Average of VOC'], aggfunc='sum').sort_values(by='Space Name',ascending = False).plot(subplots=True)
all_data.pivot_table(index=['Space Name','Hr'], values=['Average of Temperature_Ajusted','Average of Humid','Average of Pressure'], aggfunc='sum').sort_values(by=['Space Name','Hr','Average of Pressure','Average of Humid'],ascending = False).plot(subplots=True,kind='line')
all_data.pivot_table(index=['Hr'], values=['Average of Lux','Average of CO2'], aggfunc='sum').plot(subplots=True)
all_data.pivot_table(index=['Hr'], values=['Average of Presence'], aggfunc='sum').plot(subplots=True)
all_data.pivot_table(index=['Hr'],columns='Space Name',values='Average of Presence',aggfunc='sum').plot()
all_data.pivot_table(index=['Hr'], values=['Average of Temperature_Ajusted'], aggfunc='sum').plot(subplots=True)
all_data.pivot_table(index=['Hr'], values=['Average of Lux'], aggfunc='sum').plot(subplots=True)
all_data.pivot_table(index=['Weekday','MinuteZone'], values=['Average of Presence'], aggfunc='sum').sort_values(by='Average of Presence',ascending = False).plot(subplots=True)
all_data[((all_data['Hr']>6) & (all_data['Hr']<20)) ].pivot_table(index=['Hr','MinuteZone'], values=['Average of Presence'], aggfunc='sum').sort_values(by=['Hr','MinuteZone','Average of Presence'],ascending = True).plot(subplots=True)
all_data.pivot_table(index=['Day',], values=['Average of Presence'], aggfunc='sum').sort_values(by=['Day','Average of Presence'],ascending = True).plot(subplots=True)

# CREATING COVARIANCE AND CORRELATION MATRIX 
features = ['MinuteZone','Space Name','Average of MaxOccupants','Average of Humid','Average of Noise','Average of CO2','Average of Presence','Average of Occupancy','Average of Temperature_Ajusted','Average of VOC','Average of Lux','Average of Pressure']
feature_cov = all_data[features].cov()
feature_corr = all_data[features].corr()


# PLOTTING COVARIANCE MATRIX
f, ax = plt.subplots(figsize=(10, 6))
hm = sns.heatmap(round(feature_cov,2), annot=True, ax=ax, cmap="coolwarm",fmt='.2f',linewidths=.05)
f.subplots_adjust(top=0.93)
t= f.suptitle('Covariance among Parameters', fontsize=10)


# PLOTTING CORRELATION MATRIX
f, ax = plt.subplots(figsize=(10, 6))
hm = sns.heatmap(round(feature_corr,2), annot=True, ax=ax, cmap="coolwarm",fmt='.2f',linewidths=.05)
f.subplots_adjust(top=0.93)
t= f.suptitle('Correlation among Parameters', fontsize=10)
new_features = ['Average of Humid','Average of Noise','Average of CO2','Average of Temperature_Ajusted','Average of Lux','Average of Pressure']

# CREATING PAIR PLOTS USING SEABORN
sns.pairplot(all_data[new_features])