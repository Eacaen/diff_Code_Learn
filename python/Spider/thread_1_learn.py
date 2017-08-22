# -*- coding: utf-8 -*-

import time, threading

# 新线程执行的代码:
def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(1)
    print 'thread %s ended.' % threading.current_thread().name

print 'thread %s is running...' % threading.current_thread().name
t = threading.Thread(target=loop, name='LoopThread-1')
v = threading.Thread(target=loop, name='LoopThread-2')
t.start()
# t.join()
v.start()

print 'thread %s ended.' % threading.current_thread().name