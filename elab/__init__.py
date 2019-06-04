'''

    Common functions used across many lab projects

'''

import sys
import subprocess
import os

CWD = os.getcwd()

def warn(msg):
    '''Write message to standard error'''
    sys.stderr.write(msg + "\n")

def die(msg, errnum=1):
    '''Write message to standard error and then halt'''
    warn(msg)
    sys.exit(errnum)


def syscall(cmd, dieiferr=False, stream=None):
    '''Run a command and return the output.

    Optionally, if stream is provided, the stdout is written to the stream and
    the stderr is written to stderr.

    If an error occurs, the and dieiferr is False, then None is returned for the stdout'''
    try:
        proc = subprocess.Popen(cmd,
                                shell=True,
                                cwd=CWD,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                close_fds=True)
        stderr = proc.stderr.readlines()
        stdout = proc.stdout.readlines()

        if stream is not None:
            stream.write("\n".join([x.strip() for x in stdout]) + "\n")

            warn("\n".join([x.strip() for x in stderr]) + "\n")

        return stdout, stderr
    except subprocess.CalledProcessError as grepexc:
        warn("\n".join([x.strip() for x in stderr]))
        warn(f"ERROR: {cmd}")
        warn(f"error code {grepexc.returncode} {grepexc.output}")

        if dieiferr:
            sys.exit(grepexc.returncode)

    if stream is not None:
        stream.write("\n".join([x.strip() for x in stdout]) + "\n")
    else:
        print("\n".join([x.strip() for x in stderr]) + "\n")
    return None, stderr


if sys.version_info < (3, 0):
    die("This is intended to be used in 3.x")
