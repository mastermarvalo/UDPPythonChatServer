# UDP Chat Server using Python
This is a basic chat server written in python to demonstrate the use of UDP protocol and ports to transmit information.

-------
## How to Use
Before clients can chat through the server, it needs to run on a specified port. Afterwards clients can connect with tools such as netcat or telnet (for this example I will be using Windows netcat).

The server includes the following commands:
> /nick - changes the nickname of the client

> /list - lists the nicknames of all connected users

> /quit - Disconnects the client from the server

> /msg [nickname] [message] - PMs a user **DOESNT WORK**


#

### Starting the Server
_chat_server.py_ is the driving file for the entire server and accepts a **port number** as a single argument.

> `$python3 ./chat_server.py port_number`

#

### Starting a Connecting with a netcat Client
Using netcat, use the localhost as the address of your computer if you are running on the same computer, and the local IP if you are running from another client. 

For the port, make sure it is the same on your used to initialize the server.

In order to run netcat in UDP listening mode you need to use the -u flag.
