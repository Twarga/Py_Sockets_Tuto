import socket

HOST = "192.168.10.6"
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST, PORT))

server.send("Hello from client".encode('utf-8'))
print(server.recv(1024).decode('utf-8:'))