import threading, time
def now() :
	
	return str( time.strftime( '%Y-%m-%d %H:%M:%S' , time.localtime() ) )
def func1():
	print threading.current_thread().name ,'\n'
	print 'start func1: ' + now() + "\n"
	time.sleep(5)
	print 'stop func1: ' + now() + "\n"

def func2():
    print threading.current_thread().name ,'\n'	
    print 'start func2: ' + now() + "\n"
    time.sleep(1)
    print 'stop func2: ', now() + "\n"
thtsk = []
thread1 = threading.Thread(target = func1)
thread1.start()
thtsk.append(thread1)
thread2 = threading.Thread(target = func2)
thread2.start()
thtsk.append(thread2)

print 'start join: ' + now() + "\n"

print threading.current_thread().name ,'\n'
thread1.join()
print threading.current_thread().name ,'\n'
thread2.join()

print 'here------------------\n'
# for thd in thtsk:
# 	print threading.current_thread().name ,'\n'
# 	thd.join()
print 'end join: ' + now() + "\n"