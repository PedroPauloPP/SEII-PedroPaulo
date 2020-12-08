#Video 2 - Cliente

import socket

HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))

while  True:
    full_msg = ''
    new_msg = True
    while True:
            msg = s.recv(16) #Tamanho máximo de bytes a ser recebido
            if new_msg:
                print(f"comprimento de new_msg: {msg[:HEADERSIZE]}")
                msglen = int(msg[:HEADERSIZE]) #Transforma para inteiro o valor de msg[:HEADERSIZE]
                new_msg = False

            full_msg += (msg.decode("utf-8"))
            if len(full_msg) - HEADERSIZE ==msglen:
                print("full msg recebido")
                print(full_msg[HEADERSIZE:])
                new_msg = True
                full_msg = ''

        print(full_msg)
