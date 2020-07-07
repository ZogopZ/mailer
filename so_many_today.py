# Calculates time left until internship's end date. Due to Corona-Virus
# this date was shifted. The time period 13/03/2020 - 13/5/2020, was
# moved to 1/6/2020 - 31/07/2020.  Also calculates how much money was
# earned on current date and time.

# -- Start of deprecated comments.
# Calculates time left until date 13/05/2020 and 17:00 Athens time.
# Also calculates how much money earned today and how much money earned
# since the start of the internship.
# -- End of deprecated comments.


from datetime import timedelta
from render_tools import *
from tools import *
import timeit

start_time = timeit.default_timer()
now = datetime.datetime.today()
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
# Sets working dates, weekends
set_dates(first_day_date, last_day_date, corona_start, corona_end)
# Sets holidays.
set_holidays()
# Sets working_status True if working, false if not.
set_working_status(now)

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
output_1 = "Η πρακτική μου τελειώνει σε " + str(tfl[0]) + " χρόνια " \
           + str(tfl[1]) + " μήνες " + str(tfl[2]) + " εβδομάδες " \
           + str(tfl[3]) + " ημέρες " + "\r\n" + 49 * " " \
           + str(tfl[3]) + " ώρες " + str(tfl[4]) + " λεπτά " \
           + str(tfl[5]) + " δευτερόλεπτα " + "\r\n" + 49 * " " \
           + str(tfl[6]) + " χιλιοστά του δευτερολέπτου και " \
           + str(tfl[7]) + " μικροδευτερόλεπτα.\r\n"


output_2 = ""
time_worked_today = 0
# If I am working right now, calculate pay earned today.
if get_working_status():
    # Calculate working time today.
    time_worked_today = now - datetime.datetime(now.year,
                                                now.month,
                                                now.day, 9)
    # Render  message's 2 output.
    output_2 = render_output_2(time_worked_today, pay_per_microsecond_8)

elif not get_working_status():
    if now < work_start:
        time_worked_today = now - now
        output_2 = "\nΑυτήν την στιγμή δεν δουλεύω και αράζω πέτσα. " \
                   "Σε λιγάκι πιάνουμε δουλειά...\r\n"
    elif now > work_end:
        time_worked_today = work_end - work_start
        output_2 = "\nΑυτήν την στιγμή δεν δουλεύω και αράζω πέτσα." \
                   "Σήμερα βγήκε το μεροκάματο των 23,232 ευρώ. \r\n"

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
euro_made = (microseconds_passed+microseconds_passed_off_days) *\
            pay_per_microsecond_8
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
output_3 = "Μηνιαία έχω βγάλει " + str(monthly_wage_earned) + \
           " ευρώ. (Προσοχή! Στο ποσό αυτό συνυπολογίζονται οι 2-5" \
           " μέρες που πληρώνομαι" \
           " κάθε μήνα χωρίς να δουλεύω...)\r\n"
output_4 = "Συνολικά έχω βγάλει " + str(euro_made) + \
           " ευρώ και έχω δουλέψει " + \
           str(days_worked) + \
           " ημέρες, συνυπολογίζοντας την σημερινή.\r\n\r\n"
signature = "Regards,\r\nZois Zogopoulos\r\n"
pySignature = 113 * " " + "This is an automated email from Python.\r\n"

dateString = "Ημερομηνία: " + str(now.date()) + \
             "\r\nΏρα: " + str(now.time()) + "\r\n\r\n"
zois_email = dateString + \
             output_1 + output_2 + output_3 + output_4 + \
             signature + pySignature

print(zois_email)
send_email(zois_email)
stop_time = timeit.default_timer()
execution_time = stop_time - start_time
# It returns time in seconds.
print('-- mailer was Executed in ' + str('{:.4f}'.format(execution_time)) +
      ' seconds --')
