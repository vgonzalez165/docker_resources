# Índice del repositorio Docker

Este repositorio contiene ejemplos y recursos para Docker organizados en tres apartados principales:

- **Docker Compose** → ejemplos de despliegue de servicios.
- **Dockerfiles personalizados** → contenedores preparados simulando servidores reales, por ejemplo, bases de datos con datos precargados.
- **Recursos adicionales** → utilidades, notas y material de apoyo.

## 1. Docker Compose

Colección de ficheros `docker-compose.yml` para desplegar tanto servicios básicos como varios servicios combinados en un único fichero compose.

### Instrucciones

Todos los servicios están conectados a una red externa denominada `shared_network`, por lo que antes de lanzar cualquiera de estos servicios será necesario tener creada esta red. En caso de no tenerla se debe crear esta red con la orden `docker network create shared_network`

Al compartir todos los servicios la misma red externa se pueden comunicar directamente cualesquiera dos servicios que se levanten utilizando la resolución local de nombres de Docker. Asimismo, cada servicio expone varios puertos en la máquina física.

Para levantar el entorno configurado en un fichero `compose` únicamente hay que ubicarse en el directorio que contiene dicho fichero y ejecutar la orden `docker compose up -d`.

### Relación de ficheros `compose`
 
|   Nombre                                              |                                                              | Puertos expuestos        | Función del puerto                        |
| ----------------------------------------------------- | ------------------------------------------------------------ | ------------------------ | ----------------------------------------- |
| [**Registry + UI**](./compose/registry/index.md)                                   | Registro privado de contenedores                             | 5000 <br> 8085           | Docker Registry <br> Interfaz Web         |
| [**Redis**](./compose/redis/index.md)                 | Base de datos clave-valor                                    | 6379                     | Protocolo RESP                            |
| [**Neo4j**](./compose/neo4j/index.md)                 | Base de datos orientada a grafos                             | 7074 <br> 7687           | Interfaz Web <br> Protocolo Bolt          |
| [**Odoo + PostgreSQL**](./compose/odoo/index.md)      | Entorno de trabajo Odoo                                      | 8069                     | Interfaz Web de Odoo                      |
| [**MQTT Broker**](./compose/mqtt_broker/index.md)     | Broker MQTT con generación de datos simulados                | 1883<br>9001<br>4000     | Protocolo MQTT<br>MQTT sobre WebSockets<br>Interfaz web herramienta monitoreo   |
| [**Jupyter Notebook**](./compose/jupyter_notebook/index.md)| Notebook Python con librerías para ciencia de datos     | 8888                     | Interfaz web de Jupyter                   |
| [**MongoDB + Express**](./compose/mongodb/)           | Base de datos NoSQL de documentos con visor Web              | 27017<br>8081            | Conexiones a Mongo<br>Interfaz web de Express  |
| [**LAMP**](./compose/lamp/)                           | Stack Web: Apache + MySQL + PHP                              | 80<br>8080               | Web desplegada en Apache<br>MPHPMyAdmin   |
| [**Clúster Hadoop**](./compose/hadoop_cluster/)       | Clúster Hadoop (con Jupyter)                                 | 9870<br>8088<br>19888<br>7777<br>10000<br>1002| Interfaz Web de HDFS<br>Interfaz Web de Resource Manager<br>Interfaz Web de JobHistory Server<br>Interfaz Web de Jupyter<br>Conexión para cliente Hive<br>Conexión para cliente HiveServer2 |
| [**Spark**](./compose/spark/)            | Spark con cliente Jupyter                | 8080<br>8081<br>7077<br>4040<br>8899 | Interfaz Web Spark Master<br>Interfaz Web Spark Worker<br>Puerto comunicación Master<br>Spark Context UI<br>Jupyter Lab |
| [**MySQL + PHPMyAdmin**](./compose/mysql/)            | Gestor de bases de datos MySQL con PHPMyAdmin                | 3306<br>8000 | Puerto estándar MySQL<br>Interfaz PHPMyAdmin |
| **MinIO**                                             |                                                              |                          |                                           |
|[**InfluxDB**](./compose/influxdb/index.md)                                          |                                                              |                          |                                           |


## 2. Dockerfiles personalizados

Pasos a realizar para crear imágenes de Docker con datos precargados, por ejemplo, servidores web que tengan una determinada página Web o sistemas gestores de bases de datos que contengan ya datos previamente cargados.

### Instrucciones generales


### Relación de contenedores

- [Nginx con web estática precargada](./dockerfiles/nginx_estatica/index.md)
- [MySQL con base de datos de empleados](./dockerfiles/mysql_employees/index.md)

## 3. Recursos adicionales

Notas, tutoriales y utilidades relacionadas con Docker.

- [Guía de comandos básicos de Docker](./recursos/comandos-basicos.md)
- [Redes en Docker](./recursos/redes.md)
- [Gestión de volúmenes](./recursos/volumenes.md)
- [Buenas prácticas con Dockerfiles](./recursos/buenas-practicas-dockerfiles.md)













Perfecto 👌 Aquí tienes un resumen **claro y didáctico** de las **principales características** de los tipos de contenedores más utilizados hoy en día —ideal para tus clases de sistemas operativos o DevOps—:

---

## 🐳 **1. Docker**

### 🔹 Descripción

Es el sistema de contenedores más popular. Permite **empaquetar aplicaciones y sus dependencias** en imágenes portables que se ejecutan de forma aislada del sistema anfitrión.

### 🔹 Características principales

* **Arquitectura cliente-servidor** (usa el daemon `dockerd`).
* Usa **imágenes OCI** (Open Container Initiative).
* **Portabilidad total:** se ejecuta igual en Windows, Linux o macOS.
* **Gran ecosistema:** Docker Hub, Compose, Swarm.
* **Foco en las aplicaciones**, no en sistemas completos.
* **Aislamiento a nivel de proceso** (usa namespaces y cgroups).
* **Velocidad de despliegue:** arranca contenedores en segundos.
* Compatible con **Kubernetes** (como runtime o a través de `containerd`).

---

## 🧩 **2. Podman**

### 🔹 Descripción

Alternativa a Docker desarrollada por Red Hat. Ofrece las mismas funciones que Docker, pero **sin daemon** y **sin necesidad de permisos de root**.

### 🔹 Características principales

* **No usa daemon:** cada contenedor es un proceso del usuario.
* **Totalmente rootless:** puede ejecutarse sin privilegios de administrador.
* **Compatibilidad con Docker:** usa las mismas imágenes y comandos.
* **Soporta pods:** permite agrupar contenedores como en Kubernetes.
* **Integración con systemd:** puede generar unidades systemd automáticamente.
* Mayor **seguridad** y **control granular de procesos**.
* Ideal para entornos donde se prioriza la **seguridad** (por ejemplo, servidores multiusuario).

---

## 🏗️ **3. LXC / LXD**

### 🔹 Descripción

LXC (Linux Containers) fue el primer sistema de contenedores de Linux. LXD es su capa superior, que ofrece una **interfaz más moderna y gestionada**, pensada para **simular máquinas virtuales completas**.

### 🔹 Características principales

* **Basado en el sistema operativo:** virtualización ligera (usa el kernel del host).
* **Entornos casi completos:** puedes ejecutar `systemd`, `sshd`, etc.
* **Aislamiento fuerte:** namespaces, cgroups y AppArmor/SELinux.
* **Gestión avanzada con LXD:** creación, snapshots, redes, almacenamiento.
* Permite **imágenes de sistemas completos** (Ubuntu, Debian, CentOS...).
* Ideal para **entornos de pruebas** o **laboratorios de servidores Linux**.
* **Rendimiento muy alto** (sin hipervisor).

---

## ☸️ **4. Kubernetes Pods**

### 🔹 Descripción

No es un sistema de contenedores en sí, sino una **unidad lógica de agrupación y orquestación** dentro de Kubernetes. Un *Pod* puede contener **uno o varios contenedores** que comparten red y almacenamiento.

### 🔹 Características principales

* **Unidad básica de ejecución en Kubernetes**.
* **Agrupa varios contenedores** que funcionan como un mismo servicio.
* Los contenedores del Pod **comparten IP, red y volúmenes**.
* Usa un **runtime** subyacente (Docker, containerd, CRI-O...).
* **Gestión automática:** despliegue, escalado, recuperación, balanceo.
* Ideal para **entornos de producción distribuidos**.
* Permite **alta disponibilidad** y **resiliencia**.

---

## 🧾 **Resumen comparativo**

| Tipo de contenedor  | Nivel de virtualización      | Kernel propio       | Usa daemon | Rootless            | Orientado a            | Orquestación                | Ejemplo de uso                     |
| ------------------- | ---------------------------- | ------------------- | ---------- | ------------------- | ---------------------- | --------------------------- | ---------------------------------- |
| **Docker**          | Aislamiento de procesos      | NO                   | SI          | Parcial             | Aplicaciones           | Docker Compose / Kubernetes | Desarrollo y despliegue de apps    |
| **Podman**          | Aislamiento de procesos      | NO                   | NO          | SI                   | Aplicaciones seguras   | Podman pods / systemd       | Servidores y entornos multiusuario |
| **LXC/LXD**         | Virtualización ligera del SO | NO                   | NO          | Parcial             | Sistemas completos     | LXD clustering              | Laboratorios o servidores Linux    |
| **Kubernetes Pods** | Orquestación de contenedores | Depende del runtime | NO          | Depende del runtime | Servicios distribuidos | Kubernetes                  | Producción a gran escala           |

---

¿Quieres que te prepare una **versión esquemática visual** (tipo infografía o diagrama comparativo) para usarla en tus apuntes o presentaciones en clase?
