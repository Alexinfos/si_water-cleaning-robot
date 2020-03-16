import socket
import time
import hardware.motor

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
        if len(data) == 0:
            file = open('/web/interface/index.html')
            clientSocket.send(self.generateHTTP200ResponseHMTL(file.read()))
        else:
            prevButtonState = hardware.motor.getStatus()
            if data[0] == "FWD":
                buttonState = hardware.motor.fwd()
            elif data[0] == "BWD":
                buttonState = hardware.motor.bwd()
            elif data[0] == "LEFT":
                buttonState = hardware.motor.left()
            elif data[0] == "RIGHT":
                buttonState = hardware.motor.right()
            elif data[0] == "STOP":
                buttonState = hardware.motor.stop()
            elif data[0] == "STATUS":
                buttonState = hardware.motor.getStatus()
            else:
                buttonState = prevButtonState

            if (buttonState != prevButtonState):
                json = """{
                    "success": true,
                    "error": null,
                    "status": {
                        "fwd": """ + buttonState.fwd + """,
                        "bwd": """ + buttonState.bwd + """,
                        "right": """ + buttonState.right + """,
                        "left": """ + buttonState.left + """,
                        "stop": """ + buttonState.stop + """
                    }
                }"""
            else:
                json = """{
                    "success": false,
                    "error": "Status not changed",
                    "status": {
                        "fwd": """ + buttonState.fwd + """,
                        "bwd": """ + buttonState.bwd + """,
                        "right": """ + buttonState.right + """,
                        "left": """ + buttonState.left + """,
                        "stop": """ + buttonState.stop + """
                    }
                }"""
            clientSocket.send(self.generateHTTP200ResponseJSON(json))
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
        
    def generateHTTP200ResponseHMTL(self, html):
        return 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n' + html + "\n"

    def generateHTTP200ResponseJSON(self, json):
        return 'HTTP/1.1 200 OK\r\nContent-Type: text/json\r\n\r\n' + json + "\n"

