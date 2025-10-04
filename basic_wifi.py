import network,time
network.country("IN")

ssid = "ssid"
password = "password"

station = network.WLAN(network.STA_IF)
station.active(True)

station.connect(ssid, password)
while station.isconnected() == False:
    time.sleep(1)
    print("Connecting....")
    
print("Connected successfully")

print(station.ifconfig())
print(station.config('mac'))
print(station.config('ssid'))
print(station.config('channel'))



