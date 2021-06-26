import socket
import string

def UDPserver(host, port):
    global udpd

    udpd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpd.bind((host, port))

    while True:
        bitMsg, clientAddress = udpd.recvfrom(2048)
        strMsg = bitMsg.decode()
        asciiMsg = ascii(strMsg)

        ponto = -2
        esp = 0
        maius = 0
        minus = 0
        decimal = 0

        for dado in asciiMsg:
            if dado in string.punctuation:
                ponto += 1
            elif dado in string.whitespace:
                esp += 1
            elif dado in string.ascii_uppercase:
                maius += 1
            elif dado in string.ascii_lowercase:
                minus += 1
            elif dado in string.digits:
                decimal += 1
      
        if maius == 0 or minus == 0 or decimal == 0:
            erro = 'Senha inválida!'
            udpd.sendto(erro.encode(), clientAddress)
        elif ponto > 0 or esp > 0:
            erro = 'Senha inválida!'
            udpd.sendto(erro.encode(), clientAddress)
        elif len(strMsg) > 32 or len(strMsg) < 6:
            erro = 'Senha inválida!'
            udpd.sendto(erro.encode(), clientAddress)
        else:
            saida = 'Senha valida.'
            udpd.sendto(saida.encode(), clientAddress)



#host = 'localhost'
#port = 12000
   
#if __name__ == "__main__":    
#    UDPserver(host, port)
