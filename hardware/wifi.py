import network
import time

TAG = "[hardware.wifi] > "

def checkImport():
    print(TAG + "sucessfully imported !")

# Main functions

# > Wifi Initializer

class WifiClient:

    def __init__(self, ssid, pwd):
        self.client = network.WLAN(network.STA_IF)

        if not self.client.isconnected():
            self.client.active(True)
            self.client.connect(ssid, pwd)
        
        i=0
        while (not self.client.isconnected() and i < 15):
            time.sleep(1)
            i += 1
        
        if (self.client.isconnected()):
            print(TAG + "Successfully connected to WiFi network!")
            ip,_,_,_ = self.client.ifconfig()
            self.ip = ip
            print(TAG + "Server IP: " + ip)
