#Video 3 - Cliente

import socket
import time
import pickle

HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),1236))

while  True:
    full_msg = b''
    new_msg = True
    while True:
            msg = s.recv(16)
            if new_msg:
                print(f"comprimento de new_msg: {msg[:HEADERSIZE]}")
                msglen = int(msg[:HEADERSIZE])
                new_msg = False

            full_msg += msg

            if len(full_msg) - HEADERSIZE ==msglen:
                print("full msg recebido")
                print(full_msg[HEADERSIZE:])
                d=pickle.loads(full_msg[HEADERSIZE:])#Carregamento dos bytes do parâmetro inserido para um objeto
                print(d)

                new_msg = True
                full_msg = b''

        print(full_msg)
