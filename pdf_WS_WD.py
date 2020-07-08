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
from windrose import WindroseAxes



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

# sensors in plot
ss = 4
se = 5

nameFig = 'windrose_WS_WD_sensor'+str(se)+'.png'

# plot ax
for isensor in range(ss,se):
	nlabel=['sensor'+str(isensor)]
	ax = WindroseAxes.from_ax()
	data_sensor[isensor]['Direction ‚ True'] = data_sensor[isensor]['Direction ‚ True'].replace('***',np.nan)
	ax.bar(data_sensor[isensor]['Direction ‚ True'].astype(float), data_sensor[isensor]['Wind Speed'].astype(float), normed=True, opening=0.8, edgecolor='white')
	ax.set_legend()
plt.savefig('/Users/claragarciasan/Documents/TUD/Research/MeasurementsHeatStress/plots_chooseDay/'+nameFig)