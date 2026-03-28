import multiprocessing
import time

def worker(lock, shared_value, name):
    for _ in range(5):
        with lock:
            current = shared_value.value
            print(f"{name} read value: {current}")
            time.sleep(0.5)
            shared_value.value = current + 1
            print(f"{name} updated value to: {shared_value.value}")

if __name__ == "__main__":
    lock = multiprocessing.Lock()
    shared_value = multiprocessing.Value('i', 0)

    p1 = multiprocessing.Process(target=worker, args=(lock, shared_value, "Process 1"))
    p2 = multiprocessing.Process(target=worker, args=(lock, shared_value, "Process 2"))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Final value:", shared_value.value)