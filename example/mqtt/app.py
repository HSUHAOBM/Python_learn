from flask import Flask, render_template, request
from flask_mqtt import Mqtt
import json

app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = 'mqtt.eclipseprojects.io'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_USERNAME'] = ''
app.config['MQTT_PASSWORD'] = ''
app.config['MQTT_KEEPALIVE'] = 5
app.config['MQTT_TLS_ENABLED'] = False

mqtt = Mqtt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/publish', methods=['POST'])
def publish():
    data = json.loads(request.data)
    mqtt.publish(data['topic'], data['message'])
    return 'OK'

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        mqtt.unsubscribe('test/topic')
        mqtt.subscribe('test/topic')
    else:
        print("Failed to connect, return code {0}".format(rc))

@mqtt.on_message()
def handle_message(client, userdata, message):
    if message.topic == "test/topic":
        print(message.topic + ' ' + str(message.payload))
    else:
        print("Received message on topic {0} with payload {1}".format(message.topic, message.payload))

if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)