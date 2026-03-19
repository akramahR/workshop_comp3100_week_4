import socket
import multiprocessing

HOST = "localhost"
PORT = 12345

def handle_client(conn, addr):
    """Function to handle a single client connection."""
    print(f"[Process {multiprocessing.current_process().pid}] Connected by {addr}")
    try:
        conn.sendall(f"Hello from process {multiprocessing.current_process().pid}!".encode())
    except Exception as e:
        print(f"[Process {multiprocessing.current_process().pid}] Error: {e}")
    finally:
        conn.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server listening on {HOST}:{PORT}...")

    try:
        while True:
            conn, addr = server_socket.accept()
            print(f"Accepted connection from {addr}")

            process = multiprocessing.Process(target=handle_client, args=(conn, addr))
            process.daemon = True
            process.start()

            conn.close()  # Close in parent process
    except KeyboardInterrupt:
        print("\nServer shutting down...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()