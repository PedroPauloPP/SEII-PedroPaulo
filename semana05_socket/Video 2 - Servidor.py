#Video 2 - Servidor
#O código do vídeo 2 serve para o armazenamento em buffer e streaming de dados

import socket
import time

HEADERSIZE= 10 #Constante indica o tamanho inicial definido

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1235))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Conexão com {address} foi estabelecida!")

    msg = "Bem vindo ao Servidor!"
    msg = f'{len(msg):<{HEADERSIZE}}' + msg #Tamanho da mensagem a ser transmitida

    clientsocket.send(bytes(msg, "utf-8"))

    while   True:
        time.sleep(3) #suspende a execução por 3 segundos
        msg = f"O tempo de execução foi: {time.time()}"
        msg = f'{len(msg):<{HEADERSIZE}}' + msg
        clientsocket.send(bytes(msg, "utf-8"))
