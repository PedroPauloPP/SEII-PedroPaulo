#Video 5 - Cliente

import select
import errno #Tratamento de erros possíveis que serão gerados.
import socket
import sys


HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

my_username = input("Username:")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #insere conexão nos dados usados
client_socket.connect((IP, PORT)) #Estabelece conexão nos dados informados
client_socket.setblocking(False) #A fução de recebimento nao vai bloquear os dados

username = my_username.encode("utf-8")
username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")#Nome do usuário em utf nao é maior que o tamanho pré-definido
client_socket.send(username_header + username) #Envia ao servidor o nome + header

while   True:
    message = input(f"{my_username} > ") #Usuário insere o nome
    #message =''
    if message:
        message = message.encode("utf-8")
        message_header = f"{len(message) :<{HEADER_LENGTH} }".encode("utf-8")
        client_socket.send(message_header + message) #Envia mensagem ao servidor caso critério for obedecido
    try:
        while True: #Recebendo os objetos
            username_header = client_socket.recv(HEADER_LENGTH)
            if not len(username_header):
                print("Conexão fechada pelo servidor")
                sys.exit()
            username_length = int(username_header.decode("utf-8").strip())
            username = client_socket.recv(username_length).decode("utf-8")

            message_header = client_socket.recv(HEADER_LENGTH)#Recebe o tamanho do header pré-definido
            message_length = int(message_header.decode("utf-8").strip())#Transforma em inteiro o header da mensagem
            message = client_socket.recv(message_length).decode("utf-8")#Recebe o tamanho em bytes e volta pra objeto

            print(f"{username} > {message}")

    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:  #Critério de erro se for em branco ou não pertencente ao erro estipulado
            print('Reading error',str(e)) #Indica o erro caso não se enquadre
            sys.exit() #Encerra o sistema
        continue

    except Exception as e:
        print('General error', srt(e))#Caso erro desconhecido, a informação é printada
        sys.exit()
        pass
