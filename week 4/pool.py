import multiprocessing
from multiprocessing import Pool
import time

def square(x):
    p = multiprocessing.current_process()
    time.sleep(1)
    print(f"Process Name: {p.name}, PID: {p.pid}, result:{x * x}")
    return x * x

if __name__ == "__main__":
    with Pool(4) as pool:
        results = pool.map(square, [1, 2, 3, 4, 5])
    print(results)