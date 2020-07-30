import sys
from tools import send_solo_email, send_multi_email, send_debug_email

def cli_master(input_mail):
    if len(sys.argv) == 1:
        print('[DEFAULT]')
        send_multi_email(input_mail)
    else:
        if len(sys.argv) == 2:
            if sys.argv[1] == '-d':
                print('[DEBUGGING]')
                send_debug_email(input_mail)
            elif sys.argv[1] == '-s':
                print('[SOLO-FLY]')
                send_solo_email(input_mail)
