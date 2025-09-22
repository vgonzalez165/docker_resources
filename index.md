# 📚 Índice del repositorio Docker

Este repositorio contiene ejemplos y recursos organizados en tres apartados principales:

- **Docker Compose** → ejemplos de despliegue de servicios.
- **Dockerfiles personalizados** → contenedores preparados con configuraciones o datos extra.
- **Recursos adicionales** → utilidades, notas y material de apoyo.

## 🐳 1. Docker Compose

Colección de ficheros `docker-compose.yml` para desplegar tanto servicios básicos como varios servicios combinados en un único fichero compose.

Todos los servicios están conectados a una red externa denominada `shared_network`, por lo que antes de lanzar cualquiera de estos servicios será necesario tener creada esta red. En caso de no tenerla se debe crear esta red con la siguiente orden:

```
docker network create shared_network
```

Al compartir todos los servicios la misma red externa se pueden comunicar directamente cualesquiera dos servicios que se levanten utilizando la resolución local de nombres de Docker. Asimismo, cada servicio expone varios puertos en la máquina física.



 
|   Nombre                                                              |                                                     | Puertos expuestos        | Función del puerto                        |
| --------------------------------------------------------------------- | --------------------------------------------------- | ------------------------ | ----------------------------------------- |
| [**Redis**](./docker_compose/Redis/index.md)                          | Base de datos clave-valor                           | 6379                     | Protocolo RESP                            |
| [**Neo4j**](./docker_compose/Neo4j/index.md)                          | Base de datos orientada a grafos                    | 7074 <br> 7687           | Interfaz Web <br> Protocolo Bolt          |
| [**Odoo + PostgreSQL**](./docker_compose/Odoo/index.md)               | Entorno de trabajo Odoo                             | 8069                     | Interfaz Web de Odoo                      |
| [**MQTT Broker**](./docker_compose/mqtt_broker/index.md)              | Broker MQTT con generación de datos simulados       | 1883<br>9001<br>4000     | Protocolo MQTT<br>MQTT sobre WebSockets   |
| [**Jupyter Notebook**](./docker_compose/jupyter_notebook/index.md)    | Notebook Python con librerías para ciencia de datos | 8888                     | Interfaz web de Jupyter                   |
| [**MongoDB + Express**]()                                             | Base de datos NoSQL de documentos con visor Web     | 27017<br>8081            | Conexiones a Mongo<br>Interfaz web de Mongo Express  |
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
