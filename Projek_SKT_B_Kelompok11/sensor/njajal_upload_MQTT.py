import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev
import paho.mqtt.client as mqtt #mqtt library for python
import random

mqttc = mqtt.Client() # Define Connection
mqttc.connect("iot.eclipse.org", 1883, 60) # Do Connection


GPIO.setmode(GPIO.BCM)

pipesr = [[0xF0, 0xF0, 0xF0, 0xF0, 0xC5], [0xF0, 0xF0, 0xF0, 0xF0, 0xC4]]
pipesw = [[0xF0, 0xF0, 0xF0, 0xF0, 0xA4], [0xF0, 0xF0, 0xF0, 0xF0, 0xA3]]

radio = NRF24(GPIO, spidev.SpiDev())
radio.begin(0, 17)

radio.setPayloadSize(32)
radio.setChannel (0x76)
radio.setDataRate(NRF24.BR_1MBPS)
radio.setPALevel (NRF24.PA_MIN)

radio.setAutoAck(True)
radio.enableDynamicPayloads()
radio.enableAckPayload()

radio.openReadingPipe(1, pipesr[0])
radio.openReadingPipe(2, pipesr[1])
radio.startListening()

while (1):
        ackPL = [1]
        while not radio.available(0):
            time.sleep(1/100)

        receivedMessage = []
        radio.read(receivedMessage, radio.getDynamicPayloadSize())
        #print("Received : {}".format(receivedMessage))
        string = ""
        for n in receivedMessage:
            if (n >= 32 and n <= 126):
                string += chr(n)
        if (string == "1") :
                print(string)
                data = random.randrange(0, 12, 1)
                print(data)
                mqttc.publish("/sensor/asap", payload=string, qos=0, retain=True)
        if (string == "0") :
                print(string)
                data = random.randrange(0, 12, 1)
                print(data)
                mqttc.publish("/sensor/asap", payload=string, qos=0, retain=True)
