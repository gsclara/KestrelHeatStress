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
# sdate = '2020-05-19 13:00:00'
# edate = '2020-05-20 13:00:00'
sdate = '2020-06-02 11:00:00'
edate = '2020-06-03 11:00:00'

# set Kestrel stations input data
#Kestrel_pname = '/Users/claragarciasan/Documents/TUD/MeasurementsHeatStress/Calibration_Rotterdam_Bolnes/20200519_20'
Kestrel_pname = '/Users/claragarciasan/Documents/TUD/MeasurementsHeatStress/Calibration Rotterdam Blijdorp/20200502-03'
nameFig = 'KestrelCalibrationOverConcrete'
Kestrel_s1name = 'HEAT - 2514397.xls'
Kestrel_s2name = 'HEAT - 2514400.xls'
Kestrel_s3name = 'HEAT - 2514402.xls'
Kestrel_s4name = 'HEAT - 2514403.xls'
Kestrel_s5name = 'HEAT - 2520824.xls'
labelname = ['2514397','2514400','2514402','2514403','2520824']


# read data from measurements
data_sensor = dict()
data_sensor[0]=read_data.readKestrelSensors(Kestrel_pname,Kestrel_s1name,sdate,edate)
data_sensor[1]=read_data.readKestrelSensors(Kestrel_pname,Kestrel_s2name,sdate,edate)
data_sensor[2]=read_data.readKestrelSensors(Kestrel_pname,Kestrel_s3name,sdate,edate)
data_sensor[3]=read_data.readKestrelSensors(Kestrel_pname,Kestrel_s4name,sdate,edate)
data_sensor[4]=read_data.readKestrelSensors(Kestrel_pname,Kestrel_s5name,sdate,edate)

# plot Kestrel sensors
fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

# plot ax1
for isensor in range(0,5):
	nlabel=['sensor'+str(isensor)]
	ax1.plot(data_sensor[isensor]['FORMATTED DATE_TIME'],data_sensor[isensor]['Temperature'],'x',color=plt.cm.tab20b(isensor),label=labelname[isensor])
ax1.set_ylabel('T [C]',fontsize=14)
ax1.legend()
ax1.set_xlabel('Time [UTC]',fontsize=14)
# plot ax2
for isensor in range(0,5):
	nlabel=['sensor'+str(isensor)]
	ax2.plot(data_sensor[isensor]['FORMATTED DATE_TIME'],data_sensor[isensor]['Wind Speed'],'x',color=plt.cm.tab20b(isensor),label=labelname[isensor])
ax2.set_ylabel('Wind Speed [m/s]',fontsize=14)
ax2.legend()
ax2.set_xlabel('Time [UTC]',fontsize=14)
# plot ax3
for isensor in range(0,5):
	nlabel=['sensor'+str(isensor)]
	ax3.plot(data_sensor[isensor]['FORMATTED DATE_TIME'],data_sensor[isensor]['Relative Humidity'],'x',color=plt.cm.tab20b(isensor),label=labelname[isensor])
ax3.set_ylabel('Relative Humidity [%]',fontsize=14)
ax3.legend()
ax3.set_xlabel('Time [UTC]',fontsize=14)
# plot ax4
for isensor in range(0,5):
	nlabel=['sensor'+str(isensor)]
	ax4.plot(data_sensor[isensor]['FORMATTED DATE_TIME'],data_sensor[isensor]['Heat Stress Index'],'x',color=plt.cm.tab20b(isensor),label=labelname[isensor])
ax4.set_ylabel('Heat Stress Index [C]',fontsize=14)
ax4.legend()
ax4.set_xlabel('Time [UTC]',fontsize=14)

#plt.show()
fig.savefig('/Users/claragarciasan/Documents/TUD/MeasurementsHeatStress/plotsCalibration/'+nameFig)