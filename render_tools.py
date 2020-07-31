import jinja2
import title_tools


def render_datetime(now, input_dictionary):
    date_string = 'Ημερομηνία: ' + str(now.date()) + '\r\n' \
                  + 'Ώρα: ' + str(now.time()) + '\r\n'
    input_dictionary.update({'date': now.date(),
                             'time': now.time()})
    return date_string


def render_signatures():
    signatures_string = 'Regards,\r\nZois Zogopoulos\r\n' \
                        + 113 * ' ' \
                        + 'This is an automated email from Python.\r\n'
    return signatures_string


def render_time(tfl, input_dictionary):
    time_string = 'Η πρακτική μου τελειώνει σε ' \
                  + str(tfl[0]) + ' χρόνια ' \
                  + str(tfl[1]) + ' μήνες ' \
                  + str(tfl[2]) + ' εβδομάδες ' \
                  + str(tfl[3]) + ' ημέρες' + '\r\n' \
                  + 28 * ' ' \
                  + str(tfl[4]) + ' ώρες ' \
                  + str(tfl[5]) + ' λεπτά ' \
                  + str(tfl[6]) + ' δευτερόλεπτα ' + '\r\n' \
                  + 28 * ' ' \
                  + str(tfl[7]) + ' χιλιοστά του δευτερολέπτου και ' \
                  + str(tfl[8]) + ' μικροδευτερόλεπτα.'
    input_dictionary.update({'years': tfl[0],
                             'months': tfl[1],
                             'weeks': tfl[2],
                             'days': tfl[3],
                             'hours': tfl[4],
                             'minutes': tfl[5],
                             'seconds': tfl[6],
                             'milliseconds': tfl[7],
                             'microseconds': tfl[8]})
    return time_string

def render_title(user_titles, input_dictionary):
    title_string = 'Τίτλος: ' \
                   + user_titles.title + ' ' \
                   + 'Ζώης Ζωγόπουλος ' \
                   + '+ image at ' + '\'' + user_titles.image_path + '\'\n'
    input_dictionary.update({'title': user_titles.title,
                             'image_path': user_titles.image_path,
                             'encoded_image': user_titles.encoded_image})
    return title_string

def render_total(euro_made, days_worked, input_dictionary):
    total_string = 'Συνολικά έχω βγάλει ' + str(euro_made) \
                   + ' ευρώ και έχω δουλέψει ' \
                   + str(days_worked) \
                   + ' ημέρες, συνυπολογίζοντας την σημερινή.\r\n'
    total_html = """
    Συνολικά έχω βγάλει {0} ευρώ και έχω δουλέψει {1} ημέρες, συνυπολογίζοντας
    την σημερινή.</p>
    """.format(str(euro_made), str(days_worked))
    input_dictionary['total'] = total_html
    return total_string

def render_wage(monthly_wage_earned, input_dictionary):
    wage_string = 'Μηνιαία έχω βγάλει ' + str(monthly_wage_earned) \
                  + ' ευρώ. (Προσοχή! Στο ποσό αυτό συνυπολογίζονται οι 2-5' \
                  + ' μέρες που πληρώνομαι κάθε μήνα χωρίς να δουλεύω...)'
    wage_html = """
    Μηνιαία έχω βγάλει {0} ευρώ. (Προσοχή! Στο ποσό αυτό συνυπολογίζονται οι
    2-5 μέρες που πληρώνομαι κάθε μήνα χωρίς να δουλεύω...)<br>
    """.format(str(monthly_wage_earned))
    input_dictionary['wage'] = wage_html
    return wage_string

def render_work(time_worked_today, pay_per_microsecond_8, input_dictionary):
    work_evaluator = str(time_worked_today)
    work_string = ''
    work_html = ''
    if work_evaluator == '8:00:00':
        work_string += 'Αυτήν την στιγμή δεν δουλεύω και αράζω πέτσα.' \
                       + 'Σήμερα βγήκε το μεροκάματο των 23,232 ευρώ.'
        work_html = """
        Αυτήν την στιγμή δεν δουλεύω και αράζω πέτσα. Σήμερα βγήκε το
        μεροκάματο των 23,232 ευρώ.<br>
        """
    elif work_evaluator == '0:00:00':
        work_string += 'Αυτήν την στιγμή δεν δουλεύω και αράζω πέτσα. ' \
                       + 'Σε λιγάκι πιάνουμε δουλειά...'
        work_html = """
        Αυτήν την στιγμή δεν δουλεύω και αράζω πέτσα. Σε λιγάκι πιάνουμε
        δουλειά...<br>
        """
    else:
        # Convert time worked to microseconds.
        microseconds_passed_today = \
            time_worked_today.total_seconds() * (10**6)
        # Convert time worked to seconds.
        seconds_worked_today = time_worked_today.total_seconds()
        remaining_seconds = seconds_worked_today
        # Calculate integer hours worked.
        hours_worked_today = int(remaining_seconds / (60*60))
        hours_string = ''
        # Need for plural output.
        if hours_worked_today > 1 or hours_worked_today == 0:
            hours_string = ' ' + str(hours_worked_today) + ' ώρες'
        # Need for singular output.
        elif hours_worked_today == 1:
            hours_string = ' ' + str(hours_worked_today) + ' ώρα'
        remaining_seconds -= hours_worked_today * (60*60)
        # Calculate integer minutes worked.
        minutes_worked_today = int(remaining_seconds / 60)
        minutes_string = ''
        # Need for plural output.
        if minutes_worked_today > 1 or minutes_worked_today == 0:
            minutes_string = ' ' + str(minutes_worked_today) + ' λεπτά'
        # Need for singular output.
        elif minutes_worked_today == 1:
            minutes_string = ' ' + str(minutes_worked_today) + ' λεπτό'
        remaining_seconds -= minutes_worked_today * 60
        # Calculate integer seconds worked.
        seconds_worked_today = int(remaining_seconds)
        seconds_string = ''
        # Need for plural output.
        if seconds_worked_today > 1 or seconds_worked_today == 0:
            seconds_string = ' και ' + str(seconds_worked_today) \
                             + ' δευτερόλεπτα'
        # Need for singular output.
        elif seconds_worked_today == 1:
            seconds_string = ' και ' + str(seconds_worked_today) \
                             + 'δευτερόλεπτο'
        euro_made_today = microseconds_passed_today * pay_per_microsecond_8
        work_string = 'Σήμερα έχω ήδη βγάλει ' \
                      + str(euro_made_today) + ' ευρώ' \
                      + ' και έχω δουλέψει' \
                      + hours_string + minutes_string + seconds_string + '.'
        work_html = """
        Σήμερα έχω ήδη βγάλει {0} ευρώ και έχω δουλέψει {1} {2} {3}.<br>
        """.format(str(euro_made_today), hours_string, minutes_string,
                   seconds_string)
        input_dictionary['work'] = work_html
    return work_string

def populate_template(input_dictionary):
    with open('assets/templates/template_hotmail.html', 'r') as template_file, \
            open('ignore/hotmail.html', 'w+') as output_file:
        html_in = template_file.read()
        jinja_template = jinja2.Template(html_in)
        html_out = jinja_template.render(
            date=input_dictionary['date'],
            time=input_dictionary['time'],
            title=input_dictionary['title'],
            base64_content=input_dictionary['encoded_image'],
            years=input_dictionary['years'],
            months=input_dictionary['months'],
            weeks=input_dictionary['weeks'],
            days=input_dictionary['days'],
            hours=input_dictionary['hours'],
            minutes=input_dictionary['minutes'],
            milliseconds=input_dictionary['milliseconds'],
            microseconds=input_dictionary['microseconds'],
            work=input_dictionary['work'],
            wage=input_dictionary['wage'],
            total=input_dictionary['total'])
        output_file.write(html_out)
    with open('assets/templates/template_gmail.html', 'r') as template_file,\
            open('ignore/gmail.html', 'w+') as output_file:
        html_in = template_file.read()
        jinja_template = jinja2.Template(html_in)
        html_out = jinja_template.render(
            date=input_dictionary['date'],
            time=input_dictionary['time'],
            title=input_dictionary['title'],
            base64_content=input_dictionary['encoded_image'],
            years=input_dictionary['years'],
            months=input_dictionary['months'],
            weeks=input_dictionary['weeks'],
            days=input_dictionary['days'],
            hours=input_dictionary['hours'],
            minutes=input_dictionary['minutes'],
            milliseconds=input_dictionary['milliseconds'],
            microseconds=input_dictionary['microseconds'],
            work=input_dictionary['work'],
            wage=input_dictionary['wage'],
            total=input_dictionary['total'])
        output_file.write(html_out)
    return
