import socket

def Server():
    udpSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    address = udpSocket.bind(('0.0.0.0',12345))

    print('yuh')

    while True:
        data, caddress = udpSocket.recvfrom()
        print(caddress)
        udpSocket.sendto(data,caddress)