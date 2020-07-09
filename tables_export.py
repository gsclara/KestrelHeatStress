# Clara Garcia-Sanchez
# 08/07/2020
# plot comparison between the Kestrel sensors for Temperature, Relative Humidity and Radiation
# Functions used:
# - readKestrelSensors
# Last Modified: 29/05/2020

import numpy as np
import pandas as pd
import read_data_functions as read_data
import matplotlib.pyplot as plt
import matplotlib.ticker
from matplotlib.cm import get_cmap
import matplotlib.dates as mdates


# set start and end dates
sdate = '2020-06-09 00:00:00'
edate = '2020-07-07 00:00:00'

# set Kestrel stations input data
Kestrel_pname = '/Users/claragarciasan/Documents/TUD/Research/MeasurementsHeatStress/data_campaign'
Kestrel_s1name = 'HEAT - 2514397.xls'
Kestrel_s2name = 'HEAT - 2514400.xls'
Kestrel_s3name = 'HEAT - 2514402.xls'
Kestrel_s4name = 'HEAT - 2514403.xls'
Kestrel_s5name = 'HEAT - 2520824.xls'
labelname = ['2514397','2514400','2514402','2514403','2520824']


# read data from measurements
data_sensor = dict()
data_sensor[0]=read_data.readKestrelSensors1(Kestrel_pname,Kestrel_s1name,sdate,edate)
data_sensor[1]=read_data.readKestrelSensors1(Kestrel_pname,Kestrel_s2name,sdate,edate)
data_sensor[2]=read_data.readKestrelSensors1(Kestrel_pname,Kestrel_s3name,sdate,edate)
data_sensor[3]=read_data.readKestrelSensors1(Kestrel_pname,Kestrel_s4name,sdate,edate)
data_sensor[4]=read_data.readKestrelSensors1(Kestrel_pname,Kestrel_s5name,sdate,edate)

# sensors numbers
ss = 0
se = 5

# daily averages to choose a day to simulate
for isensor in range(ss,se):
	nameTab0 = 'daily_averages_sensor'+str(isensor+1)+'.csv'
	data_sensor[isensor]['Wind Speed'] = data_sensor[isensor]['Wind Speed'].astype(float)
	data_sensor[isensor]['Relative Humidity'] = data_sensor[isensor]['Relative Humidity'].astype(float)
	data_sensor[isensor]['Temperature'] = data_sensor[isensor]['Temperature'].astype(float)
	data_sensor[isensor].set_index('FORMATTED DATE-TIME')
	dayly_avg = data_sensor[isensor].set_index('FORMATTED DATE-TIME').resample('1D').mean()
	dayly_min = data_sensor[isensor].set_index('FORMATTED DATE-TIME').resample('1D').min()
	dayly_max = data_sensor[isensor].set_index('FORMATTED DATE-TIME').resample('1D').max()
	dayly_std = data_sensor[isensor].set_index('FORMATTED DATE-TIME').resample('1D').std()
	print(dayly_std['Wind Speed'])
	print(dayly_avg['Wind Speed'])
	df_avg_min_max_std = pd.concat([dayly_avg['Temperature'], dayly_min['Temperature'],dayly_max['Temperature'],dayly_std['Temperature'],
				dayly_avg['Wind Speed'], dayly_min['Wind Speed'],dayly_max['Wind Speed'],dayly_std['Wind Speed'],
				dayly_avg['Relative Humidity'], dayly_min['Relative Humidity'],dayly_max['Relative Humidity'],dayly_std['Relative Humidity']], 
				axis=1, keys=['T mean','T min','T max','T std', 'WS mean','WS min','WS max','WS std','RH mean','RH min','RH max','RH std',])

	df_avg_min_max_std.to_csv(r'/Users/claragarciasan/Documents/TUD/Research/MeasurementsHeatStress/plots_chooseDay/'+nameTab0)

# name tables validation output
nameTab1 = 'hourly_averages_Temperature.csv'
nameTab2 = 'hourly_averages_RelativeHumidity.csv'
nameTab3 = 'hourly_averages_WindSpeed.csv'
nameTab4 = 'hourly_averages_WindDirection.csv'

hourly_avg = dict()
for isensor in range(ss,se):
	data_sensor[isensor]['Wind Speed'] = data_sensor[isensor]['Wind Speed'].astype(float)
	data_sensor[isensor]['Relative Humidity'] = data_sensor[isensor]['Relative Humidity'].astype(float)
	data_sensor[isensor]['Temperature'] = data_sensor[isensor]['Temperature'].astype(float)
	data_sensor[isensor]['Direction ‚ True'] = data_sensor[isensor]['Direction ‚ True'].replace('***',np.nan)
	data_sensor[isensor]['Direction ‚ True'] = data_sensor[isensor]['Direction ‚ True'].astype(float)
	hourly_avg[isensor] = data_sensor[isensor].set_index('FORMATTED DATE-TIME').resample('1H').mean()
df_temperature = pd.concat([hourly_avg[0]['Temperature'], hourly_avg[1]['Temperature'],hourly_avg[2]['Temperature'],hourly_avg[3]['Temperature'],hourly_avg[4]['Temperature']], 
				axis=1, keys=[labelname[0],labelname[1],labelname[2],labelname[3],labelname[4]])
df_relative_humidity = pd.concat([hourly_avg[0]['Relative Humidity'], hourly_avg[1]['Relative Humidity'],hourly_avg[2]['Relative Humidity'],hourly_avg[3]['Relative Humidity'],hourly_avg[4]['Temperature']], 
				axis=1, keys=[labelname[0],labelname[1],labelname[2],labelname[3],labelname[4]])
df_wind_speed = pd.concat([hourly_avg[0]['Wind Speed'], hourly_avg[1]['Wind Speed'],hourly_avg[2]['Wind Speed'],hourly_avg[3]['Wind Speed'],hourly_avg[4]['Wind Speed']], 
				axis=1, keys=[labelname[0],labelname[1],labelname[2],labelname[3],labelname[4]])
df_wind_direction = pd.concat([hourly_avg[0]['Direction ‚ True'], hourly_avg[1]['Direction ‚ True'],hourly_avg[2]['Direction ‚ True'],hourly_avg[3]['Direction ‚ True'],hourly_avg[4]['Direction ‚ True']], 
				axis=1, keys=[labelname[0],labelname[1],labelname[2],labelname[3],labelname[4]])

df_temperature.to_csv(r'/Users/claragarciasan/Documents/TUD/Research/MeasurementsHeatStress/validation_data/'+nameTab1)
df_relative_humidity.to_csv(r'/Users/claragarciasan/Documents/TUD/Research/MeasurementsHeatStress/validation_data/'+nameTab2)
df_wind_speed.to_csv(r'/Users/claragarciasan/Documents/TUD/Research/MeasurementsHeatStress/validation_data/'+nameTab3)
df_wind_direction.to_csv(r'/Users/claragarciasan/Documents/TUD/Research/MeasurementsHeatStress/validation_data/'+nameTab4)

