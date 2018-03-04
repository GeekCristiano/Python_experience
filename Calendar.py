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
