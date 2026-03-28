import multiprocessing

def worker(conn):
    conn.send("Hello from child")
    conn.close()

if __name__ == "__main__":
    parent_conn, child_conn = multiprocessing.Pipe()

    p = multiprocessing.Process(target=worker, args=(child_conn,))
    p.start()

    print(parent_conn.recv())  # receive message

    p.join()