import time 
from datetime import datetime, timedelta

def rel_timer(dic):
    """
    Timer for relative time
    """
    t = dic["time"]
    total_seconds = t[0] * 3600 + t[1] * 60 + t[2]
    time.sleep(total_seconds)
    return dic["message"]

def abs_timer(dic):
    """
    Timer for absolute time
    """
    t = dic["time"]
    now = datetime.now()
    alarm_time = datetime(now.year, now.month, now.day, t[0], t[1], t[2])

    # If the alarm time is in the past, set it for the next day
    if alarm_time < now:
        alarm_time += timedelta(days=1)

    # Calculate the time difference between now and the alarm time
    time_to_wait = (alarm_time - now).total_seconds()
    time.sleep(time_to_wait)

    return dic["message"] 