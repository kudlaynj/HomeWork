from datetime import datetime
import time
from time import sleep
import threading
from threading import Thread


time_start = datetime.now()


def potok_1():
    for i in range(1, 11):
        print(i)
        sleep(1)


alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


def potok_2():
    for i in alfa:
        print(i)
        sleep(1)


p_1 = threading.Thread(target=potok_1)
p_2 = threading.Thread(target=potok_2)

p_1.start()
p_2.start()

p_1.join()
p_2.join()

time_end = datetime.now()
time_res = time_end - time_start

print(time_res)
