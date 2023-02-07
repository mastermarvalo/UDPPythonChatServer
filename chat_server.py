import socket
import sys
import re
import threading
from client_list import ClientInfo

'''returns the message to send to a user who used /list'''
def list_clients(client, clients):
    message = 'NAME             SERVER\n'
    for users in clients:
        message += clients[users].get_nickname() + '\n'
    
    return message

'''
udpSocket - UDP Socket
message - Message to broadcast
clients - Dictionary of clients to broadcast the message to

Broadcasts a message to a dict of clients on a UDP Socket.
NEEDS TO BE A DICTIONARY
'''
def broadcast_message(udpSocket, message, clients):
    #consolidate to a broadcast message method
    print(message)
    for chat_client in clients:
        udpSocket.sendto(bytes(message, 'utf-8'), clients[chat_client].get_address())


'''
This method handles whenever a client sends something through a socket.

Called as in thread from the server to handle individual users.
'''
def handle_client(data, client, udpSocket, clients):

    message = ''.join([char for char in str(data)[2:-3]])

    nickname = client.get_nickname()

    print('message: ' + str(message))
    print('nickname: ' + nickname)

    if(message == "/list"): #lists all online users
        broadcast_str = list_clients(client, clients)
        udpSocket.sendto(bytes(broadcast_str, 'utf-8'), client.get_address())

    elif(message == "/quit"): #disconnects user
        broadcast_str = "Disconnecting from server, Goodbye!"
        udpSocket.sendto(bytes(broadcast_str, 'utf-8'), client.get_address())



    elif(message[:6] == "/nick "):
        new_name = message[6:]
        
        broadcast_str = client.get_nickname() + " has changed their nickname changed to " + new_name + "\n"
        client.change_nickname(new_name)
        broadcast_message(udpSocket, broadcast_str, clients)


    else:
        broadcast_str = "[" + nickname + "] " + message + '\n'
        broadcast_message(udpSocket, broadcast_str, clients)


def Server():


    udpSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udpSocket.bind(("0.0.0.0",6969))

    print('listening for messages yuh')

    welcome_file = open("welcome.txt", encoding="utf8")
    welcome_msg = welcome_file.read()
    welcome_file.close()

    print('Welcome message loaded')

    clients = {} #list of client caddresses
    while True:
        data, caddress = udpSocket.recvfrom(4096)

        if caddress not in clients:
            new_client = ClientInfo(caddress)
            clients[caddress] = new_client

            #Send Welcome Message :)
            udpSocket.sendto(bytes(welcome_msg, 'utf-8'), clients[caddress].get_address())
        
            broadcast_message(udpSocket, (clients[caddress].get_nickname() + " has connected to the server\n"), clients)

        client = clients[caddress]
        #Creation of client threads, thus allowing multiple connections to the server
        client_thread = threading.Thread(target=handle_client, args=(data, client, udpSocket, clients))
        client_thread.start()

Server()