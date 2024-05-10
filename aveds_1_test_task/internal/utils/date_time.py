import time
from datetime import datetime


def datetime_to_timestamp(dt: datetime):
    return int(time.mktime(dt.timetuple()))


def now():
    import calendar

    return int(calendar.timegm(datetime.utcnow().utctimetuple()))
