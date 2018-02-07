#!/usr/bin/env python3

from socket import *
import os.path


def checkFile(file):
    return os.path.isfile(file)
    

if __name__ == '__main__':
    
    serverPort = 6969
    serverSocket = socket(AF_INET,SOCK_DGRAM)
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serverSocket.bind(("127.0.0.1",serverPort))
    

    while 1 :
        try :
            print("begin")
            message, clientaddr = serverSocket.recvfrom(1024) 
            print(message)
        except :
            print("exception")


