import socket
import sys
import re
import threading
from client_list import ClientInfo

'''
udpSocket - UDP Socket
message - Message to broadcast
clients - list of clients to broadcast the message to

Broadcasts a message to a list of clients on a UDP Socket
'''
def broadcast_message(udpSocket, message, clients):
    #consolidate to a broadcast message method
    print(message)
    for chat_client in clients:
        udpSocket.sendto(bytes(message, 'utf-8'), chat_client)


'''
This method handles whenever a client sends something through a socket.

Called as in thread from the server to handle individual users.
'''
def handle_client(data, caddress, udpSocket, clients):

    print('message: ' + str(caddress))

    broadcast_str = "[" + re.search(r"\, (.*?)\)", str(caddress)).group(1) + "] " + ''.join([char for char in str(data)[2:-3]]) + '\n'

    broadcast_message(udpSocket, broadcast_str, clients)


def Server():


    udpSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udpSocket.bind(("0.0.0.0",6969))

    print('listening for messages yuh')

    clients = [] #list of client caddresses
    client_info = [] #list of ClientInfo objects to make command integration easier
    while True:
        data, caddress = udpSocket.recvfrom(4096)

        if caddress not in clients:
            new_client = ClientInfo(caddress)
            client_info = []
            clients.append(caddress)

            #Send Welcome Message :)
            udpSocket.sendto(bytes("Welcome to my UDP Chat Server!!!\n", 'utf-8'), caddress)

        #Creation of client threads, thus allowing multiple connections to the server
        client_thread = threading.Thread(target=handle_client, args=(data, caddress, udpSocket, clients))
        client_thread.start()

Server()