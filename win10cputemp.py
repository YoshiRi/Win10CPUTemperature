"""
You have to run this script as administrator.
PowerShell is used.
I am not sure, if the temperature reading is right.
"""

import subprocess
import os
#import datetime
import time

psscript = """
:loop
for /f "skip=1 tokens=2 delims==" %%A in ('wmic /namespace:\\root\wmi PATH MSAcpi_ThermalZoneTemperature get CurrentTemperature /value') do set /a "HunDegCel=(%%~A*10)-27315"
echo %HunDegCel:~0,-2%.%HunDegCel:~-2%
timeout /t 1 /nobreak >nul
goto :loop
"""

fh = os.popen("get_cpu_temp.bat")
output = fh.read()
print( output[:5])
fh.close()


# safely stop subprocess with while
while True:
    try:
        fh = os.popen("get_cpu_temp.bat")
        output = fh.read()
        print( output[:5])
        fh.close()
        time.sleep(1)
    except KeyboardInterrupt:
        exit(0)