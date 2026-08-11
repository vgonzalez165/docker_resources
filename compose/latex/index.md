
# Overleaf (Community Edition)

## Resumen

**Overleaf Community Edition** (anteriormente ShareLaTeX) es un editor de LaTeX colaborativo en tiempo real y online. Permite la edición simultánea, historial de versiones y compilación de documentos PDF directamente desde el navegador.

Este stack despliega una instancia completa de Overleaf junto con sus dependencias críticas: **MongoDB** (configurado como Replica Set para soportar transacciones) y **Redis** (para la gestión de colas y sincronización en tiempo real). Incluye un servicio de **autoconfiguración** que inicializa la réplica de base de datos automáticamente, evitando intervenciones manuales.

| Servicio     | Imagen                | Versión | Puertos   | Volúmenes         | Dependencias |
| ------------ | --------------------- | ------- | --------- | ----------------- | ------------ |
| sharelatex   | sharelatex/sharelatex | latest  | 8844:80   | `./overleaf_data` | mongo, redis |
| mongo        | mongo                 | 8.0     | -         | `./mongo_data`    | -            |
| redis        | redis                 | 6.2     | -         | `./redis_data`    | -            |
| *mongo-init* | mongo                 | 8.0     | -         | -                 | mongo        |

## Servicios definidos

- **sharelatex** → La aplicación web principal, compilador de LaTeX y gestor de proyectos.
- **mongo** → Base de datos NoSQL persistente. 
- **redis** → Almacén en memoria para gestionar sesiones, caché y la sincronización en tiempo real entre usuarios.
- **mongo-init** → Contenedor efímero. Su única función es esperar a que la base de datos arranque e inyectar el comando `rs.initiate()` para configurar el Replica Set automáticamente. Se detiene tras completar su tarea.

## Puertos expuestos

- `8844` → Interfaz web de Overleaf.


## Credenciales y configuración inicial

En el primer inicio es necesario ir a la URL `https://localhost:8844/launchpad` para crear las credenciales del usuario administrador


## Configuración y variables de entorno

La configuración se gestiona principalmente a través del archivo `.env`. Las variables se inyectan en el contenedor `sharelatex` para definir la conexión con los servicios auxiliares.

| Variable (compose)    | Valor típico / Fuente | Descripción |
| -------------------   | --- | --- |
| `OVERLEAF_APP_NAME`   | `${OVERLEAF_APP_NAME}` | Nombre que aparece en la interfaz web. |
| `OVERLEAF_MONGO_URL`  | `mongodb://mongo:27017/sharelatex?replicaSet=rs0` | Cadena de conexión a la BD. **Importante:** Debe incluir `?replicaSet=rs0`. |
| `OVERLEAF_REDIS_HOST` | `redis` | Host del servicio de colas. |
| `ENABLE_CONVERSIONS`  | `true` | Habilita la conversión de documentos. |
| `OVERLEAF_EMAIL_*`    | *Variables opcionales* | Configuración SMTP para envío de correos (ver `.env`). |



## Volúmenes y persistencia

La persistencia de datos está garantizada mediante volúmenes definidos en el archivo `.env`.

| Volumen / Ruta    | Tipo       | Servicio     | Propósito                                               |
| ----------------- | ---------- | ------------ | ------------------------------------------------------- |
| `./overleaf_data` | Bind Mount | `sharelatex` | Almacena proyectos, PDFs compilados y datos de usuario. |
| `./mongo_data`    | Bind Mount | `mongo`      | Archivos de la base de datos MongoDB.                   |
| `./redis_data`    | Bind Mount | `redis`      | Persistencia de datos de Redis (dump).                  |


## Archivos relacionados

- [`docker-compose.yml`](./compose.yml) → Definición del stack de servicios y la lógica de inicialización.
- [`.env`](./.env) → Archivo de configuración donde se definen puertos, rutas de volúmenes y credenciales SMTP.


## Notas adicionales

- **Primer arranque:** el servicio `sharelatex` puede tardar varios minutos en estar disponible la primera vez, ya que debe compilar los recursos estáticos (CSS/JS) y esperar a que `mongo-init` termine de configurar la base de datos.
- **Creación de usuario Admin:** por defecto, la instalación no tiene usuarios. Tras levantar el stack, se debe crear el primer administrador ejecutando:
```bash
docker exec -it sharelatex /bin/bash -c "cd /var/www/sharelatex; bin/managevars.js create-admin-user --email tu@email.com"

```
- **MongoDB Replica Set:** Este stack soluciona automáticamente el error `Transaction numbers are only allowed on a replica set member` mediante el servicio `mongo-init`. No se requiere intervención manual en la base de datos.