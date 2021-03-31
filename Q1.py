import http.client

def HTTPclient(host,port):
    L = int(input()) 
    #serverName = host
    #serverPort = int(port)
    conn = http.client.HTTPConnection(host, port)

    for i in range(L):
        content = input()
        conn.request("GET", content)

        r1 = conn.getresponse()

        if(r1.status == 404): 
            print('Content not found')
        else:
            data1 = r1.getheaders()
            data1 = dict(data1)
            
            tps_msg = {"audio/mpeg" : "Playing audio: ",
                        "text/html" : "Browsing: ",
                        "video/x-msvideo" : "Playing media: ",
                        "application/json" : "Processing JSON: "
                    }

            test=data1.get('Content-type')
            if(tps_msg.get(test) != None):
                print(tps_msg.get(data1.get('Content-type')) + content)    
            else:    
                print("Unknown file/media: " + data1.get('Content-type') + "-" + content)

    conn.close()


