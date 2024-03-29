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
edate = '2020-07-14 00:00:00'

# set Kestrel stations input data
Kestrel_pname = '/Users/claragarciasan/Documents/TUD/Research/MeasurementsHeatStress/data_campaign'
Kestrel_s1name = 'HEAT - 2514397_final.xls'
Kestrel_s2name = 'HEAT - 2514400_final.xls'
Kestrel_s3name = 'HEAT - 2514402_final.xls'
Kestrel_s4name = 'HEAT - 2514403_final.xls'
Kestrel_s5name = 'HEAT - 2520824_final.xls'
labelname = ['2514397','2514400','2514402','2514403','2520824']


# read data from measurements
data_sensor = dict()
data_sensor[0]=read_data.readKestrelSensors1(Kestrel_pname,Kestrel_s1name,sdate,edate)
data_sensor[1]=read_data.readKestrelSensors1(Kestrel_pname,Kestrel_s2name,sdate,edate)
data_sensor[2]=read_data.readKestrelSensors1(Kestrel_pname,Kestrel_s3name,sdate,edate)
data_sensor[3]=read_data.readKestrelSensors1(Kestrel_pname,Kestrel_s4name,sdate,edate)
data_sensor[4]=read_data.readKestrelSensors1(Kestrel_pname,Kestrel_s5name,sdate,edate)

# plot Kestrel sensors
fig = plt.figure(figsize=(17,10))
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)

# sensors in plot
ss = 0
se = 5

#nameFig = 'T_RH_Rad_sensor'+str(se)+'.png'
nameFig = 'T_RH_Rad_sensor_All.png'

# plot ax1
for isensor in range(ss,se):
	nlabel=['sensor'+str(isensor)]
	ax1.plot(data_sensor[isensor]['FORMATTED DATE-TIME'],data_sensor[isensor]['Temperature'].astype(float),'x',color=plt.cm.tab20b(isensor),label=labelname[isensor])
ax1.set_ylabel('T [C]',fontsize=14)
ax1.legend()
ax1.set_xlabel('Date [UTC]',fontsize=14)
ymin, ymax = (data_sensor[isensor]['Temperature'].astype(float).min(),data_sensor[isensor]['Temperature'].astype(float).max())
ax1.set_yticks(np.round(np.linspace(ymin, ymax, 10), 2))
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
ax1.xaxis.set_minor_formatter(mdates.DateFormatter('%d'))
ax1.xaxis.grid(True, which="minor")
ax1.xaxis.set_major_locator(mdates.MonthLocator())
ax1.xaxis.set_major_formatter(mdates.DateFormatter('\n%b\n'))
# plot ax2
for isensor in range(ss,se):
	nlabel=['sensor'+str(isensor)]
	ax2.plot(data_sensor[isensor]['FORMATTED DATE-TIME'],data_sensor[isensor]['Relative Humidity'].astype(float),'x',color=plt.cm.tab20b(isensor),label=labelname[isensor])
ax2.set_ylabel('Relative Humidiy [%]',fontsize=14)
ax2.legend()
ax2.set_xlabel('Date [UTC]',fontsize=14)
ymin, ymax = (data_sensor[isensor]['Relative Humidity'].astype(float).min(),data_sensor[isensor]['Relative Humidity'].astype(float).max())
ax2.set_yticks(np.round(np.linspace(ymin, ymax, 10), 2))
ax2.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
ax2.xaxis.set_minor_formatter(mdates.DateFormatter('%d'))
ax2.xaxis.grid(True, which="minor")
ax2.xaxis.set_major_locator(mdates.MonthLocator())
ax2.xaxis.set_major_formatter(mdates.DateFormatter('\n%b\n'))
# plot ax3
for isensor in range(ss,se):
	nlabel=['sensor'+str(isensor)]
	data_sensor[isensor]['TWL'] = data_sensor[isensor]['TWL'].replace('***',np.nan)
	ax3.plot(data_sensor[isensor]['FORMATTED DATE-TIME'],data_sensor[isensor]['TWL'].astype(float),'x',color=plt.cm.tab20b(isensor),label=labelname[isensor])
ax3.set_ylabel('TWL [w/m^2]',fontsize=14)
ax3.legend()
ax3.set_xlabel('Date [UTC]',fontsize=14)
ymin, ymax = (data_sensor[isensor]['TWL'].astype(float).min(),data_sensor[isensor]['TWL'].astype(float).max())
ax3.set_yticks(np.round(np.linspace(ymin, ymax, 10), 2))
ax3.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
ax3.xaxis.set_minor_formatter(mdates.DateFormatter('%d'))
ax3.xaxis.grid(True, which="minor")
ax3.xaxis.set_major_locator(mdates.MonthLocator())
ax3.xaxis.set_major_formatter(mdates.DateFormatter('\n%b\n'))
plt.show()
fig.savefig('/Users/claragarciasan/Documents/TUD/Research/MeasurementsHeatStress/plots_chooseDay/'+nameFig)