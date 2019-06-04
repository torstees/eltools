#!/usr/bin/env python
'''Run N jobs from a set of files'''

import subprocess
import queue
import threading
import argparse
import time
import logging

import elab

JOBS_FAILED = False


class Shell(threading.Thread):
    '''Simple abstraction for a single thread'''
    def __init__(self, thequeue):
        '''initialize with a single queue for this "thread"'''
        threading.Thread.__init__(self)
        self.queue = thequeue

    def run(self):
        '''Run the job's specified'''
        global JOBS_FAILED
        while not self.queue.empty():
            job_count = self.queue.qsize()
            job = self.queue.get(block=False)
            logging.info("Running %s #%d out of %d", job, job_count, self.queue.qsize())
            try:
                subprocess.check_call(job.split(" "))
                logging.info("Job completed: %s", job)
            except subprocess.CalledProcessError as err:
                JOBS_FAILED = True
                elab.warn(f"FAILED: {job} {err}")
                logging.error("FAILED: %s %s", job, err)
            logging.info("Task completed (%s)", job)
            self.queue.task_done()
        logging.info("queue emptied. Shutting down")

def main():
    '''This is the actual main function'''
    parser = argparse.ArgumentParser(description="Run N jobs from a set of files")
    parser.add_argument("--job-count", type=int, default=4,
                        help="Max number of jobs to run at once")
    parser.add_argument("filenames", type=str, metavar="Filename", nargs="+",
                        help="One or more files containing commands to be run in parallel")
    parser.add_argument("--log-name", type=str, default=None, help="name of log to write to")
    parser.add_argument("--sleep", type=int, default=5,
                        help='Number of seconds to sleep (defaults to 5)')

    args = parser.parse_args()
    if args.log_name is None:
        args.log_name = "%s-%s.log" % (
            time.strftime("%H:%M:%S"),
            args.filenames[0].split(".")[0].split("/")[-1])
    logging.basicConfig(filename=args.log_name)
    for file in args.filenames:
        if not JOBS_FAILED:
            que = queue.Queue()
            for line in open(file):
                if line[0] != "#":
                    que.put(line.strip())
            logging.info("Total lines found: %d", que.qsize)
            for i in range(0, args.job_count):
                thr = Shell(que)
                thr.start()
                time.sleep(args.sleep)
            elab.warn(f"{args.job_count} jobs have been launched. ")
            que.join()
        else:
            elab.warn("Well, one or more jobs died. So we will not continue with the next file")
