"""
You have to run this script as administrator.
PowerShell is used.
I am not sure, if the temperature reading is right.
"""

import os
import time
import subprocess
import re

# this code some how has error
#cmd = """for /f "skip=1 tokens=2 delims==" %%A in ('wmic /namespace:\\\\root\\wmi PATH MSAcpi_ThermalZoneTemperature get CurrentTemperature /value') do set /a "HunDegCel=(%%~A*10)-27315" & echo %HunDegCel:~0,-2%.%HunDegCel:~-2% """

cmd = """wmic /namespace:\\\\root\\wmi PATH MSAcpi_ThermalZoneTemperature get CurrentTemperature /value"""


# while loop
while True:
    try:
        ch = subprocess.check_output(cmd, shell=True)
        out = ch.decode("SHIFT-JIS")
        # getoutput
        tmp = [x for x in re.split('[\n\r=]', out) if x if x.isdigit()][0]
        #print([x for x in re.split('[\n\r=]', out) if x if x.isdigit()][0])
        c_tmp =int(tmp)/10.0 - 273.15
        print(c_tmp)
        time.sleep(1)
    except KeyboardInterrupt:
        exit(0)

