#%% Ejercicio: Aplicación que obtiene datos de sitios web en internet a través
#              de peticiones de tipo GET.

import socket
import requests

class GetPetition:
    
    def __init__(self, host):
         self.host = host
    
    def dataGet(self, host):
        
        self.host = host
        url = "http://" + self.host
        ip = socket.gethostbyname(host)
        response = requests.get(url)
        
        if "server" in response.headers: 
            server = response.headers["server"]
        else:
            server = "unknown"
        
        if "Content-Encoding" in response.headers:
            contentEncoding = response.headers["content-encoding"]
        else:
            contentEncoding = "unknown"
        
        if "Content-Type" in response.headers:
            contentType = response.headers["content-type"] 
        else:
            contentType = "unknown"
        
        out = {"Host": host,
               "IP": ip,
               "Server": server,
               "Content-Encoding": contentEncoding,
               "Content-Type" : contentType
               }
        
        return out
    
    def dataSave(self, data, path):
        
        file = open(path, "a")
        
        file.write("Host: %s\n" % (data["Host"]) )
        file.write("IP: %s\n" % (data["IP"]))
        file.write("Server: %s\n" % (data["Server"]))
        file.write("Content-Encoding: %s\n" % (data["Content-Encoding"]))
        file.write("Content-Type: %s\n\n" % (data["Content-Type"]))
        
        file.close()


urls = ['www.youtube.com','www.gmail.com','www.facebook.co']

for webPage in urls:
    p = GetPetition(webPage)
    data = p.dataGet(webPage)
    p.dataSave(data, "data.txt")
    print(data)
