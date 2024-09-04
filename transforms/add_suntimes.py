import datetime
from suntimes import SunTimes

def add_suntimes_for_record(row):
    date = datetime.datetime.fromtimestamp(row['epoch'])
    suntime = SunTimes(longitude=row['lon'], latitude=row['lat'], altitude=0)
    row['sunset'] = suntime.setwhere(date, "UTC").hour
    row['sunrise'] = suntime.risewhere(date, "UTC").hour
    return row

def add_suntimes(self):
    return self.map(f = add_suntimes_for_record)