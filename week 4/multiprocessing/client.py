# 1..10 | ForEach-Object { Start-Process python client.py }
import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 12345))
message = client_socket.recv(1024)
print("Client A received:", message.decode())
client_socket.close()
#input("Press Enter to exit...")
