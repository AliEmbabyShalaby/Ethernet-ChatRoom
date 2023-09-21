# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import threading
import socket


# This code explains how to create a socket object to create a client

def client_rec():
    # Receive message from the server
    while 1:
        try:
            message = s.recv(1024)
            print(message.decode())
        except:
            print("Disconnected from server")
            break


def client_send():
    rec_thread = threading.Thread(target=client_rec)
    rec_thread.start()
    while 1:
        data = input()
        s.send(data.encode("utf-8"))


# AF_Inet for IPV4 and SOCK_STREAM for TCP/IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(20)

# write the server IP and port number
ip = "192.168.191.195"
port = 1234
# connect to the server
try:
    print(f"Attempting connection to {ip}...")

    s.connect((ip, port))
    print(f"Connected to {ip}")

    client_send()

except socket.timeout:
    print("Server is unreachable")
