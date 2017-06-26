
import thread
import time
import Queue


def foo(delay):
    i = 0
    while True:
        i+= 1
        q.put(i)
        time.sleep(delay)
    
def bar(delay):

    while True:
        print(q.get())
        
        time.sleep(delay)
        
    
    
q = Queue.LifoQueue()

thread.start_new_thread(foo, (2,))
thread.start_new_thread(bar, (3,))

input()
