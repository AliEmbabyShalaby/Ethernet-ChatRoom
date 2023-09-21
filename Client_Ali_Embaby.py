import socket
import threading
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.settimeout(50)
ip_server = '192.168.1.8'
port = 1234

client_socket.connect((ip_server, port))
myname = "Embaby"
client_socket.send(myname.encode('utf-8'))


def receive_messages():
    while True:
        try:
            msg = client_socket.recv(1024).decode('utf-8')
            if msg != ' ':
                print(msg)
            else:
                break
        except Exception as e:
            print("Disconnected from the server.")
            client_socket.close()
            break


def send_msg():
    while True:
        try:
            message = input()
            client_socket.send(message.encode('utf-8'))
        except Exception as e:
            print(e)
            client_socket.close()
            break


receive_thread = threading.Thread(target=receive_messages)
send_thread = threading.Thread(target=send_msg)

receive_thread.start()
send_thread.start()

receive_thread.join()
send_thread.join()
