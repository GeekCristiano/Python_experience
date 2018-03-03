# Let's study the tools for working with the date and time
from datetime import date
from datetime import datetime
from datetime import timedelta

week_days = {0: "Mon", 1: "Tue", 2: "Wed", 3: "Thu", 4: "Fri", 5: "Sat", 6: "Sun"}
week_days = list(week_days.values())

months = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 7: "Jul",
          8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}
months = list(months.values())

# Get current date
today = date.today()
print("Current date is:", today)
print("Current day of the week is", week_days[today.weekday()])
print("Current day is:", today.day)
print("Current month is:", months[today.month - 1])
print("Current year is:", today.year)

# Get current datetime
now = datetime.now()
print("Current datetime is:", now)
print("Current time is:", datetime.time(now))
print("Current hour is:", now.hour)
print("Current minute is:", now.minute)
print("Current second is:", now.second)

# date formatting

# [(%y/%Y – Year), (%a/%A- weekday), (%b/%B- month), (%d - day of month)] .
print("Current datetime is:", now.strftime("%d %B %Y, %a"))

# %C- indicates the local date and time, %x- indicates the local date, %X- indicates the local time
print("Current datetime is:", now.strftime("%c"))
print("Current datetime is:", now.strftime("%x"))
print("Current datetime is:", now.strftime("%X"))

print("Current date in 24-hour format:", now.strftime("%H:%M:%S"))
print("Current date in 12-hour format:", now.strftime("%I:%M:%S"))

# using timedelta class

print(timedelta(days=1))
print("todays is:", str(datetime.now()))
print("tomorrow is:", str(datetime.now() + timedelta(days=1)))
print("one year ago is:", str(datetime.now() - timedelta(days=365)))

new_year_date = date(year=today.year, month=1, day=1)
today = date.today()

if new_year_date < today:
    print("Since the new year has passed %d days" % (today - new_year_date).days)
