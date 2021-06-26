import socket
def TCPserver (host, port):

    global tcpd
    tcpd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpd.bind(('', port))
    tcpd.listen(1)
    connectionSocket, addr = tcpd.accept()

    try:
        while True:
            cadeia = connectionSocket.recv(2048).decode()
            cadeiaAlt = ''
            cnt = 1
            for i, ch in enumerate(cadeia):
                if i == 0:
                    cadeiaAlt += ch
                elif cadeia[i] == cadeia[i-1]:
                    cnt += 1
                elif cadeia[i] != cadeia[i-1]:
                    cadeiaAlt += str(cnt)+ch
                    cnt = 1

            cadeiaAlt += str(cnt)
            connectionSocket.send(cadeiaAlt.encode())
    except:
        connectionSocket.close()

host = 'localhost'
port = 12000
    
if __name__ == "__main__":
    TCPserver(host, port)
