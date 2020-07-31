import sys
from tools import send_solo_email, send_multi_email, send_debug_email

def cli_master(hotmail_email, gmail_email, tag_dictionary):
    if len(sys.argv) == 1:
        print('[DEFAULT]')
        send_multi_email(hotmail_email, gmail_email, tag_dictionary)
    else:
        if len(sys.argv) == 2:
            if sys.argv[1] == '-d':
                print('[DEBUGGING]')
                send_debug_email(hotmail_email)
            elif sys.argv[1] == '-s':
                print('[SOLO-FLY]')
                send_solo_email(hotmail_email, gmail_email)
