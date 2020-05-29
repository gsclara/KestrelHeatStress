# Clara Garcia-Sanchez
# 29/05/2020
# read and plot results from Meteo station (Bolnes) and Kestrel measurements
#
# -Usage-
#	output = readProbesOF(ftype, nprobes, ntimes, nfolder , nfile)
# -Inputs-
#	ftype: field type (scalar/vector)
#   nprobes: number of probes
#   ntimes: number of points/tims extracted from the CFD
#   nfolder: name of the folder where the data is storaged
#   nfile: name file to be read
#
# -Outputs-
#	outputs (1: scalar)
#	outputs (3: vector)
# Last Modified: 16/07/2019

import numpy as np
import pandas as pd

def readMeteoStationsRotterdam(file_name, sheet_name, start_date, end_date):	
		f_name = file_name # change it to the name of your excel file
	s_name = sheet_name # change it to your sheet name
	df = pd.read_excel(open(f_name, 'rb'),sheet_name=s_name) 
	s_date = start_date
	e_date = end_date
	data_interest = df[(df['date_hour'].astype(str) >= s_date) & \
		(df['date_hour'].astype(str) <= e_date)]
	return data_interest

def readKestrelSensors(folder_name, file_name, sensor_name, start_date, end_date):	
	p_name = folder_name # change it to the path of your folder
	f_name = file_name # change it to the name of your excel file
	s_name = sensor_name # change it to the name of your sensor
	df = pd.read_excel(open(p_name+'/'+s_name, 'rb'), header=3) 
	s_date = start_date
	e_date = end_date
	data_interest = df[(df['FORMATTED DATE_TIME'].astype(str) >= s_date) & \
		(df['FORMATTED DATE_TIME'].astype(str) <= e_date)]
	return data_interest