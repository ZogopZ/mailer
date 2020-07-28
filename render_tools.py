def render_date(now):
    date_string = 'Ημερομηνία: ' + str(now.date()) + '\r\n' + \
                  'Ώρα: ' + str(now.time()) + '\r\n'
    date_html = """
    <p>Ημερομηνία: {0}<br>Ώρα: {1}</p>
    """.format(str(now.date()), str(now.time()))
    return [date_string, date_html]

def render_signatures():
    signatures_string = 'Regards,\r\nZois Zogopoulos\r\n' + \
                        113 * ' ' + \
                        'This is an automated email from Python.\r\n'
    signatures_html = """
    <p>Regards,<br>Zois Zogopoulos</p>
    <p><br></p>
    <p style="font-size:12px">If you have any suggestions please contact 
    support:<br>
        <ul style="font-size:12px">    
            <li>on mobile call zois by pressing 
                <a href="tel:6979156833">here</a>.
            </li>
            <li>or send an email by pressing 
                <a href="mailto:zwisss@hotmail.com">here</a>.
            </li>
        </ul>
    </p>
    <p style="text-align:right">This is an automated email from Python.</p>
    """
    return [signatures_string, signatures_html]


def render_time(tfl):
    time_string = 'Η πρακτική μου τελειώνει σε ' + \
                  str(tfl[0]) + ' χρόνια ' + \
                  str(tfl[1]) + ' μήνες ' + \
                  str(tfl[2]) + ' εβδομάδες ' + \
                  str(tfl[3]) + ' ημέρες' + '\r\n' + \
                  28 * ' ' + \
                  str(tfl[3]) + ' ώρες ' + \
                  str(tfl[4]) + ' λεπτά ' + \
                  str(tfl[5]) + ' δευτερόλεπτα ' + '\r\n' + \
                  28 * ' ' + \
                  str(tfl[6]) + ' χιλιοστά του δευτερολέπτου και ' + \
                  str(tfl[7]) + ' μικροδευτερόλεπτα.'
    time_html = """
                <table cellspacing="0" cellpadding="0">
                <tbody>
                <tr><td>&nbsp;</td></tr>
                <tr>
                    <td>Η πρακτική μου τελειώνει σε</td>
                    <td>&ensp;</td>
                    <td>
                        <table>
                        <tbody>
                        <tr>
                            <td>{0} χρόνια</td>
                            <td>{1} μήνες</td>
                            <td>{2} εβδομάδες</td>
                            <td>{3} ημέρες</td>
                        </tr>
                        </tbody>
                        </table>
                    </td>
                </tr>
                <tr>                        
                    <td></td>
                    <td></td>
                    <td>
                        <table>
                        <tbody>
                        <tr>
                            <td>{4} ώρες</td>
                            <td>{5} λεπτά</td>
                            <td>{6} δευτερόλεπτα</td>
                        </tr>
                        </tbody>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td></td>
                    <td></td>
                    <td>
                       <table>
                       <tbody>
                        <tr>
                            <td>{7} χιλιοστά του δευτερολέπτου και</td>
                            <td>{8} μικροδευτερόλεπτα.</td>
                        </tr>
                        </tbody>
                        </table>
                    </td>
                </tr>
                </tbody>
                </table>
                """.format(str(tfl[0]), str(tfl[1]), str(tfl[2]), str(tfl[3]),
                           str(tfl[4]), str(tfl[5]), str(tfl[6]),
                           str(tfl[7]), str(tfl[8]))
    return [time_string, time_html]

def render_title(title_list):
    title_string = 'Τίτλος:' + ' ' + \
                   title_list[0] + \
                   ' Ζώης Ζωγόπουλος\r\n'
    title_html = '<table><tbody><tr><td>Τίτλος:</td>' + \
                 '<td>' + title_list[0] + '</td>' + \
                 '<td>Ζώης Ζωγόπουλος</td>' + \
                 '<td>&ensp;</td>' + \
                 '<td>' + title_list[2] + '</td>' + \
                 '</tr></tbody></table>'
    return [title_string, title_html]

def render_total(euro_made, days_worked):
    total_string = 'Συνολικά έχω βγάλει ' + str(euro_made) + \
                   ' ευρώ και έχω δουλέψει ' + \
                   str(days_worked) + \
                   ' ημέρες, συνυπολογίζοντας την σημερινή.\r\n'
    total_html = """
    Συνολικά έχω βγάλει {0} ευρώ και έχω δουλέψει {1} ημέρες, συνυπολογίζοντας
    την σημερινή.</p>
    """.format(str(euro_made), str(days_worked))
    return [total_string, total_html]

def render_wage(monthly_wage_earned):
    wage_string = 'Μηνιαία έχω βγάλει ' + str(monthly_wage_earned) + \
                  ' ευρώ. (Προσοχή! Στο ποσό αυτό συνυπολογίζονται οι 2-5' \
                  ' μέρες που πληρώνομαι' \
                  ' κάθε μήνα χωρίς να δουλεύω...)'
    wage_html = """
    Μηνιαία έχω βγάλει {0} ευρώ. (Προσοχή! Στο ποσό αυτό συνυπολογίζονται οι
    2-5 μέρες που πληρώνομαι κάθε μήνα χωρίς να δουλεύω...)<br>
    """.format(str(monthly_wage_earned))
    return [wage_string, wage_html]

def render_work(time_worked_today, pay_per_microsecond_8):
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
                             + 'δευτερόλεπτα'
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
        <p>Σήμερα έχω ήδη βγάλει {0} ευρώ και έχω δουλέψει {1} {2} {3}.<br>
        """.format(str(euro_made_today), hours_string, minutes_string,
                   seconds_string)
    return [work_string, work_html]
