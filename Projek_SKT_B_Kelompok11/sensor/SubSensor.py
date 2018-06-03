import paho.mqtt.client as mqtt

mqtt_client = mqtt.Client()

mqtt_client.connect("iot.eclipse.org", 1883)

def handle_message(mqttc, obj, msg):
    #print("Datanya adalah "+str(msg.payload,'utf-8')+" topik "+msg.topic)
    if(msg.topic == "/sensor/asap"):
        if(int(msg.payload) == 1):
            statusAsap = 'Ada Asap'
        else:
            statusAsap = 'Tidak ada asap'
        print(statusAsap)
    elif(msg.topic == "/sensor/udara"):
        if(int(msg.payload) >= 0 and int(msg.payload) <= 50):
            statusUdara = 'Baik'
        elif(int(msg.payload) >= 51 and int(msg.payload) <=100):
            statusUdara = 'Sedang'
        elif(int(msg.payload) >= 101 and int(msg.payload) <=199):
            statusUdara = 'Tidak sehat'
        elif(int(msg.payload) >= 200 and int(msg.payload) <=299):
            statusUdara = 'Sangat tidak sehat'
        elif(int(msg.payload) >= 300 and int(msg.payload) <=500):
            statusUdara = 'Berbahaya'
        print(statusUdara)
mqtt_client.on_message = handle_message

mqtt_client.subscribe("/sensor/asap")
mqtt_client.subscribe("/sensor/udara")

mqtt_client.loop_forever()

