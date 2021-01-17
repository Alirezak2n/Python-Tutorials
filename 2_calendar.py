import calendar
import datetime
import time
# print ruzaye hafte
print(calendar.weekheader(3))
print()
# avalin ruz
print(calendar.firstweekday())
print()
# ye mah ro miyare
print(calendar.month(2019, 5))
# ye mah ro be surate matrix miare
print(calendar.monthcalendar(2019, 3))
#kole salo miare
print(calendar.calendar(2019))

day_of_the_week = calendar.weekday(2019,3,8)
print(day_of_the_week)

is_leap = calendar.isleap(2020)
print(is_leap)

howmany_leap_days = calendar.leapdays(2000, 2020)
print(howmany_leap_days)

