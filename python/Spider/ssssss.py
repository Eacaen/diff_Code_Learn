from multiprocessing import Lock, Pool
import time


def function(index):
    print 'Start process: ', index
    time.sleep(index )
    print 'End process', index


if __name__ == '__main__':
    pool = Pool(processes=3)
    for i in xrange(4):
        pool.apply_async(function, (i,))
    pool.close()
    print "Started processes"
    
    pool.join()
    print "Subprocess done."