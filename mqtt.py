import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    #client.subscribe("room1/#")
    client.subscribe("rooms/")
    client.subscribe("rooms/ack/")
    
    
    ##! subscribe setiap room_id
    ##! ada
    
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
#? setting username password for connection
#? room1
#client.username_pw_set(username="938d6a63", password="16f7507c506a707f")
#? token tessatpam
#client.username_pw_set(username="0c70c0c8", password="50cb975fb6f325e4")
#call on_connect function
#? token ruang1
#client.username_pw_set(username="9f820c79", password="a8157327549fff7e")
#? token ruang2
#client.username_pw_set(username="17ef7535", password="1301fb934951c507")
#? token ruang3
client.username_pw_set(username="9f820c79", password="a8157327549fff7e")
#? Dst....

client.on_connect = on_connect
#call on_message function
client.on_message = on_message

client.connect("broker.shiftr.io", 1883, 60)
#client.publish("tessatpam","server connected ")
##untuk online ip ganti broker.shifter.io
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
#client.loop_forever()

