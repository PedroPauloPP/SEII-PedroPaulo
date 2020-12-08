#Video 3 - Servidor
#O código do vídeo 3 visa enviar e receber objetos

import socket
import time
import pickle


HEADERSIZE= 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1236))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Conexão com {address} foi estabelecida!")
    d= {1: "Olá", 2: "Tudo bem?"} #Inserção de dados a serem transmitidos
    msg = pickle.dumps(d) #Função objeto python é convertido para bytes

    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg

    clientsocket.send(msg)
