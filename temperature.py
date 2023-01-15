#-*---------Develop by Keidi Francis--*---#
#--*--------For you know the temperature of your system/Pc ------*---#

import os
import re

def get_cpu_temperature():
    # get the temperature data from the sensors
    temperature_data = os.popen('sensors').read()
    # search for the line containing the temperature data
    temperature_match = re.search(r'Core 0:.*?\+(\d+)', temperature_data)
    if temperature_match:
        # extract the temperature from the match
        temperature = int(temperature_match.group(1))
        # return the temperature in Celsius
        return temperature

# get the current temperature
temperature = get_cpu_temperature()
print(f'Current temperature: {temperature} °C')
