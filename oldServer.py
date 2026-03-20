import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))
server_socket.listen()

print("Server is listening on port 12345...")

while True:
    conn, addr = server_socket.accept()
    print(f"Connection established with {addr}")
    conn.sendall(b"Hello from server!")
    conn.close()

