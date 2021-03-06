import datetime
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

import smtplib
import getpass

working_dates = []
weekends = []
holidays = []
working_status = True

# Function getters for global variables.
def get_working_dates():
    return working_dates

def get_weekends():
    return weekends

def get_holidays():
    return holidays

def get_working_status():
    return working_status

def set_dates(first_day, last_day, corona_start, corona_end):
    # Generate all dates between first day of work and first day of
    # Corona-Virus.
    dates_generated_1 = [first_day + datetime.timedelta(days=day_x) for
                         day_x in range(0, (corona_start-first_day).days)]
    # Generate all dates between last day of Corona-Virus and last day
    # of work.
    dates_generated_2 = [corona_end + datetime.timedelta(days=day_x) for
                         day_x in range(1, (last_day-corona_end).days + 1)]
    # Merge lists to create a sum of all generated dates.
    dates_generated = dates_generated_1 + dates_generated_2
    for date in dates_generated:
        if date.weekday() in (5, 6):
            # Append weekends to specified list.
            weekends.append(date)
        elif date.weekday() in holidays:
            # Ignore holidays.
            continue
        else:
            # Append working dates to specified list. Weekend and
            # holidays are not included.
            working_dates.append(date)

def set_working_status(now):
    global working_status
    # No work during holidays.
    for day in holidays:
        if now.date() == day:
            working_status = False
    # No work during weekends.
    for day in weekends:
        if now.date() == day.date():
            working_status = False
    # Variables below are used to set 'working_status' boolean.
    before_work = datetime.datetime(now.year, now.month, now.day,
                                    8, 59, 59, 999999)
    after_work = datetime.datetime(now.year, now.month, now.day,
                                   17, 0, 0, 1)
    if now <= before_work or now >= after_work:
        working_status = False


def time_left(so_many_today):
    tfl = []
    # Generate specified values, according to calculated difference.
    days_left = so_many_today.days
    seconds_left = so_many_today.seconds
    micro_seconds_left = so_many_today.microseconds
    # Generate specified time periods with simple math.
    years_left = days_left // 365
    days_left -= years_left * 365
    months_left = days_left // 30
    days_left -= months_left * 30
    weeks_left = days_left // 7
    days_left -= weeks_left * 7
    hours_left = seconds_left // 60 // 60
    seconds_left -= 60 * 60 * hours_left
    minutes_left = seconds_left // 60
    seconds_left -= 60 * minutes_left
    mil_seconds_left = micro_seconds_left // 1000
    micro_seconds_left -= 1000 * mil_seconds_left
    # Add above time values to 'tfl' list.
    tfl.extend([years_left, months_left, weeks_left, days_left,
                hours_left, minutes_left, seconds_left,
                mil_seconds_left, micro_seconds_left])

    return tfl


def set_holidays():
    global holidays
    holidays = [datetime.date(2019, 12, 25),
                datetime.date(2019, 12, 26),
                datetime.date(2020, 1, 1),
                datetime.date(2020, 1, 6),
                datetime.date(2020, 3, 2),
                datetime.date(2020, 6, 8),
                ]

def paid_days_off(now):
    off_days_paid = 0
    if now.month == 11:
        off_days_paid = 0
    elif now.month == 12:
        off_days_paid = 2.48
    elif now.month == 1:
        off_days_paid = 2.48 + 5
    elif now.month == 2:
        off_days_paid = 2.48 + 5 + 4
    elif now.month == 3:
        off_days_paid = 2.48 + 5 + 4 + 5
    elif now.month == 4:
        off_days_paid = 2.48 + 5 + 4 + 5 + 5
    elif now.month == 5:
        off_days_paid = 2.48 + 5 + 4 + 5 + 5 + 5
    elif now.month == 6:
        off_days_paid = 2.48 + 5 + 4 + 5 + 5 + 5 + 4
    elif now.month == 7:
        off_days_paid = 2.48 + 5 + 4 + 5 + 5 + 5 + 4 + 4
    return off_days_paid

def send_debug_email(input_email):
    # Create message object instance.
    msg = MIMEMultipart('alternative')
    # Setup the parameters of the message.
    msg['From'] = 'zwisss@hotmail.com'
    # Add in the message body.
    # msg.attach(MIMEText(zois_email, 'plain'))
    msg.attach(MIMEText(input_email, "html"))  # DELETE THIS!!!
    server = smtplib.SMTP('smtp.live.com', 587)
    # Hostname to send for this command defaults to the fully qualified
    # domain name of the local host.
    server.ehlo()
    # Puts connection to SMTP server in TLS mode
    server.starttls()
    server.ehlo()
    # Hide password typing from screen.
    server.login('zwisss@hotmail.com', getpass.getpass('Password: '))
    # server.login('zwisss@hotmail.com', 'replace_with_password')
    # Set subject and send the message via the server to maself.
    msg['Subject'] = '[DEBUG] email to maself'
    server.sendmail(msg['From'], 'zwisss@hotmail.com',
                    msg.as_string())
    print('\nDEBUG e-mail to maself was successfully sent.')
    server.quit()

def send_solo_email(hotmail_email, gmail_email):
    solo_email = input('Please gib e-mail: ')
    # Create message object instance.
    message_hotmail = MIMEMultipart('alternative')
    message_gmail = MIMEMultipart('alternative')
    # Setup the parameters of the message.
    message_hotmail['From'] = 'zwisss@hotmail.com'
    message_gmail['From'] = 'zwisss@hotmail.com'
    # Add in the message body.
    # msg.attach(MIMEText(zois_email, 'plain'))
    message_hotmail.attach(MIMEText(hotmail_email, "html"))  # DELETE THIS!!!
    message_gmail.attach(MIMEText(gmail_email, "html"))  # DELETE THIS!!!
    image = MIMEImage(open('assets/army-insignia/stratarxis.png',
                           'rb').read())
    image.add_header('Content-ID', '<army-insignia>')
    message_gmail.attach(image)
    server = smtplib.SMTP('smtp.live.com', 587)
    # Hostname to send for this command defaults to the fully qualified
    # domain name of the local host.
    server.ehlo()
    # Puts connection to SMTP server in TLS mode
    server.starttls()
    server.ehlo()
    # Hide password typing from screen.
    server.login('zwisss@hotmail.com', getpass.getpass('Password: '))
    # Set subject and send the message via the server to maself.
    message_hotmail['Subject'] = 'Very important stuff solarized + ' \
                                 + solo_email
    server.sendmail(message_hotmail['From'], 'zwisss@hotmail.com',
                    message_hotmail.as_string())
    print('\nMail to maself was successfully sent.')
    # Set subject and send the message via the server to one e-mail.
    message_gmail['Subject'] = 'An e-mail from your φρέντ'
    server.sendmail(message_gmail['From'], solo_email,
                    message_gmail.as_string())
    print('Solarized email was successfully sent.')
    server.quit()

def send_multi_email(hotmail_email, gmail_email, tag_dictionary):
    # Create message object instance.
    message_hotmail = MIMEMultipart('alternative')
    message_gmail = MIMEMultipart('alternative')
    # Setup the parameters of the message.
    message_hotmail['From'] = 'zwisss@hotmail.com'
    message_gmail['From'] = 'zwisss@hotmail.com'
    # Add in the message body.
    # msg.attach(MIMEText(zois_email, 'plain'))
    message_hotmail.attach(MIMEText(hotmail_email, "html"))  # DELETE THIS!!!
    message_gmail.attach(MIMEText(gmail_email, "html"))  # DELETE THIS!!!
    image = MIMEImage(open(tag_dictionary['image_path'], 'rb').read())
    image.add_header('Content-ID', '<army-insignia>')
    message_gmail.attach(image)
    server = smtplib.SMTP('smtp.live.com', 587)
    # Hostname to send for this command defaults to the fully qualified
    # domain name of the local host.
    server.ehlo()
    # Puts connection to SMTP server in TLS mode
    server.starttls()
    server.ehlo()
    # Hide password typing from screen.
    server.login('zwisss@hotmail.com', getpass.getpass('Password: '))
    # Set subject and send the message via the server to maself.
    message_hotmail['Subject'] = 'Very important stuff'
    server.sendmail(message_hotmail['From'], 'zwisss@hotmail.com',
                    message_hotmail.as_string())
    print('\nMail to maself was successfully sent.')
    # Send the message via the server to theon.
    server.sendmail(message_hotmail['From'], 'theonzwg@gmail.com',
                    message_hotmail.as_string())
    print('Mail to Porportheon was successfully sent.')
    # Set subject and send the message via the server to pitsimpriko.
    message_gmail['Subject'] = '[Zizizi] Regarding monthly salary.'
    server.sendmail(message_gmail['From'], 'mariannaleventi@gmail.com',
                    message_gmail.as_string())
    print('Mail to PhD student Marianna, was successfully sent.')
    # Set subject and send the message via the server to Hlia.
    message_hotmail['Subject'] = 'Σχετικά με τον μηνιαίο μισθό.'
    server.sendmail(message_hotmail['From'], 'ilias.Anagnostopoulos@intrasoft-intl.com',
                    message_hotmail.as_string())
    print('Mail to Ilia, was successfully sent.')
    # Set subject and send the message via the server to Paan.
    message_gmail['Subject'] = '5 EASY STEPS TO COMPLETELY ANNIHILATE your ' \
                               'opponents on Game of Thrones Board Game ' \
                               'Expansio.'
    server.sendmail(message_gmail['From'], 'gpanag123@gmail.com',
                    message_gmail.as_string())
    print('Mail to Paan, was successfully sent.')
    # Set subject and send the message via the server to Kabremala.
    message_hotmail['Subject'] = 'Beekilling! The new profitable job of' \
                                 'the future.'
    server.sendmail(message_hotmail['From'], 'tzogx@hotmail.com',
                    message_hotmail.as_string())
    print('Mail to Taso, was successfully sent.')
    server.quit()
