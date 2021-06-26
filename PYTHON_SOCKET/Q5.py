import socket

def UDPserver (host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((host, port))

    while True:
        bitMsg, clientAddress = server.recvfrom(2048)
        strOriginal = bitMsg.decode()

        if strOriginal == 'Hello, world! From ' + str(host) + ':' + str(port):
            print('Servidor recebeu a mensagem correta')
            saida = 'Sucesso' 
            server.sendto(saida.encode(), clientAddress)
        else:
            print('Servidor nao recebeu a mensagem correta')
            erro = 'Erro'
            server.sendto(erro.encode(), clientAddress) 

#host = 'localhost'
#port = 12000
    
#if __name__ == "__main__":   
#    UDPserver(host, port)
