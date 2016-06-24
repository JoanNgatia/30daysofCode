# import sys

S = raw_input().strip()


def check_string(s):
    try:
        y = int(s)
        print y
    except ValueError:
        print 'Bad String'

check_string(S)
