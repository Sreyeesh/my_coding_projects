"""
Mcree: High Noon

Author : Sreyeesh Garimella 

Get the time when it's high noon somewhere in the world.


"""

  
from datetime import datetime
import pytz
import time
from playsound import playsound


utc = pytz.utc

# this is already list of  all time zones and not the actual time.

world_timezones = pytz.all_timezones

# print(len(world_timezones))
# print(world_timezones[0:359])
# print(type(world_timezones))

for t in world_timezones[0:359]:
    print(t)
    # print(datetime.now(pytz.timezone(t)).strftime('%a %d %b %Y %I:%M:%S.%f %p %z'))
    
    # if datetime.now(pytz.timezone(t).strftime('%H:%M %p')) ==  '12:00 PM': 
    #     print(f'In {t} it\s high noon.')
    current_time = datetime.now(pytz.timezone(t)).strftime('%H:%M %p')
    
    if current_time == '12:00 PM':
        playsound('/Users/sreyeeshgarimella/Documents/my_coding_projects/The_Complete_Python_Course/high_noon.mp3')
        # print("It\'s {t} high noon.")
        print(f"In {t} it\'s {current_time} high noon.")
        
    else:
        # print("It ain\'t my  time.")
        playsound('/Users/sreyeeshgarimella/Documents/my_coding_projects/The_Complete_Python_Course/My_Time.mp3')
        print(f"In {t} ain\'t {current_time} my time")
        break 
        # print('prepare to attack.')
    
   
        

        
        
        
        
        
    
  
        
  
