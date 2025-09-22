# 📦 Entorno de Simulación IoT

## 📋 Resumen

Este fichero `docker-compose.yml` despliega un entorno de simulación IoT completo, con un broker de mensajería **MQTT** que actúa como punto central para la comunicación. El entorno incluye contenedores para un broker, un visualizador de mensajes y dos servicios de Python que simulan un sensor y un consumidor de datos. Este setup es ideal para ejercicios de ingesta de datos y desarrollo de aplicaciones IoT.

| Servicio | Imagen | Versión | Puertos | Volúmenes | Red |
|---|---|---|---|---|---|
| `mqtt-broker` | `eclipse-mosquitto` | `2` | `1883:1883`<br>`9001:9001` | `./mosquitto.conf:/mosquitto/config/mosquitto.conf`<br>`./mosquitto_data:/mosquitto/data`<br>`./mosquitto_log:/mosquitto/log` | `shared-network` |
| `mqtt-explorer` | `smeagolworms4/mqtt-explorer` | - | `4000:4000` | - | `shared-network` |
| `sensor-simulator` | `python` | `3.9-slim` | - | `./sensor_simulator.py:/app/sensor_simulator.py`<br>`./requirements.txt:/app/requirements.txt` | `shared-network` |
| `data-consumer` | `python` | `3.9-slim` | - | `./data_consumer.py:/app/data_consumer.py`<br>`./requirements.txt:/app/requirements.txt` | `shared-network` |


## 🛠️ Servicios definidos

  - **`mqtt-broker`** → Servidor de mensajería MQTT que gestiona el intercambio de mensajes entre los sensores y los consumidores.
  - **`mqtt-explorer`** → Herramienta visual para monitorear en tiempo real los mensajes que pasan por el broker.
  - **`sensor-simulator`** → Un script de Python que simula la función de un sensor IoT, publicando datos en un tópico del broker.
  - **`data-consumer`** → Un script de Python que se suscribe a los tópicos y consume los datos enviados por el sensor.


## 🌐 Puertos expuestos

  * **`1883`** → Puerto estándar para la comunicación MQTT.
  * **`9001`** → Puerto para la comunicación MQTT sobre WebSockets, para clientes basados en navegador.
  * **`4000`** → Puerto para la interfaz web de la herramienta de monitoreo `mqtt-explorer`.


## 🔑 Credenciales por defecto

- No son necesarias credenciales


## 💾 Volúmenes y persistencia

| Ruta Host (local)      | Ruta Contenedor                    | Servicio          | Propósito |
|------------------------|------------------------------------|-------------------|-----------|
| `./mosquitto.conf`     | `/mosquitto/config/mosquitto.conf` | `mqtt-broker`     | Permite configurar el broker Mosquitto desde el equipo anfitrión. |
| `./mosquitto_data`     | `/mosquitto/data`                  | `mqtt-broker`     | Almacena los datos de persistencia del broker, como los mensajes retenidos o las configuraciones de seguridad. |
| `./mosquitto_log`      | `/mosquitto/log`                   | `mqtt-broker`     | Guarda los archivos de registro del broker para la auditoría y depuración. |
| `./sensor_simulator.py`| `/app/sensor_simulator.py`         | `sensor-simulator`| Mapea el script del simulador para que el contenedor lo ejecute. |
| `./data_consumer.py`   | `/app/data_consumer.py`            | `data-consumer`   | Mapea el script del consumidor de datos para su ejecución. |
| `./requirements.txt`   | `/app/requirements.txt`            | `sensor-simulator`<br>`data-consumer` | Contiene las dependencias de Python (ej. `paho-mqtt`) para que los servicios las instalen automáticamente. |



## 📝 Notas adicionales

- El contenedor `mqtt-broker` ejecuta el script Python `sensor-simulator.py` que simula diversos sensores IoT. Sería conveniente mejorar este script para incluir más tipos de sensores.
- El contenedor `data-consumer` simplemente ejecuta el script `data-consumer.py` a modo de ejemplo como consumidor de los datos generados por los sensores.
