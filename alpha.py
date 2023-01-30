import paho.mqtt.client as mqtt

# Define the MQTT callback functions
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
    print("Topic: "+msg.topic+" Message: "+str(msg.payload))

# Connect to the MQTT broker
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60)

# Subscribe to a topic to receive alerts
client.subscribe("/food-shelf-life/alerts")

# Publish an alert message when the food is about to go bad
if food_is_about_to_go_bad:
    client.publish("/food-shelf-life/alerts", "Freshness Alert: Food is about to go bad!")

# Keep the connection to the MQTT broker alive
client.loop_forever()