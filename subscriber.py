import os
from dotenv import load_dotenv
import paho.mqtt.client as mqtt
import json
import redis
from datetime import datetime

load_dotenv()

BROKER=os.getenv("MQTT_BROKER")
PORT=os.getenv("MQTT_PORT")
HOST=os.getenv("REDIS_HOST")
R_PORT=os.getenv("REDIS_PORT")

try:
    
    r=redis.Redis(
        host=HOST,
        port=R_PORT,
        decode_responses=True
    )
except Exception as e:
    print("Connection failed: ",e)
try:
    r.execute_command(
    "TS.CREATE",
    "temp:sensor1",
    "RETENTION", 3600000,   # keep data for 1 hour (ms)
    "LABELS",
    "sensor", "sensor1",
    "type", "temperature"
    )
except redis.ResponseError:
    pass




def on_connect(client,userdata,flags,rc):
    print("Connected with result code",rc)
    client.subscribe("home/+/temp")
    
def on_message(client,userdata,msg):
    payload=json.loads(msg.payload)
    iso_time = payload["timestamp"]

    dt = datetime.fromisoformat(iso_time)
    timestamp_ms = int(dt.timestamp() * 1000)
    try:
        r.execute_command(
        "TS.ADD",
        "temp:sensor1",
        timestamp_ms,
        payload["temp"]
        )
        print("Temp: ",payload["temp"])
        print("Time: ",payload["timestamp"])
    except Exception as e:
        print("Error",e)
        

client = mqtt.Client()
client.on_connect =  on_connect
client.on_message = on_message

client.connect(BROKER,int(PORT),60)
client.loop_forever()