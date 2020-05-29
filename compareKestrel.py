# Clara Garcia-Sanchez
# 29/05/2020
# plot comparison between the meteorological stations in Rotterdam and the Kestrel sensors
# Functions used:
# - readKestrelSensors
# Last Modified: 29/05/2020

import numpy as np
import pandas as pd
import read_data_functions as read_data
import matplotlib.pyplot as plt
import matplotlib.ticker
from matplotlib.cm import get_cmap

# set start and end dates
sdate = '2020-05-19 13:00:00'
edate = '2020-05-20 10:00:00'

# set Kestrel stations input data
Kestrel_pname = '/Users/claragarciasan/Documents/TUD/MeasurementsHeatStress/Calibration_Rotterdam_Bolnes/20200519_20'
Kestrel_s1name = 'HEAT - 2514397.xls'
Kestrel_s2name = 'HEAT - 2514400.xls'
Kestrel_s3name = 'HEAT - 2514402.xls'
Kestrel_s4name = 'HEAT - 2514403.xls'
Kestrel_s5name = 'HEAT - 2520824.xls'

# read data from measurements
data_sensor1=read_data.readKestrelSensors(Kestrel_pname,Kestrel_s1name,sdate,edate)
data_sensor2=read_data.readKestrelSensors(Kestrel_pname,Kestrel_s2name,sdate,edate)
data_sensor3=read_data.readKestrelSensors(Kestrel_pname,Kestrel_s3name,sdate,edate)
data_sensor4=read_data.readKestrelSensors(Kestrel_pname,Kestrel_s4name,sdate,edate)
data_sensor5=read_data.readKestrelSensors(Kestrel_pname,Kestrel_s5name,sdate,edate)

# plot Kestrel sensors
fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

# plot ax1
ax1.plot(data_sensor1['FORMATTED DATE_TIME'],data_sensor1['Temperature'],'x',color=plt.cm.tab20b(0),label='2514397')
ax1.plot(data_sensor2['FORMATTED DATE_TIME'],data_sensor2['Temperature'],'x',color=plt.cm.tab20b(1),label='2514400')
ax1.plot(data_sensor3['FORMATTED DATE_TIME'],data_sensor3['Temperature'],'x',color=plt.cm.tab20b(2),label='2514402')
ax1.plot(data_sensor4['FORMATTED DATE_TIME'],data_sensor4['Temperature'],'x',color=plt.cm.tab20b(3),label='2514403')
ax1.plot(data_sensor5['FORMATTED DATE_TIME'],data_sensor5['Temperature'],'x',color=plt.cm.tab20b(4),label='2520824')
ax1.set_ylabel('T [C]',fontsize=14)
ax1.legend()
ax1.set_xlabel('Time',fontsize=14)
# plot ax2
ax2.plot(data_sensor1['FORMATTED DATE_TIME'],data_sensor1['Wind Speed'],'x',color=plt.cm.tab20b(0),label='2514397')
ax2.plot(data_sensor2['FORMATTED DATE_TIME'],data_sensor2['Wind Speed'],'x',color=plt.cm.tab20b(1),label='2514400')
ax2.plot(data_sensor3['FORMATTED DATE_TIME'],data_sensor3['Wind Speed'],'x',color=plt.cm.tab20b(2),label='2514402')
ax2.plot(data_sensor4['FORMATTED DATE_TIME'],data_sensor4['Wind Speed'],'x',color=plt.cm.tab20b(3),label='2514403')
ax2.plot(data_sensor5['FORMATTED DATE_TIME'],data_sensor5['Wind Speed'],'x',color=plt.cm.tab20b(4),label='2520824')
ax2.set_ylabel('Wind Speed [m/s]',fontsize=14)
ax2.legend()
ax2.set_xlabel('Time',fontsize=14)
# plot ax3
ax3.plot(data_sensor1['FORMATTED DATE_TIME'],data_sensor1['Relative Humidity'],'x',color=plt.cm.tab20b(0),label='2514397')
ax3.plot(data_sensor2['FORMATTED DATE_TIME'],data_sensor2['Relative Humidity'],'x',color=plt.cm.tab20b(1),label='2514400')
ax3.plot(data_sensor3['FORMATTED DATE_TIME'],data_sensor3['Relative Humidity'],'x',color=plt.cm.tab20b(2),label='2514402')
ax3.plot(data_sensor4['FORMATTED DATE_TIME'],data_sensor4['Relative Humidity'],'x',color=plt.cm.tab20b(3),label='2514403')
ax3.plot(data_sensor5['FORMATTED DATE_TIME'],data_sensor5['Relative Humidity'],'x',color=plt.cm.tab20b(4),label='2520824')
ax3.set_ylabel('Relative Humidity [%]',fontsize=14)
ax3.legend()
ax3.set_xlabel('Time',fontsize=14)
# plot ax4
ax4.plot(data_sensor1['FORMATTED DATE_TIME'],data_sensor1['Heat Stress Index'],'x',color=plt.cm.tab20b(0),label='2514397')
ax4.plot(data_sensor2['FORMATTED DATE_TIME'],data_sensor2['Heat Stress Index'],'x',color=plt.cm.tab20b(1),label='2514400')
ax4.plot(data_sensor3['FORMATTED DATE_TIME'],data_sensor3['Heat Stress Index'],'x',color=plt.cm.tab20b(2),label='2514402')
ax4.plot(data_sensor4['FORMATTED DATE_TIME'],data_sensor4['Heat Stress Index'],'x',color=plt.cm.tab20b(3),label='2514403')
ax4.plot(data_sensor5['FORMATTED DATE_TIME'],data_sensor5['Heat Stress Index'],'x',color=plt.cm.tab20b(4),label='2520824')
ax4.set_ylabel('Heat Stress Index [C]',fontsize=14)
ax4.legend()
ax4.set_xlabel('Time',fontsize=14)

plt.show()
