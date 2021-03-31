import http.client

def HTTPclient(host,port):
    L = int(input()) 
    conn = http.client.HTTPConnection(host,port)

    for i in range(L):
        content = input()
        conn.request("GET", content)

        r1 = conn.getresponse()
        data1 = r1.read().decode()

        print(data1)
        
    conn.close()