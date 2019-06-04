'''

    Common functions used across many lab projects

'''

import sys


def warn(msg):
    '''Write message to standard error'''
    sys.stderr.write(msg + "\n")

def die(msg, errnum=1):
    '''Write message to standard error and then halt'''
    warn(msg)
    sys.exit(errnum)




if sys.version_info < (3, 0):
    die("This is intended to be used in 3.x")
