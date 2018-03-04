# import the necessary module
import calendar

# create textCalendar for March 2018
c = calendar.TextCalendar(calendar.MONDAY)
str = c.formatmonth(2018, 3)
print(str)
