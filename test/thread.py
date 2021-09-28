from threading import *
import time

tmp = 5


def MyThread1():
    global tmp
    while tmp > 0:
        time.sleep(1)
        tmp -= 1


def MyThread2():
    global tmp
    while tmp > 0:
        print(tmp)
        time.sleep(0.2)


t1 = Thread(target=MyThread1, args=[])
t2 = Thread(target=MyThread2, args=[])

t1.start()
t2.start()
