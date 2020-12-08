#Video 1 - Servidor
#O vídeo 1 tem por objetivo enviar e receber dados através de um servidor e um usuário

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Funções representam o endereço e protocolos a serem requisitados, sendo o argumento para o socket()
s.bind((socket.gethostname(), 1234)) #Ligação do socket no endereço
s.listen(5) #Listen especifica o número de conexões nao aceitas que o sistema vai permitir antes de recusar novas conexões

while True:
    clientsocket, address = s.accept() #Ao se ter a conexão, é retornado o novo "socket object" que representa a conexão e o endereço do usuário
    print(f"Conexão com {address} foi estabelecida!")
    clientsocket.send(bytes("Bem vindo ao Servidor!", "utf-8")) #Projeta uma mensagem definindo que a conexão foi aceita
    clientsocket.close() #Encerra quando a conexao é bem sucedida
