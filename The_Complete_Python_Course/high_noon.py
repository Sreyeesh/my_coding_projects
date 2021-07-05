"""
Mcree: High Noon

Author : Sreyeesh Garimella 

Get the time when it's high noon somewhere in the world.


"""

from datetime import date, datetime
import time
import pytz

utc = pytz.utc
today_time = time.ctime()
world_timezones = pytz.all_timezones #this is already list of  all time zones and not the actual time. 





# print(world_timezones)
# print(today_time)
# print(utc)



