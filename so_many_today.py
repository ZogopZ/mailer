# Calculates time left until internship's end date. Due to Corona-Virus
# this date was shifted. The time period 13/03/2020 - 13/5/2020, was
# moved to 1/6/2020 - 31/07/2020.  Also calculates how much money was
# earned on current date and time.


from datetime import timedelta
from render_tools import *
import title_tools
from cli_tools import cli_master
from tools import *
import timeit


start_time = timeit.default_timer()

output_list = []
tag_dictionary = {}
now = datetime.datetime.today()
# now = datetime.datetime(2020, 7, 24, 18, 25)
# now = datetime.datetime(2020, 7, 24, 8, 2)
print(render_datetime(now, tag_dictionary))
# Stopped working due to Corona-Virus.
corona_start = datetime.datetime(2020, 3, 14, 9)
# Started working after Corona-Virus restrictions were lifted.
corona_end = datetime.datetime(2020, 5, 31, 9)
# Work starts at 9:00 o'clock in the morning.
work_start = datetime.datetime(now.year, now.month, now.day, 9, 0, 0, 0)
# Work end at 17:00 o'clock in the evening.
work_end = datetime.datetime(now.year, now.month, now.day, 17, 0, 0, 0)
# Specify starting date of internship.
first_day_date = datetime.datetime(2019, 11, 13, 9)
# Deprecated: Specify ending date of internship.
last_day_date = datetime.datetime(2020, 7, 31, 9)
# Specify a random date-time to use as start_time in military titles.
# Remove this and use 'first_day_date' variable to see the correct
# title.
random_start_time = datetime.datetime(2020, 7, 15, 9, 0, 0, 0)
# Sets working dates, weekends
set_dates(first_day_date, last_day_date, corona_start, corona_end)
# Sets holidays.
set_holidays()
# Sets working_status True if working, false if not.
set_working_status(now)
# Creates an instance of Title class.
user_titles = title_tools.Title(random_start_time, last_day_date, now)
user_titles.military_title()
print(render_title(user_titles, tag_dictionary))

# Total pay for 6 month internship.
total_to_be_paid = 580.8 * 6
# 23.232 euro per day is defined by corresponding company.
pay_per_hour_8 = 23.232 / 8
# Calculate pay per microsecond working 8 hours a day.
pay_per_microsecond_8 = 23.232 / (8 * 60 * 60 * 1000 * 1000)
# Generate date difference.
so_many_today = last_day_date + timedelta(hours=8) - now
# This function returns time left in multiple time types.
tfl = time_left(so_many_today)
print(render_time(tfl, tag_dictionary))

time_worked_today = 0
# If I am working right now, calculate pay earned today.
if get_working_status():
    # Calculate working time today.
    time_worked_today = now - datetime.datetime(now.year,
                                                now.month,
                                                now.day, 9)
elif not get_working_status():
    if now < work_start:
        time_worked_today = now - now
    elif now > work_end:
        time_worked_today = work_end - work_start
print(render_work(time_worked_today, pay_per_microsecond_8, tag_dictionary))

time_worked = 0
days_worked = 0
# For each working day, calculate the sum of working seconds.
for day in working_dates:
    # Calculate days worked for printing only.
    days_worked += 1
    if day.year == now.year and day.month == now.month and day.day == now.day:
        # For today working seconds are already calculated.
        break
    time_worked += 8 * 60 * 60
time_worked += time_worked_today.total_seconds()
# Convert to microseconds.
microseconds_passed = time_worked * (10**6)
microseconds_passed_off_days = paid_days_off(now) * 8 * 60 * 60 * (10**6)
euro_made = (microseconds_passed+microseconds_passed_off_days) \
            * pay_per_microsecond_8
monthly_wage_earned = 0
# First month work was less than a full months work.
if (euro_made / 580.8) < 1:
    monthly_wage_earned = euro_made - 359.63
# Not first month of work.
elif (euro_made / 580.8) > 1:
    # Calculate full months passed.
    full_months_passed = int((euro_made - 359.63) / 580.8)
    monthly_wage_earned = euro_made - 359.63 - full_months_passed * 580.8
# Exactly one month's work.
elif (euro_made / 580.8) == 1:
    monthly_wage_earned = 580.8
print(render_wage(monthly_wage_earned, tag_dictionary))
print(render_total(euro_made, days_worked, tag_dictionary))
print(render_signatures())
populate_template(tag_dictionary)
with open('ignore/hotmail.html', 'r') as hotmail_html_file, \
        open('ignore/gmail.html', 'r') as gmail_html_file:
    hotmail_email = hotmail_html_file.read()
    gmail_email = gmail_html_file.read()
cli_master(hotmail_email, gmail_email, tag_dictionary)
stop_time = timeit.default_timer()
execution_time = stop_time - start_time
# It returns time in seconds.
print('-- mailer was Executed in ' + str('{:.4f}'.format(execution_time))
      + ' seconds --')
