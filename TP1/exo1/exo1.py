#/usr/bin/python3

from socket import *
import time

if __name__ == '__main__':


   
    serverName = "10.4.0.7"
    serverPort = 8081
    clientSocket = socket (AF_INET,SOCK_DGRAM)

    try :
        message = "azeaze"
        t = time.process_time()
        clientSocket.sendto (message.encode('utf-8'),(serverName,serverPort))
        message, serverAddress = clientSocket.recvfrom(2048)
        t = time.process_time() - t

        print("time = ",t)
        clientSocket.close()
    except :
        print("exception")
        raise 
    
