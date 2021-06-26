import socket
def UDPclient(host,port):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    StrFin = 'Hello, world! From ' + str(host) + ':' + str(port)
    client.sendto(StrFin.encode(), (host, port))

    resp, serverAddress = client.recvfrom(2048)

    print('Saida: ', resp.decode())

    client.close()

#host = 'localhost'
#port = 12000
    
#if __name__ == "__main__":   
#    UDPclient(host, port)
