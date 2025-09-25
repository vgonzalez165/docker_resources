# 📦 MongoDB + Mongo Express

## 📋 Resumen

MongoDB es una base de datos **NoSQL orientada a documentos**, que almacena la información en formato BSON (JSON binario). Se caracteriza por su flexibilidad en el esquema, alta escalabilidad y rendimiento.

Mongo Express es una interfaz web ligera que permite administrar una instancia de MongoDB directamente desde el navegador, facilitando tareas como consultas, inserción de documentos y gestión de colecciones.

Este stack combina ambos servicios: la base de datos MongoDB y la interfaz de administración Mongo Express.

| Servicio      | Imagen              | Versión | Puertos     | Volúmenes               | Red            |
| ------------- | ------------------- | ------- | ----------- | ----------------------- | -------------- |
| mongo         | mongo:6.0           | 6.0     | 27017:27017 | `./mongo_data:/data/db` | shared-network |
| mongo-express | mongo-express:1.0.2 | 1.0.2   | 8081:8081   | —                       | shared-network |


## 🛠️ Servicios definidos

* **mongo** → base de datos NoSQL orientada a documentos.
* **mongo-express** → interfaz web para gestionar MongoDB.


## 🌐 Puertos expuestos

* `27017` → puerto de conexión estándar de MongoDB.
* `8081` → interfaz web de administración Mongo Express.

## 🔑 Credenciales por defecto

### MongoDB

* **Usuario root**: `root`
* **Contraseña**: `paso`

### Mongo Express

* **Usuario web (Basic Auth)**: `admin`
* **Contraseña web**: `secret`


## 💾 Volúmenes y persistencia

| Ruta Host (local) | Ruta Contenedor | Servicio | Propósito                                                                             |
| ----------------- | --------------- | -------- | ------------------------------------------------------------------------------------- |
| `./mongo_data`    | `/data/db`      | `mongo`  | Almacenamiento de los datos de MongoDB para persistencia tras destruir el contenedor. |



## 📂 Archivos relacionados

* [docker-compose.yml](./docker-compose.yml)


## 📝 Notas adicionales

- El servicio `mongo-express` depende de que `mongo` esté sano. Para ello se define un **healthcheck** que comprueba la conexión ejecutando `db.runCommand("ping")`.
- La red `shared-network` está definida como **externa**, por lo que debe existir previamente con:

  ```bash
  docker network create shared-network
  ```
- Es recomendable cambiar las contraseñas por defecto (`paso` y `secret`) en un entorno de producción.
