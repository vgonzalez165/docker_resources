# Cassandra + DataStax Studio

## Resumen

**Apache Cassandra** es una base de datos **NoSQL distribuida** diseñada para manejar grandes volúmenes de datos con alta disponibilidad, escalabilidad horizontal y sin un único punto de fallo. Utiliza un modelo basado en **columnas** y ofrece replicación automática entre nodos.

**DataStax Studio** es una herramienta visual desarrollada por DataStax que permite interactuar con Cassandra desde una **interfaz web**, facilitando la ejecución de consultas CQL (Cassandra Query Language) y la visualización de los resultados.

Este stack proporciona un entorno completo de aprendizaje con un servidor Cassandra persistente y una interfaz web para practicar consultas y visualizar datos.

| Servicio        | Imagen                      | Versión | Puertos   | Volúmenes                   | Red           |
| --------------- | --------------------------- | ------- | --------- | --------------------------- | ------------- |
| cassandra       | cassandra:4.1               | 4.1     | 9042:9042 | `./data:/var/lib/cassandra` | cassandra-net |
| datastax-studio | datastax/dse-studio\:latest | latest  | 9091:9091 | —                           | cassandra-net |

## Servicios definidos

* **cassandra** → base de datos NoSQL orientada a columnas, con persistencia en disco.
* **datastax-studio** → interfaz web interactiva para ejecutar consultas CQL sobre Cassandra.

## 🌐 Puertos expuestos

* `9042` → puerto estándar de Cassandra para conexiones CQL.
* `9091` → interfaz web de DataStax Studio accesible desde el navegador.

## Credenciales por defecto

Cassandra, por defecto, no requiere credenciales para conexiones locales si no se ha activado la autenticación.
En caso de configurarse, los valores utilizados en el archivo `.env` son:

* **Usuario:** `cassandra`
* **Contraseña:** `cassandra`

## Volúmenes y persistencia

| Ruta Host (local) | Ruta Contenedor      | Servicio    | Propósito                                                                                                |
| ----------------- | -------------------- | ----------- | -------------------------------------------------------------------------------------------------------- |
| `./data`          | `/var/lib/cassandra` | `cassandra` | Almacena los datos de la base de datos Cassandra para mantener persistencia tras eliminar el contenedor. |

## Variables gestionadas por `.env`

El fichero `.env` permite modificar fácilmente los parámetros de despliegue sin editar el `docker-compose.yml`.

| Variable                 | Descripción                                                  |
| ------------------------ | ------------------------------------------------------------ |
| `CASSANDRA_VERSION`      | Versión de la imagen Cassandra.                              |
| `CASSANDRA_CLUSTER_NAME` | Nombre del clúster de Cassandra.                             |
| `CASSANDRA_DC`           | Nombre del centro de datos (Data Center).                    |
| `CASSANDRA_RACK`         | Identificador del rack lógico.                               |
| `CASSANDRA_PORT`         | Puerto de exposición de Cassandra (por defecto, 9042).       |
| `STUDIO_PORT`            | Puerto de acceso web de DataStax Studio (por defecto, 9091). |
| `NETWORK_NAME`           | Nombre de la red Docker compartida.                          |

## Archivos relacionados

* [docker-compose.yml](./docker-compose.yml)
* [.env](./.env)

## Notas adicionales

* Ambos servicios se conectan a través de la red `cassandra-net`, definida en el fichero `.env`.

* Para iniciar el entorno, ejecutar en la carpeta del proyecto:

  ```bash
  docker compose up -d
  ```

* Una vez desplegado, se puede acceder a la interfaz web en:
  👉 [http://localhost:9091](http://localhost:9091)

* Para conectarse desde DataStax Studio, crear una nueva conexión con los siguientes parámetros:

  * **Host:** `cassandra_db`
  * **Puerto:** `9042`

* Se recomienda **aumentar el tiempo de espera** en la conexión inicial, ya que Cassandra puede tardar en iniciar la primera vez.


