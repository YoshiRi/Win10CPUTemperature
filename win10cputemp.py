"""
You have to run this script as administrator.
PowerShell is used.
I am not sure, if the temperature reading is right.
"""

import os
import time



# while loop
while True:
    try:
        fh = os.popen("get_cpu_temp.bat")
        output = fh.read()
        print(output[:5])
        fh.close()
        time.sleep(1)
    except KeyboardInterrupt:
        exit(0)