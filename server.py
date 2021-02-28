import socket
import sys
import threading

#IP address = 127.0.0.1
#PORT NUMBER = 20000 + 03016 (6130301621) = 23016

if len(sys.argv) != 3 :
    print(f"Now using : {sys.argv[0]} <IP> <Port>")
    exit()

IP = sys.argv[1]
PORT = int(sys.argv[2])

connections = []

def clientThreadFunc(conn, addr):
    conn.send(b"You are in the chat")
    while True:
        try: 
            message = conn.recv(2048)
            if message:
                msg = f"<{addr[0]}_{addr[1]}>  : {message.decode()}"
                print(msg)
                broadcast(msg.encode(), conn)
        except:
            exit()

def broadcast(msg, sender):
    for cli_conn in connections:
        if cli_conn != sender:
            try:
                cli_conn.send(msg)
            except:
                cli_conn.close()
                remove(cli_conn)

def remove(conn):
    if conn in connections:
        connections.remove(conn)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((IP, PORT))
server.listen(10)
print(f"Listening to: {IP}_{PORT}")

#main loop
while True:
    conn, addr = server.accept()
    connections.append(conn)
    print(f"{addr} has connected")
    
    thread_client = threading.Thread(target=clientThreadFunc, args=((conn, addr)))
    thread_client.start()