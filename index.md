# 📚 Índice del repositorio Docker

Este repositorio contiene ejemplos y recursos organizados en tres apartados principales:

- **Docker Compose** → ejemplos de despliegue de servicios.
- **Dockerfiles personalizados** → contenedores preparados con configuraciones o datos extra.
- **Recursos adicionales** → utilidades, notas y material de apoyo.

## 🐳 1. Docker Compose

Colección de ficheros `docker-compose.yml` para desplegar servicios básicos y combinados.
 
|   Nombre                                                     | Puertos expuestos        | Función del puerto                        |                                           |
| ------------------------------------------------------------ | ------------------------ | ----------------------------------------- | ----------------------------------------- |
| [**Redis**](./docker_compose/Redis/index.md)                 | 6379                     | Protocolo RESP                            | Base de datos clave-valor                 |
| [**Neo4j**](./docker_compose/Neo4j/index.md)                 | 7074 <br> 7687           | Interfaz Web <br> Protocolo Bolt          | Base de datos orientada a grafos          |
| [**Odoo + PostgreSQL**](./docker_compose/Odoo/index.md)      | 8069                     | Interfaz Web de Odoo                      | Entorno de trabajo Odoo                   |
| [**MQTT Broker**](./docker_compose/mqtt_broker/index.md)     | 1883<br>9001<br>4000     | Protocolo MQTT<br>MQTT sobre WebSockets   | Broker MQTT con generación de datos simulados |
| [**Jupyter Notebook**](./docker_compose/jupyter/index.md)    | 8888                     | Interfaz web de Jupyter                   | Notebook Python con librerías para ciencia de datos |
| [**MongoDB + Express**]() | 27017<br>8081 | Conexiones a Mongo<br>Interfaz web de Mongo Express | Base de datos NoSQL de documentos con visor Web |
| **MinIO** |  |  |  |
| **InfluxDB** |  |  |  |
| **MinIO** |  |  |  |


## ⚙️ 2. Dockerfiles personalizados

Contenedores preparados con configuraciones específicas o datos precargados.

- [Nginx con web estática precargada](./dockerfiles/nginx_estatica/index.md)
- [MySQL con base de datos de empleados](./dockerfiles/mysql_employees/index.md)

## 📦 3. Recursos adicionales

Notas, tutoriales y utilidades relacionadas con Docker.

- [Guía de comandos básicos de Docker](./recursos/comandos-basicos.md)
- [Redes en Docker](./recursos/redes.md)
- [Gestión de volúmenes](./recursos/volumenes.md)
- [Buenas prácticas con Dockerfiles](./recursos/buenas-practicas-dockerfiles.md)
