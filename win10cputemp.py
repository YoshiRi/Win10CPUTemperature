"""
You have to run this script as administrator.
live plotter is from https://makersportal.com/blog/2018/8/14/real-time-graphing-in-python
"""

import os
import time
import subprocess
import re
import matplotlib.pyplot as plt
import numpy as np


#### Get Temp
# this code some how has error
#cmd = """for /f "skip=1 tokens=2 delims==" %%A in ('wmic /namespace:\\\\root\\wmi PATH MSAcpi_ThermalZoneTemperature get CurrentTemperature /value') do set /a "HunDegCel=(%%~A*10)-27315" & echo %HunDegCel:~0,-2%.%HunDegCel:~-2% """

cmd = """wmic /namespace:\\\\root\\wmi PATH MSAcpi_ThermalZoneTemperature get CurrentTemperature /value"""
ch = subprocess.check_output(cmd, shell=True)
out = ch.decode("SHIFT-JIS")
# getoutput
tmp = [x for x in re.split('[\n\r=]', out) if x if x.isdigit()][0]
c_tmp =int(tmp)/10.0 - 273.15

#### 1. Live plotter
# use ggplot style for more sophisticated visuals
plt.style.use('ggplot')

def live_plotter(x_vec,y1_data,line1,identifier='',pause_time=0.1):
    if line1==[]:
        # this is the call to matplotlib that allows dynamic plotting
        plt.ion()
        fig = plt.figure(figsize=(13,6))
        ax = fig.add_subplot(111)
        # create a variable for the line so we can later update it
        line1, = ax.plot(x_vec,y1_data,'-o',alpha=0.8)        
        #update plot label/title
        plt.ylabel('Celsius Degree')
        plt.title('CPU Temperature'.format(identifier))
        plt.show()
    
    # after the figure, axis, and line are created, we only need to update the y-data
    line1.set_ydata(y1_data)
    # adjust limits if new data goes beyond bounds
    if np.min(y1_data)<=line1.axes.get_ylim()[0] or np.max(y1_data)>=line1.axes.get_ylim()[1]:
        plt.ylim([np.min(y1_data)-np.std(y1_data),np.max(y1_data)+np.std(y1_data)])
    # this pauses the data so the figure/axis can catch up - the amount of pause can be altered above
    plt.pause(pause_time)
    
    # return line so we can update it again in the next iteration
    return line1


#### Plotter setting

size = 100
dataa = [c_tmp]*size
xlabels = np.arange(size) - size + 1
line1 = []



#### while loop
while True:
    try:
        ch = subprocess.check_output(cmd, shell=True)
        out = ch.decode("SHIFT-JIS")
        # getoutput
        tmp = [x for x in re.split('[\n\r=]', out) if x if x.isdigit()][0]
        c_tmp =int(tmp)/10.0 - 273.15
        #print(c_tmp)
        dataa.append(c_tmp)
        dataa.pop(0)
        line1 = live_plotter(xlabels,np.array(dataa),line1)
        time.sleep(1)
    except KeyboardInterrupt:
        exit(0)

