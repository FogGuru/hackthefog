from flask import Flask, request, redirect, url_for, abort,  json
import paho.mqtt.client as mqtt
import datetime
import json

default_port=1883
broker_address = "192.168.9.20"
mqtt_topic = 'people_counter/72'
mqtt_user = 'participant'
mqtt_password = 'participant'


app = Flask(__name__)

subscribed = False

@app.route('/')
def home():
    html = "<html>" \
           "<head><title>Welcome to La Marina de Valencia</title></head>" \
           "<body><h2>Welcome to La Marina de Valencia</h2>" \
           "<body><h3>Current beach-stip population</h3>"

    global subscribed
    if subscribed == False:
        subscribe_on_topic()
    subscribed = True

    list_lines = str(read_message()).split('\n')
    #html = ''
    for line in list_lines:
        if line != '':
            html += "<p> Number People just Entered in last 1 minute: " + str(line) + "</p>"
    #return html.format()
    return html

@app.route('/subscribe')
def subscribe():
    global subscribed
    if subscribed == False:
        subscribe_on_topic()
    subscribed = True
    html = "<b>Subscribed</b>"
    return html.format()

def read_message():
    try:
        f = open("messages.log", "r+")
        message = f.read()
        f.close()
    except Exception as e:
        message = "No messages found"
    return message

def on_connect(client, userdata, flags, rc):  # The callback for when the client connects to the broker
    print("Connected with result code {0}".format(str(rc)))  # Print result of connection attempt
    client.subscribe(mqtt_topic)  # Subscribe to the topic “digitest/test1”, receive any messages published on it


def on_message(client, userdata, message):
    print("time ", datetime.datetime.now())
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    #formated_message = str(datetime.datetime.now()) + "- Received message: "+ str(message.payload.decode("utf-8")) + ", on topic: " + str(message.topic) + "\n"
    formated_message = str(message.payload.decode("utf-8"))
    res = json.loads(formated_message)
    print(res)
    f = open("messages.log", "w")
    f.write(str(res['SensorData']['LeftToRight']))
    f.close()

def subscribe_on_topic(topic = mqtt_topic):
    client = mqtt.Client("subscriber7")
    client.on_message = on_message  # attach function to callback
    client.on_connect = on_connect  # attach function to callback
    print("connecting to broker: " + broker_address)
    client.connect(broker_address, port=default_port) #connect to broker
    client.username_pw_set(username=mqtt_user, password=mqtt_password)
    client.loop_start()  # start the loop
    print("Subscribing to topic: " + mqtt_topic)
    client.subscribe(mqtt_topic)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
