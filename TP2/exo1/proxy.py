#!/usr/bin/env python3

from socket import *
from sys import argv

ip_server = "127.0.0.1"
port_ip = "8081"

ip_proxy = "127.0.0.1"
port_proxy = "8082"





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
            print("connection :")
            message = connectionSocket.recv(1024)
            
            file  = message[5:13] # file toto.txt localhost:8080/toto.txt
            with open(file) as f:
                read_data = f.read()
                print("message to send : ",read_data)
                connectionSocket.send(messageOk.encode('utf-8')+read_data.encode('utf-8'))
                connectionSocket.close()
        except:
            print("execption")
            connectionSocket.send(messagenotFound.encode('utf-8'))
            connectionSocket.close()
