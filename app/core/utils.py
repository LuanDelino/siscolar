
from datetime import datetime, timezone, timedelta

def get_current_time():
    
    tz = timezone(timedelta(hours=-3))
    time_now = datetime.now()
    return  time_now.astimezone(tz).strftime("%Y-%m-%dT%H:%M:%S")