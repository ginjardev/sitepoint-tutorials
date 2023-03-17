"""
Tutorial code for the topic "Understanding Python Date and Time with Examples" @SitePoint
"""
from datetime import datetime, date, time, timedelta
import time as t
from pytz import timezone

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

# create time object
my_time = time()
print("My time is: ", my_time)

# create time from ISO time string
iso_time = time.fromisoformat('12:45:12')
print('The time says: ', iso_time)

# extract hour, minute, second and microsecond from time object
new_time = time(7, 20, 50, 569230)
hour = new_time.hour
print('Hours: ',hour)
minute = new_time.minute
print('Minutes: ', minute)
second = new_time.second
print('Seconds: ', second)
microsecond = new_time.microsecond
print('Microseconds: ', microsecond)

#create date time object
dt = datetime(2023, 3, 14, 10, 38, 10, 345389)
print('The date time is: ', dt)

# get current local date time
print('Current locate date time is: ', datetime.now())

#create datetime object from ISO string
iso_dt = datetime.fromisoformat('2023-03-14 11:25:30.983023')
print('Date time from ISO is: ', iso_dt)

#extract date and time attributes from datetime object
new_dt = datetime.now()

year = new_dt.year
print('Year : ', year)
month = new_dt.month
print('Month : ', month)
day = new_dt.day
print('Day : ', day)
hour = new_dt.hour
print('Hours : ', hour)
minute = new_dt.minute
print('Minutes: ', minute)
second = new_dt.second
print('Seconds: ', second)
microsecond = new_dt.microsecond
print('Microseconds: ', microsecond)


# create timedelta object
td = timedelta(10, 30, 4300, 3000, 12, 5, 3)
print('Time Delta:', td)

# format date in datetime object
date_time = datetime.now()
formatted_date = date_time.strftime("%m/%d/%Y")
print("Formatted Date:", formatted_date)

# format time in datetime object
date_time = datetime.now()

formatted_time = date_time.strftime("%I:%M:%S")
print("Formatted time in 12-hour clock:", formatted_time)

formatted_time_2 = date_time.strftime("%I:%M:%S %p")
print("Formatted time in 12-hour clock indicating time of day:", formatted_time_2)

# format time and date in datetime object
date_time = datetime.now()

formatted_date_time = date_time.strftime("%d %B %Y, %H:%M:%S")
print("Formatted date and time:", formatted_date_time)

formatted_date_time_2 = date_time.strftime("%A, %d %B %Y, %I:%M %p")
print("Formatted date and time in 12-hour clock:", formatted_date_time_2)

# strptime() string to datetime object
date_string = "March 15, 23 12:12:20"
dt_format = "%B %d, %y %H:%M:%S"

datetime_from_string = datetime.strptime(date_string, dt_format)
print("Datetime from string:", datetime_from_string)

# strptime() string to date object
datetime_object = datetime.strptime("15/03/23", "%d/%m/%y")
d_o = datetime_object.date()

print("Date from string:", d_o)

# strptime() string to date object
time_object = datetime.strptime("15 Mar, 2023 13:50:30", "%d %b, %Y %H:%M:%S")
t_o = time_object.time()


print("Time from string:", t_o)

# calculate future date
date_now = datetime.now()
print("Today's date:", date_now)

future_date = date_now + timedelta(days=7)
print("Future date is:", future_date)

# calculate difference between two dates
present_date = date.today()
print("Present date:", present_date)

future_date = date(2023,5, 10)
print("Future date:", future_date)

time_gap = future_date - present_date

print("Time gap between two dates:", time_gap)

# calculate difference between time delta objects

time_delta1 = timedelta(days = 2, hours = 1, seconds = 33, weeks=2)
time_delta2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)

result = time_delta1 + time_delta2

print("Sum of two delta objects:", result)


# create dateime object with timezone info
tz = timezone('Africa/Accra')
date_time_object = datetime.now(tz)

print("Timezone information:", date_time_object.tzinfo)
print("Timezone code:", date_time_object.tzname())

# switch between timezones
accra_timezone = timezone('Africa/Accra')

accra_datetime = datetime.now(accra_timezone)

print("Current date time in Accra:", accra_datetime)
# switch to New York timezone

new_york_timezone = timezone('America/New_York')
new_york_datetime = accra_datetime.astimezone(new_york_timezone)

print("Current date time in New York:", new_york_datetime)

# time module
# get time in seconds since epoch
time_secs = t.time()
print("Time in sceconds from epoch", time_secs)

# gmtime()
gm_time = t.gmtime()

print("Time struct in UTC:", gm_time)

# localtime()
local_time = t.localtime()

print("Time struct in local time:", local_time)

# ctime()
time_in_secs = 1678671984.939945

time_string = t.ctime(time_in_secs)
print("Time string: ", time_string)

# strftime()
time_tuple = t.gmtime()
time_format = "%y/%m/%d %I:%M:%S %p"
time_in_string = t.strftime(time_format, time_tuple)
print("Time expressed as formatted string:", time_in_string)

# sleep()
for i in range(5):
    lt = t.localtime()
    seconds = lt.tm_sec
    print(seconds)
    t.sleep(2)

hel = {"name": "Hellp", "number": [1, 3, 4], "school": {"name": "talent"}}
