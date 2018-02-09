#!/usr/bin/env python3
from sys import argv
from socket import *
from threading import * 
import os.path 
import re


#default config
ip_server = "127.0.0.1"
serverPort = 8081
file_index = "image.html"

folder="folder/"
blockSendFile = 1024

# message HTP
messageOk = "HTTP/1.1 200 OK \r\n\r\n"
messagenotFound =  "HTTP/1.1 401 Not Found\r\n\r\n"+" <h1> 404 NOT FOUND  <h1>"


def handle_client_proxy(connectionSocket, address):# thread pour chaque connexion du proxy 

    try :
        message = connectionSocket.recv(1024)
        print(message)
        file = get_file_request(message)
        if exist_file(file) :
            send_file(connectionSocket,file)
        else :
            connectionSocket.send(messagenotFound.encode('utf-8'))
            connectionSocket.close()
    except : # je dois enlever raise 
        if(connectionSocket != None):
            try :
                connectionSocket.close()
            except error :
                raise 
        raise



    
def exist_file(file):# check if file exist or not
    if (file == None) :
        return None
    try:
        if(os.path.exists(folder+file)) :
            print("file exist")
            return True
    except:
        raise Exception("file not existe",file)


def send_file(clientSocket, file):# send file

    realFile = folder+file # concatener because i assume that all file are located in folder 'folder = folder\'
    try:
        with open(realFile,"rb") as f:
            clientSocket.sendall(messageOk.encode('utf-8'))
            clientSocket.sendall(f.read())
    except :
        raise Exception("can't open file "+realFile)
           


    
def get_file_request(messageClient): # string 
    
    myre = re.match("GET /(.*?)\s",messageClient.decode('utf-8')) ; # regex to get file ,any file
    if(myre) :
        if(myre.group(1)):
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
            Thread(target=handle_client_proxy, args=(connectionSocket,address, )).start()
        except KeyboardInterrupt :
            raise
        except error as e  :
            print(e)
