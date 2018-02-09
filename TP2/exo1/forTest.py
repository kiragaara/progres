#!/usr/bin/env python3
from sys import argv
from socket import *
import os.path


folder="folder/"
block = 5


def send_file(file):

    realFile = folder+file
    size = os.path.getsize(realFile)
    print("sizefile = ",size)
    cpt = 0
    try:
        print(realFile)
        with open(realFile) as f:
            while cpt < size:
                print(f.read(block))
                cpt += block
    except :
        raise 
    

if __name__ == '__main__':

    try:
        send_file("fichier1")
        print("fin fichier1")
        send_file("fichier2")
        print("fin de fichier 2")
    except :
        raise
    print("end")
