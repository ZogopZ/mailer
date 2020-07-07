def render_output_2(time_worked_today, pay_per_microsecond_8):
    # Convert time worked to microseconds.
    microseconds_passed_today = time_worked_today.total_seconds() * (10**6)
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
        seconds_string = ' και ' + str(seconds_worked_today) + ' δευτερόλεπτα'
    # Need for singular output.
    elif seconds_worked_today == 1:
        seconds_string = ' και ' + str(seconds_worked_today) + ' δευτερόλεπτο'
    euro_made_today = microseconds_passed_today * pay_per_microsecond_8
    output_2 = 'Σήμερα έχω ήδη βγάλει ' + \
               str(euro_made_today) + ' ευρώ' + \
               ' και έχω δουλέψει' + \
               hours_string + minutes_string + seconds_string + '.\r\n'
    return output_2
