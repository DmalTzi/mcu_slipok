import network
import urequests
import json
import time
from machine import Pin

SSID = "True2-WiFi"
PASSWORD = "truetrue"
api_url = "http://167.71.207.82:9090/api/check/relay"

relay1 = Pin(2, Pin.OUT)
relay2 = Pin(0, Pin.OUT)


# เริ่มต้นตั้งค่า WiFi
def connect_wifi():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect(SSID, PASSWORD)

    print("connecting to wifi...")
    while not wifi.isconnected():
        pass
    print("wifi is connected", wifi.ifconfig())

def using_api():
    response = urequests.get(api_url)
    if response.status_code == 200:
        return response.json()

def start():
    connect_wifi()
    while True:
        response = using_api()
        print(response)
        if response["slot1"] > 0:
            print("slot1 : on")
            relay1.value(0)
        else:
            print("slot1 : off")
            relay1.value(1)
            
        if response["slot2"] > 0:
            print("slot2 : on")
            relay2.value(0)
        else:
            print("slot2 : off")
            relay2.value(1)
        
        time.sleep(10)
        
    
start()


