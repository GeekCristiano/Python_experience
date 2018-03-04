# import the necessary module
import calendar

# create textCalendar for March 2018
c = calendar.TextCalendar(calendar.MONDAY)
# if you want to get HTML code of calendar use HTMLCalendar class
# c = calendar.HTMLCalendar(calendar.MONDAY)
str = c.formatmonth(2018, 3)
print(str)

# iterate over calendar
for i in c.itermonthdates(2018, 3):
    print(i)

# print name of months and  week days
for m in calendar.month_name:
    print(m)

for d in calendar.day_abbr:
    print(d)

# print day of week in each month in 2018 year
for month in range(1, 13):
    month_cal = calendar.monthcalendar(2018, month)
    first_week = month_cal[0]

    for d in first_week:
        if d == 1:
            print("In %s 2018, the first day of the month is %s."
                  % (calendar.month_name[month], calendar.day_name[first_week.index(d)]))
            break
