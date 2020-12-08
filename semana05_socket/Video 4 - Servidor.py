#Video 4 - Servidor
#O video 4 tem como objetivo criar uma aplicação Chat utilizando sockets
#   Com a função de implementar um chat, adiciona-se um endereço, IP e a porta da conexão.
#   Adiciona-se a lib socket para manipulação dos dados via bytes, conforme as linhas 12 e 13, no qual permite o uso do
#endereço e estabelece o tipo de conexao feita. Define-se um parâmetro; linha 18; para que seja alocado todo os dados, e
#também os clientes para que seja adicionado o usuário utilizando o chat.
#    Define-se o parâmetro receive_message através do client_socket, sendo que ele tentará ler o header passado, e caso 
#o comprimento nao seja igual ao message_header, ele retornará o header e o comprimento da mensagem até então, caso contrário,
#retornará falso em completo.
#    Caso a afirmação seja verdadeira, ele irá ler e entender o endereço e o usuário, indicando se o valor do usuário é 
#falso ou verdadeiro, indicado na linha 41. Caso falso, ele continua, caso contrário, é adicionado ao sockets.list o 
#client_socket, indicando assim que a conexão foi aceita e mostrando o usuário e o endereço da conexão estabelecida.
#    Considerando a linha 65, dentro de exception_sockets, sera removido atraves do .remove o notified_socket de sockets.list e
#também do parÂmetro clients.
#    Caso a mensagem recebida na linha 49 seja indicada como falso, ele removera o notified_socket do socket_list e deletará
#o notified_socket do parametro clients.


import socket
import select


HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

server_socket.bind((IP, PORT))

server_socket.listen()
sockets_list =[server_socket]

clients={}
def receive_message (client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)

        if not len(message_header):
            return False
        message_length = int(message_header.decode("utf-8").strip())
        return {"header:": message_header, "data":client_socket.recv(message_length)}

    except:
        return False

while   True:
    read_sockets, _, exception_sockets = select.select(sockets_list,[], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()

            user = receive_message(client_socket)
            if user is False:
                continue

                sockets_list.append(client_socket)
                clients[client_socket] = user
                print(f"Nova conexao aceita de {client_address[0]}:{client_address[1]} usuario:{user['data'].decode('utf-8')}")

            else:
                message = receive_message(notified_socket)

                if message is False:
                    print(f"Conexao encerrada de {clients[notified_socket]['data'].decode('utf-8')}")
                    sockets_list.remove(notified_socket)
                    del clients[notified_socket]
                    continue

                user = clients[notified_socket]
                print(f"Mensagem recebida de {user['data'].decode('utf-8')}: {message['data'].decode('utf-8')}")

                for client_socket in clients:
                    if client_socket != notified_socket:
                        client_socket.send(user['header'] + user['data'] + message['header']+ message['data'])


    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]
