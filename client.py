import socket
import sys
import threading

if len(sys.argv) != 3 :
    print(f"Now using : {sys.argv[0]} <IP> <Port>")
    exit()

IP = sys.argv[1]
PORT = int(sys.argv[2])

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((IP, PORT))

def sendMessage():
    while True:
        msg = input()
        server.send(msg.encode())

def recvMessage():
    while True:
        msg = server.recv(2048)
        if msg:
            print(msg.decode())
            
thread_sendMessage = threading.Thread(target=sendMessage)
thread_sendMessage.start()

thread_recvMessage = threading.Thread(target=recvMessage)
thread_recvMessage.start()