# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 17:48:23 2021

@author: alokk
"""

import data_extraction as de
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression

import pandas as pd

all_data = de.all_data
#Selected Features
features = ['Hr','MinuteZone','Space Name','Average of MaxOccupants','Average of Humid','Average of Noise','Average of CO2','Average of Temperature_Ajusted','Average of Lux','Average of Pressure','Weekday']

#Target Feature
label = ['Average of OccupancyPercentage']

regr = RandomForestRegressor(max_depth=10, random_state=0)

data = all_data[features]

data['Weekday'] = data['Weekday'].map(de.Weekday_num)
data['MinuteZone'] = data['MinuteZone'].map(de.MinZone)
data['Space Name'] = data['Space Name'].map(de.space)

data['Space Name'].fillna(value=data['Space Name'].median(), inplace=True)
data['Average of Lux'].fillna(value=data['Average of Lux'].mean(), inplace=True)
train = data
test = all_data[label]

test.fillna(value=test.mean(), inplace=True)

X_train, X_test, y_train, y_test = train_test_split(train, test, test_size=0.33, random_state=100)

def select_features(X_train, y_train, X_test):
	# configure to select all features
	fs = SelectKBest(score_func=f_regression, k='all')
	# learn relationship from training data
	fs.fit(X_train, y_train)
	# transform train input data
	X_train_fs = fs.transform(X_train)
	# transform test input data
	X_test_fs = fs.transform(X_test)
	return X_train_fs, X_test_fs, fs

X_train_fs, X_test_fs, fs = select_features(X_train, y_train, X_test)
# what are scores for the features

for i in range(len(fs.scores_)):
	print('Feature %s: %f' % (features[i], fs.scores_[i]))

# plot the scores
z = pd.DataFrame([features,list(fs.scores_)]).T
z.columns =['Feature Name', 'Feature Score']
z.plot('Feature Name', 'Feature Score',figsize=(10,3))


regr.fit(X_train, y_train)

y_pred = regr.predict(X_test)

print(mean_absolute_error(y_test, y_pred, multioutput='raw_values'))
