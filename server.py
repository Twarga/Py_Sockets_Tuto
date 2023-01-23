import socket   
HOST = "192.168.10.6"
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)

while True:
    communication_socket, address = server.accept()
    print(f"Connected to {address}")
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"message from client is : {message}")
    communication_socket.send(f"Got your message ! Thank You ! " .encode('utf-8'))
    communication_socket.close()
    print(f"connection with {address} ended !")
