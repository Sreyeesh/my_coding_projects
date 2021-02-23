import calendar

print(calendar.weekheader(2))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2020,7))
print(calendar.monthcalendar(2020, 7))
print(calendar.calendar(2020))

day_of_the_week = calendar.weekday(2020, 7,21)
print(day_of_the_week)

is_leap = calendar.isleap(2020)
print(is_leap)


how_many_leap_days = calendar.leapdays(2000, 2020)
print(how_many_leap_days)

