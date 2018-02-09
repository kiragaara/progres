#!/usr/bin/env python3
from threading import * 
from socket import *
from sys import argv

ip_server = "127.0.0.1"
port_server = 8081

ip_proxy = "127.0.0.1"
port_proxy = 8082

delay = 0.3
#def handle_proxy():# le proxy se connecte au server


def connexion_server(): # proxy connecte to server
    try :
        clientSocket = socket(AF_INET,SOCK_STREAM)
        clientSocket.connect((ip_server,port_server))
        return clientSocket
    except :
        raise

    

def handle_server(socketClient,addressclient,socketproxy):
    try : 
        message = socketClient.recv(1024)
        socketproxy.sendall(message) # envoi server
        while 1 :
            socketproxy.settimeout(delay)
            message =  socketproxy.recv(1024)
            socketClient.sendall(message)
            if(len(message) == 0):
                break
        socketClient.close()
        socketproxy.close()
           
    except  :
        socketClient.close()
        socketproxy.close()
        raise

def handle_client(connectionSocket,address):# thread client  avoir l adress client
    try :
        socketserver = connexion_server()
        Thread(target=handle_server, args=(connectionSocket,address,socketserver, )).start()

    except : # je dois enlever raise 
        if(connectionSocket != None):
            try :
                connectionSocket.close()
            except error :
                raise 
        raise

    



if __name__ == '__main__':

    if(len(argv) == 3):
        ip_server = argv[1]
        serverPort = int(argv[2])
        

    serverPort = 8081
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serverSocket.bind((ip_proxy,port_proxy))
    serverSocket.listen(6)



    while 1 :
        try :
            connectionSocket, address = serverSocket.accept()
            Thread(target=handle_client, args=(connectionSocket,address, )).start()
        except KeyboardInterrupt :
            print("execption")
            connectionSocket.close()
            raise 
