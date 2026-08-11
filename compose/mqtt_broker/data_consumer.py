import paho.mqtt.client as mqtt
import json
import os
from datetime import datetime

# Configuración desde variables de entorno
BROKER_HOST = os.getenv("BROKER_HOST", "localhost")
BROKER_PORT = int(os.getenv("BROKER_PORT", "1883"))

def on_connect(client, userdata, flags, rc):
    print(f"Conectado al broker con código: {rc}")
    client.subscribe("iot/sensores/#")  # Suscribirse a todos los topics

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
        print(f"\n📨 [{datetime.now().strftime('%H:%M:%S')}] {msg.topic}")
        print(f"   Sensor: {data.get('sensor_id')}")
        print(f"   Valor: {data.get('value')} {data.get('unit')}")
        print(f"   Ubicación: {data.get('location')}")
    except Exception as e:
        print(f"Error procesando mensaje: {e}")


if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    
    print("Conectando al consumidor MQTT...")
    client.connect(BROKER_HOST, BROKER_PORT, 60)
    client.loop_forever()