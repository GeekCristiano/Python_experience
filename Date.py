# Let's study the tools for working with the date and time
from datetime import date

week_days = {0: "Mon", 1: "Tue", 2: "Wed", 3: "Thu", 4: "Fri", 5: "Sat", 6: "Sun"}

months = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 7: "Jul",
          8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}

# Get current date

today = date.today()
print("Current date is:", today)
print("Current day of the week is", week_days.get(today.weekday()))
print("Current day is:", today.day)
print("Current month is:", months.get(today.month))
print("Current year is:", today.year)
