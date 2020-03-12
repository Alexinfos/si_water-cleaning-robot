# Modules import
print("_________________________\nStarting modules import...")
import hardware.io
hardware.io.checkImport()
import hardware.wifi
hardware.wifi.checkImport()
import web.server
web.server.checkImport()
print("Modules imported!\n_________________________")

# Init
wifiClient = hardware.wifi.WifiClient("TP-LINK_B294", "20420642")
web.server.WebServer(wifiClient, "8081")