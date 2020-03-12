import socket
import time

TAG = "[web.server] > "

def checkImport():
    print(TAG + "sucessfully imported !")

# Main functions

# > Wifi Initializer

class WebServer:

    def __init__(self, wifi, port):
        self.wifiClient = wifi
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.wifiClient.ip, port))
        self.socket.listen(2)
        
        time.sleep(2)
        print(TAG + "Listening...")
        
        while True:
          self.handleConnection()
    
    def handleConnection(self):
        clientSocket, _ = self.socket.accept()
        request = self.parseRequest(clientSocket)
        data = self.parseData(request)
        file = open('/web/interface/index.html')
        clientSocket.send(self.generateHTTP200Response(file.read()))
        clientSocket.close()
    
    def parseRequest(self, cSocket):
        request = []
        dataStream = cSocket.makefile('rwb', 0)
        while True:
            line = dataStream.readline()
            if not line or line == b'\r\n':
                break
            request.append(line)
        return request
    
    def parseData(self, request):
        data = []
        if len(request) > 0:
            try:
                dat = str(request[0]).split('?')[1].split(" HTTP")[0].split('&')
                pass
            except IndexError as err:
                print(TAG + "Error while parsing data:")
                print(err)
                if err == 'list index out of range':
                    print("[errANA] This probably means no data was sent by the client")
                    print("dat=" + dat)
                dat = []
                pass
            
            if (len(dat) > 0):
                for d in dat:
                    data[d.split("=")[0]] = d.split("=")[1]
        return data
        
    def generateHTTP200Response(self, html):
        return 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n' + html + "\n"

