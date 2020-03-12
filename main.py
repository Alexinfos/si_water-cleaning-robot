print("Copyright (C) Alexis Brandner 2020\nThis program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the  License, or (at your option) any later version.\nThis program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.\nYou should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.")

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