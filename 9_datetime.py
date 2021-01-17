import datetime
import pytz

today = datetime.date.today()
print(today)

birthday = datetime.date(1994,12,19)

print(birthday)

days_since_birth = today - birthday

print(days_since_birth)

tdelta = datetime.timedelta(days=10)
print(today + tdelta)

print(today.month)
print(today.weekday())

print(datetime.time(7,2,20,15))
#datetime.date(y,m,d)
#datetime.time(h,m,s,ms)
#datetime.datetime(y,m,d,h,m,s,ms)

hour_delta = datetime.timedelta(hours=10)
print(datetime.datetime.now() + hour_delta)

datetime_today=datetime.datetime.now(tz=pytz.utc)
print(datetime_today.astimezone(pytz.timezone('US/Pacific')))
datetime_pacific = datetime_today.astimezone(pytz.timezone('US/Pacific'))
for timezones in pytz.all_timezones:
    print(timezones)

#taghyire format str format time
print(datetime_pacific.strftime('%B %d, %Y'))
#taghyire format str parse time
print(datetime.datetime.strptime('march 09,2019','%B %d,%Y'))
print(repr(datetime.datetime.strptime('march 09,2019','%B %d,%Y')))
