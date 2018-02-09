#!/usr/bin/env python3
from sys import argv
from socket import *
import os.path 
import re


#default config
ip_server = "127.0.0.1"
serverPort = 8081
file_index = "index.html"

folder="folder/index.html"
blockSendFile = 1024

# message HTTP
messageOk = "HTTP/1.1 200 OK \r\n\r\n"
messagenotFound =  "HTTP/1.1 401 Not Found\r\n\r\n"+" <h1> 404 NOT FOUND  <h1>"


def exist_file(file):# check if file exist or not
    try:
        print(file)
        if(os.path.exists(folder+file)) :
            return True
    except:
        raise Exception("file not existe",file)


def send_file(clientSocket, file):# send file

    realFile = folder+file # concatener because i assume that all file are located in folder 'folder = folder\'
    cpt = 0
    try:
        size = os.path.getsize(realFile)
        with open(realFile) as f:
            while cpt < size :
                clientSocket.sendall(messageOk.encode('utf-8'))
                clientSocket.sendall(f.read(blockSendFile).encode('utf-8'))
                cpt += blockSendFile
    except :
        raise Exception("can't open file")
           

def get_file_request(messageClient): # string 
    
    myre = re.match("GET /(.*?)\s",messageClient.decode('utf-8')) ; # regex to get file ,any file
    if(myre) : 
        return myre.group(1)
    return file_index # principal page 

if __name__ == '__main__':


    if(len(argv) == 3):
        ip_server = argv[1]
        serverPort = int(argv[2])

    connectionSocket = None 

    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serverSocket.bind((ip_server,serverPort))
    serverSocket.listen(1)
    while True :
        try :
            connectionSocket, address = serverSocket.accept()
            print("connection :")
            message = connectionSocket.recv(1024)
            print(message)
            # file  = message[5:13] # file toto.txt localhost:8080/toto.txt
            file = get_file_request(message)
            if exist_file(file) :
                send_file(connectionSocket,file)

        
            connectionSocket.close()
        except:
            if(connectionSocket != None):
                connectionSocket.send(messagenotFound.encode('utf-8'))
                connectionSocket.close()
                raise # for debug je dois l enlever a la fin 
