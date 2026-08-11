# InfluxDB 2

## Resumen

**InfluxDB 2** es una base de datos **time-series (serie temporal)** diseñada para almacenar, consultar y analizar datos que varían con el tiempo, como métricas, logs, o datos de sensores IoT.
Se caracteriza por su **alto rendimiento**, **modelo de datos eficiente** y un lenguaje de consultas propio llamado **Flux**.

Este stack levanta una instancia de InfluxDB 2 totalmente inicializada y lista para su uso, utilizando **secretos de Docker** para gestionar las credenciales de manera segura y garantizando la **persistencia de los datos y la configuración**.

| Servicio  | Imagen     | Versión | Puertos   | Volúmenes                                                            | Red por defecto |
| --------- | ---------- | ------- | --------- | -------------------------------------------------------------------- | --------------- |
| influxdb2 | influxdb:2 | 2.x     | 8086:8086 | `influxdb2-data`, `influxdb2-config`, `./flux-scripts:/flux-scripts` | default         |


## Servicios definidos

- **influxdb2** → base de datos de series temporales, con interfaz web y API REST en el puerto `8086`.



## Puertos expuestos

- `8086` → interfaz web, API y punto de entrada para clientes (CLI, Python, Grafana, etc.).


## Credenciales y configuración inicial

Durante la primera ejecución, InfluxDB se configura automáticamente mediante variables de entorno y secretos:

| Parámetro                               | Valor                                   | Descripción                                      |
| --------------------------------------- | --------------------------------------- | ------------------------------------------------ |
| `DOCKER_INFLUXDB_INIT_MODE`             | `setup`                                 | Modo de inicialización del contenedor.           |
| `DOCKER_INFLUXDB_INIT_ORG`              | `docs`                                  | Nombre de la organización inicial.               |
| `DOCKER_INFLUXDB_INIT_BUCKET`           | `home`                                  | Bucket por defecto donde se almacenan los datos. |
| `DOCKER_INFLUXDB_INIT_USERNAME_FILE`    | `/run/secrets/influxdb2-admin-username` | Usuario administrador.                           |
| `DOCKER_INFLUXDB_INIT_PASSWORD_FILE`    | `/run/secrets/influxdb2-admin-password` | Contraseña del usuario administrador.            |
| `DOCKER_INFLUXDB_INIT_ADMIN_TOKEN_FILE` | `/run/secrets/influxdb2-admin-token`    | Token de autenticación para la API.              |

Los ficheros `.env.influxdb2-admin-*` almacenan los valores reales y deben **crearse manualmente** antes de levantar el servicio.



## Volúmenes y persistencia

| Volumen / Ruta                 | Tipo          | Servicio    | Propósito                                            |
| ------------------------------ | ------------- | ----------- | ---------------------------------------------------- |
| `influxdb2-data`               | Docker Volume | `influxdb2` | Almacena los datos de series temporales.             |
| `influxdb2-config`             | Docker Volume | `influxdb2` | Guarda la configuración y metadatos de la instancia. |
| `./flux-scripts:/flux-scripts` | Bind Mount    | `influxdb2` | Permite ejecutar o importar scripts Flux locales.    |



## Secretos gestionados por Docker

Estos ficheros deben crearse en el mismo directorio que el fichero `compose.yml` y cada uno debe contener únicamente el elemento al que hacen referencia. Por ejemplo, el fichero `.env.influxdb2-admin-username` contendrá una única línea con el nombre de usuario del administrador.

| Secreto                    | Archivo asociado                | Contenido                            |
| -------------------------- | ------------------------------- | ------------------------------------ |
| `influxdb2-admin-username` | `.env.influxdb2-admin-username` | Nombre de usuario administrador.     |
| `influxdb2-admin-password` | `.env.influxdb2-admin-password` | Contraseña de acceso.                |
| `influxdb2-admin-token`    | `.env.influxdb2-admin-token`    | Token de autenticación para API/CLI. |


## Archivos relacionados

- [compose.yml](./compose.yml) → definición del stack de servicios.
- `.env.influxdb2-admin-username` → contiene el nombre de usuario admin.
- `.env.influxdb2-admin-password` → contiene la contraseña.
- `.env.influxdb2-admin-token` → contiene el token de autenticación.
- `./flux-scripts/` → carpeta con consultas o scripts en lenguaje **Flux**.


## Notas adicionales

- Este stack crea automáticamente una organización y un bucket inicial llamados **`docs`** y **`home`** respectivamente.
- Se puede acceder a la **interfaz web** en `http://localhost:8086` autenticándose con las credenciales configuradas.
- Los datos se almacenan de forma persistente en los volúmenes `influxdb2-data` y `influxdb2-config`.
- Para conectarse desde un cliente externo (por ejemplo, Grafana o Telegraf), se debe utilizar el token definido en `.env.influxdb2-admin-token`.

