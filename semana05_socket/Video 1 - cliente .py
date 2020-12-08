#Video 1 - cliente 

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))

full_msg = ''
while True:
    msg = s.recv(1024) #Funcao que determinará o número máximo de bytes a ser lido
    if msg len(msg) <= 0: #Se parâmetro anterior for 0, o sistema é interrompido
        break
    full_msg += (msg.decode("utf-8"))

print(full_msg)
