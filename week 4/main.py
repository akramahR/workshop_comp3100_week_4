import multiprocessing
import time
import random

def worker(name):
    for i in range(10):
        print(f"Hello from {name}. count: {i}")
        #time.sleep(0.2)
        time.sleep(random.uniform(0, 1))

def worker2():
    for i in range(10):
        p = multiprocessing.current_process()
        print(f"Process Name: {p.name}, PID: {p.pid}. count: {i}")
        #time.sleep(0.2)
        time.sleep(random.uniform(0, 1))

if __name__ == "__main__":
    process = multiprocessing.Process(target=worker, args=("Process 1",))
    process2 = multiprocessing.Process(target=worker, args=("Process 2",))
    process3 = multiprocessing.Process(target=worker2)

    #process.daemon = True
    #process2.daemon = False
    #process3.daemon = True

    process.start()
    process2.start()
    process3.start()
    process.join()
    process2.join()
    process3.join()

    print("some more code")