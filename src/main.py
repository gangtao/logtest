import logging
import argparse
import time
import random
import string
import multiprocessing

logging.basicConfig(format='%(process)d %(asctime)s %(message)s')


def log(size):
    content = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(size))
    logging.warning('Watch out! %s', content)
    logging.info('I told you so')

def worker(size, interval):
    while True:
        log(size)
        time.sleep(interval)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='sample test logging output')

    parser.add_argument("--s", help="how big the log will be")
    parser.add_argument("--i", help="sleep interval")
    parser.add_argument("--p", help="number of logger process")

    args = parser.parse_args()
    size = int(args.s)
    interval = float(args.i)
    process_number = int(args.p)

    logging.warning('the size is set to %s', size)
    logging.warning('the logging interval is set to %s', interval)
    logging.warning('the processor number is set to %s', process_number)

    jobs = []
    for i in range(process_number):
        p = multiprocessing.Process(target=worker,args=(size,interval,))
        jobs.append(p)
        p.start()
