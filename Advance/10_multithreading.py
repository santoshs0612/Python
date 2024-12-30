import threading
import time
from concurrent.futures import ThreadPoolExecutor
# indicate some task beaing done

def function(seconds):
    print(f"Sleeping for {seconds}")
    time.sleep(seconds)

def main():
    # Normal code
    time1 = time.perf_counter()
    # function(4)
    # function(2)
    # function(1)
    # time2 = time.perf_counter()
    # print(time2-time1)
    # Same code using threads 
    t1 = threading.Thread(target=function,args=[4])
    t2 = threading.Thread(target=function,args=[2])
    t3 = threading.Thread(target=function,args=[1])

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    time2 = time.perf_counter()
    print(time2-time1)


def poolonDemo():
    with ThreadPoolExecutor() as executer:
        # future1 = executer.submit(function,3)
        # future2 = executer.submit(function,2)
        # future3 = executer.submit(function,1)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())
        l =[3,5,1,2]
        results = executer.map(function,l)
        for result in results:
            print(result)
poolonDemo()
