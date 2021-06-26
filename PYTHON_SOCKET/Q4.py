import socket

def TCPserver(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', port))
    server.listen(1)

    connection, addr = server.accept()
    bitsMsg = connection.recv(2048)
    strOriginal = bitsMsg.decode()

    if strOriginal == 'Hello, world! From ' + str(host) + ':' + str(port):
        print('Servidor recebeu a mensagem correta')
        saida = 'Sucesso'
        connection.send(saida.encode())
    else:
        print('Servidor nao recebeu a mensagem correta')
        erro = 'Erro'
        connection.send(erro.encode())

    connection.close()


#host = 'localhost'
#port = 12000

#if __name__ == "__main__":
#    TCPserver(host, port)
