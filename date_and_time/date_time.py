"""
Tutorial code for the topic "Understanding Python Date and Time with Examples" @SitePoint
"""
from datetime import datetime
from datetime import date
import time


# get current date and time
current_date_time = datetime.now()
print(current_date_time)

# get current date
current_date = date.today()
print(current_date)
print(current_date.ctime())

# create date object
mydate = date(2023, 3, 13)
print('The date is: ', mydate)

# create date from ISO date string
iso_date = date.fromisoformat('2023-03-13')
print("Date from ISO format: ", iso_date)

# extract year, month, day from date object
current_date = date.today()
year = current_date.year
print("The year is: ", year)
month = current_date.month
print("The month is: ", month)
day = current_date.day
print("The day is: ", day)