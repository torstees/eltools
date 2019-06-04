

def warn(msg):
    '''Write message to standard error'''
    sys.stderr.write(f"{msg}\n")

def die(msg, errnum=1):
    '''Write message to standard error and then halt'''
    warn(msg)
    sys.exit(errnum)


