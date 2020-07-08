# Clara Garcia-Sanchez
# 29/05/2020
# functions to read the measurement data input:
# readMeteoStationsRotterdam: reads data from the stations installed in Rotterdam
# readKestrelSensors: reads data from the Kestrel sensors
# Last Modified: 29/05/2020

import numpy as np
import pandas as pd

def readMeteoStationsRotterdam(folder_name, file_name, sheet_name, start_date, end_date):	
	p_name = folder_name
	f_name = file_name # change it to the name of your excel file
	s_name = sheet_name # change it to your sheet name
	df = pd.read_excel(open(p_name+'/'+f_name, 'rb'),sheet_name=s_name) 
	s_date = start_date
	e_date = end_date
	data_interest = df[(df['date_hour'].astype(str) >= s_date) & \
		(df['date_hour'].astype(str) <= e_date)]
	#data_interest = df
	return data_interest

def readKestrelSensors(folder_name, sensor_name, start_date, end_date):	
	p_name = folder_name # change it to the path of your folder
	s_name = sensor_name # change it to the name of your sensor
	df = pd.read_excel(open(p_name+'/'+s_name, 'rb'), header=3) 
	s_date = start_date
	e_date = end_date
	df['FORMATTED DATE_TIME'] = pd.to_datetime(df['FORMATTED DATE_TIME'], errors='coerce')
	df['FORMATTED DATE_TIME'] = df['FORMATTED DATE_TIME'].dt.tz_localize('CET').dt.tz_convert('UTC')
	data_interest = df[(df['FORMATTED DATE_TIME'].astype(str) >= s_date) & \
		(df['FORMATTED DATE_TIME'].astype(str) <= e_date)]
	return data_interest

def readKestrelSensors1(folder_name, sensor_name, start_date, end_date):	
	p_name = folder_name # change it to the path of your folder
	s_name = sensor_name # change it to the name of your sensor
	df = pd.read_excel(open(p_name+'/'+s_name, 'rb'), header=3) 
	s_date = start_date
	e_date = end_date
	df['FORMATTED DATE-TIME'] = pd.to_datetime(df['FORMATTED DATE-TIME'], errors='coerce')
	df['FORMATTED DATE-TIME'] = df['FORMATTED DATE-TIME'].dt.tz_localize('CET').dt.tz_convert('UTC')
	data_interest = df[(df['FORMATTED DATE-TIME'].astype(str) >= s_date) & \
		(df['FORMATTED DATE-TIME'].astype(str) <= e_date)]
	return data_interest
