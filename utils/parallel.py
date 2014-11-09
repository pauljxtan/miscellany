#!/usr/bin/env python

"""
A simple server for parallel processing of input functions.
"""

# TODO:
#     documentation!
#     add timers
#     add support for kwargs

import multiprocessing

class Server(object):
    def __init__(self, func, args, n_threads=None, verbose=False):
        self.func = func
        self.args = args
        self.n_calls = len(args)
        self.n_threads = n_threads
        if n_threads == None:
            # Use maximum number of threads
            self.n_threads = multiprocessing.cpu_count()
        self.verbose = verbose

        self.n_jobs = 0
        self.n_results = 0
        self.jobs = []
        self.results = [None for i, v in enumerate(args)]
        self.queue = multiprocessing.Queue()

        self.__do_jobs()

    def __begin_job(self):
        args = [self.func, self.queue, self.n_jobs]
        args += list(self.args[self.n_jobs])

        if self.verbose:
            print "Beginning job", self.n_jobs
        
        job = multiprocessing.Process(target=wrapper, args=args)
        job.start()

        self.jobs.append(job)

        self.n_jobs += 1

        return job

    def __get_result(self):
        result = self.queue.get()
        ijob = result["ijob"]
        self.results[ijob] = result

        if self.verbose:
            print "Got result for job", ijob

        self.jobs[ijob].join()

        #if self.verbose:
        #    print "Joined job", ijob

        self.n_results += 1

        return result
    
    def __do_jobs(self):
        # First batch
        for i in range(min(self.n_threads, self.n_calls)):
            self.__begin_job()

        # Later batches
        while self.n_results < self.n_jobs:
            self.__get_result()
            if self.n_jobs < self.n_calls:
                self.__begin_job()

        # Clean-up
        for job in self.jobs:
            job.join()

    def get_results(self):
        results = [d["results"] for d in self.results]
        return results

def wrapper(func, queue, ijob, *args):
    result = func(*args)
    results = dict(args=args, results=result, ijob=ijob)
    
    queue.put(results)
    queue.close()

    print "Placed job %d on queue" % ijob

if __name__ == "__main__":
    import random
    import time

    def test(num, t):
        time.sleep(t)
        return num, t

    test_args = [[i, random.random()] for i in range(20)]

    server = Server(test, test_args, n_threads=2, verbose=True)
    results = server.get_results()
    print
    print test_args
    print results
