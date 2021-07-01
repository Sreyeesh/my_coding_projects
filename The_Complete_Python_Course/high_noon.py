"""
Mcree: High Noon

Author : Sreyeesh Garimella 

Get the time when it's high noon somewhere in the world.


"""

from datetime import datetime
import pytz
from pprint import pprint


all_time_zones = pytz.all_timezones
print(f' these are all the worlds time zones: ', all_time_zones)


list_of_time_zones = []
print(list_of_time_zones)

for time in all_time_zones:
    print(time)
    # list_of_time_zones.append(time)





