import paho.mqtt.client as mqtt
import random
import json
import time
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()


BROKER=os.getenv("MQTT_BROKER")
PORT=os.getenv("MQTT_PORT")
TOPIC="home/room1/temp"
interval=10

client=mqtt.Client()
try:
    client.connect(BROKER,PORT,60)
except:
    print("Connection failed")


print("Publishing temperature data... Press Ctrl+C to stop")

client.loop_start()
try:
    while True:
        temp=round(random.uniform(20,30),2)
        payload={
            "temp":temp,
            "timestamp":str(datetime.now())
        }
        client.publish(
            topic=TOPIC,
            payload=json.dumps(payload),
            qos=1
        )
        print("Published: ",payload)
        time.sleep(interval)
except  KeyboardInterrupt:
    print("\nInterrupted by user. Stopping publisher...")
    
finally:
    client.loop_stop()
    client.disconnect()