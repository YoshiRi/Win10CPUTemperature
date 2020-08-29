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
$t = Get-WmiObject MSAcpi_ThermalZoneTemperature -Namespace “root/wmi”

while (1) {$t.CurrentTemperature; sleep 2}
"""
psscript = """
:loop
for /f "skip=1 tokens=2 delims==" %%A in ('wmic /namespace:\\root\wmi PATH MSAcpi_ThermalZoneTemperature get CurrentTemperature /value') do set /a "HunDegCel=(%%~A*10)-27315"
echo %HunDegCel:~0,-2%.%HunDegCel:~-2%
timeout /t 1 /nobreak >nul
goto :loop
"""

si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW

cmd = ['powershell.exe', '-Command',  psscript]
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, startupinfo=si)

# safely stop subprocess with while
while True:
    try:
        tmp = proc.stdout.readline()
        #proc.stdout.readline() # hack to prevent output twice
        print(tmp.decode("SHIFT-JIS"))
        #celsius = float(tmp)
        #celsius_str = f'{celsius:.2f};{datetime.datetime.now().isoformat()}'
        #print(celsius)
        time.sleep(1)
    except KeyboardInterrupt:
        proc.kill()
        exit(0)