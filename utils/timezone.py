from datetime import datetime
from zoneinfo import ZoneInfo


def india_time():
    # Store IST as a normal SQLite datetime for simple display.
    return datetime.now(ZoneInfo("Asia/Kolkata")).replace(tzinfo=None)
