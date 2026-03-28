import multiprocessing

def producer(q):
    q.put("Hello from producer")

def consumer(q):
    message = q.get()
    print("Consumed:", message)

if __name__ == "__main__":
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=producer, args=(q,))
    p2 = multiprocessing.Process(target=consumer, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()