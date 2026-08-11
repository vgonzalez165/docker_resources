import paho.mqtt.client as mqtt
import json
import random
import time
import os
from datetime import datetime

# Configuración desde variables de entorno
BROKER_HOST = os.getenv("BROKER_HOST", "localhost")
BROKER_PORT = int(os.getenv("BROKER_PORT", "1883"))
TOPIC_PREFIX = os.getenv("TOPIC_PREFIX", "iot/sensores")

# Tipos de sensor a simular
SENSOR_TYPES = [
    "temperature", 
    "humidity", 
    "pressure", 
    "vibration"
]

def generate_sensor_data(sensor_type, sensor_id):
    """Genera datos realistas según el tipo de sensor"""
    base_values = {
        "temperature": (20, 30),  # °C
        "humidity": (40, 80),     # %
        "pressure": (980, 1020),  # hPa
        "vibration": (0, 10)      # mm/s
    }
    
    min_val, max_val = base_values[sensor_type]
    value = random.uniform(min_val, max_val)
    
    # Pequeñas variaciones para hacerlo más realista
    if sensor_type == "temperature":
        value += random.uniform(-0.5, 0.5)
    
    return {
        "sensor_id": sensor_id,
        "type": sensor_type,
        "value": round(value, 2),
        "timestamp": datetime.utcnow().isoformat(),
        "unit": get_unit(sensor_type),
        "location": random.choice(["nave_A", "nave_B", "exterior"])
    }

def get_unit(sensor_type):
    units = {
        "temperature": "°C",
        "humidity": "%",
        "pressure": "hPa",
        "vibration": "mm/s"
    }
    return units.get(sensor_type, "units")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Conectado exitosamente al broker MQTT en {BROKER_HOST}:{BROKER_PORT}")
    else:
        print(f"Error de conexión. Código: {rc}")

# Configurar cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect

try:
    print(f"Conectando a MQTT broker en {BROKER_HOST}:{BROKER_PORT}...")
    client.connect(BROKER_HOST, BROKER_PORT, 60)
    client.loop_start()  # Usar loop_start en lugar de loop_forever para no bloquear
    
    # Esperar a que se establezca la conexión
    time.sleep(2)
    
    # Publicar datos de forma continua
    sensor_count = 0
    while True:
        for sensor_type in SENSOR_TYPES:
            # Simular múltiples sensores del mismo tipo
            for i in range(3):
                sensor_id = f"{sensor_type}_sensor_{i+1}"
                data = generate_sensor_data(sensor_type, sensor_id)
                topic = f"{TOPIC_PREFIX}/{sensor_type}/{sensor_id}/data"
                
                client.publish(topic, json.dumps(data))
                print(f"Publicado: {topic} - {data['value']}{data['unit']}")
                
                sensor_count += 1
                time.sleep(0.5)  # Pequeña pausa entre sensores
            
        print(f"--- Ronda completada. Total de mensajes: {sensor_count} ---")
        time.sleep(10)  # Pausa entre rondas de sensores
        
except KeyboardInterrupt:
    print("Deteniendo simulador...")
    client.loop_stop()
    client.disconnect()
except Exception as e:
    print(f"Error: {e}")
    client.loop_stop()
    client.disconnect()