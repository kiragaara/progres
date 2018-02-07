#!/usr/bin/env python3

from socket import *
import os.path

    

if __name__ == '__main__':

    serverPort = 8081
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serverSocket.bind(("192.168.43.224",serverPort))
    serverSocket.listen(1)
    messageOk = "HTTP/1.1 200 OK \r\n\r\n"
    messagenotFound =  "HTTP/1.1 401 Not Found\r\n\r\n"+" <h1> 404 NOT FOUND  <h1>"
    while 1 :
        connectionSocket, address = serverSocket.accept()

        try :
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
