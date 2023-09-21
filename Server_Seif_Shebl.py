# server.py
# This code explains how to create a socket object to create a server
import socket
import threading

clientList = []
nicknameList = []

# Create a socket object with IPv4 and TCP socket type
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine's hostname (you can also specify an IP address here)
ip = socket.gethostname()

# Set the port number
port = 1234

# Bind the IP and port to the socket object 's'
s.bind((ip, port))

# Listen for incoming connections with a maximum queue of 3
s.listen(3)

def broadcast(my_client, message):
    for client in clientList:
        if client == my_client:
            continue
        else:
            client.send(message.encode())

def broadcast_withme (message) :
    print(message)
    for client in clientList:
        client.send(message.encode())

def receive(my_client, sender_name):
    my_client.settimeout(40)
    while True:
        try:
            message = my_client.recv(1024).decode()
       #     print(sender_name+':'+message)
            broadcast(my_client, sender_name+':'+message)
        except:
            clientList.remove(my_client)
            nicknameList.remove(sender_name)
            print(sender_name + " disconnected!!")
            my_client.close()
            break



def accept():
    while True:
        client,address = s.accept()
        client.settimeout(10)
        try:
            client.send("Please send your name".encode('utf-8'))
            sender_name = client.recv(1024).decode()
            client.settimeout(None)
            clientList.append(client)
            # print(message)
            nicknameList.append(sender_name)
            broadcast_withme(sender_name + " is connected")
            client_thread = threading.Thread(target=receive, args=(client, sender_name,))
            client_thread.start()
        except:
            client.send("Can not connect,Please try again".encode('utf-8'))
            continue



accept_thread = threading.Thread(target=accept)
# receive_thread = threading.Thread(target=receive)

accept_thread.start()
