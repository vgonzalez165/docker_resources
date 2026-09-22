# Focalboard

## Resumen

**Focalboard** es una herramienta de código abierto y autoalojada para la gestión de tareas y proyectos, desarrollada como alternativa a plataformas como Trello, Notion o Asana. Ofrece organización visual de flujos de trabajo mediante vistas en tableros Kanban, tablas, calendarios y galerías.

Este stack despliega una arquitectura multi-contenedor compuesta por la aplicación **Focalboard** y un motor de base de datos dedicado **PostgreSQL 16 (Alpine)**, garantizando un rendimiento óptimo, control de concurrencia y la **persistencia completa de los tableros, metadatos y archivos adjuntos**.

| Servicio      | Imagen                       | Versión   | Puertos          | Volúmenes            | Red por defecto |
| ------------- | ---------------------------- | --------- | ---------------- | -------------------- | --------------- |
| focalboard    | mattermost/focalboard:latest | latest    | 8000:8000        | `focalboard-data`    | default         |
| focalboard-db | postgres:16-alpine           | 16-alpine | *(solo interno)* | `focalboard-db-data` | default         |

## Servicios definidos

- **focalboard** → servidor de aplicaciones que proporciona la interfaz web y la API REST de Focalboard.
- **focalboard-db** → base de datos relacional PostgreSQL 16 encargada del almacenamiento transaccional de usuarios, espacios de trabajo y tableros.

## Puertos expuestos

- `8000` → acceso a la interfaz web y endpoints de Focalboard desde el host.

## Variables de entorno y configuración

### Focalboard (`focalboard`)

| Variable       | Valor                                                                                             | Descripción                                                                          |
| -------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| `FB_DBTYPE`    | `postgres`                                                                                        | Especifica el motor de base de datos a utilizar.                                     |
| `FB_DBCONNSTR` | `postgres://focalboard_user:focalboard_password@focalboard-db:5432/focalboard_db?sslmode=disable` | Cadena de conexión JDBC/PostgreSQL para comunicarse con el servicio `focalboard-db`. |

### PostgreSQL (`focalboard-db`)

| Variable            | Valor                 | Descripción                                                  |
| ------------------- | --------------------- | ------------------------------------------------------------ |
| `POSTGRES_USER`     | `focalboard_user`     | Nombre de usuario administrador de la base de datos.         |
| `POSTGRES_PASSWORD` | `focalboard_password` | Contraseña asignada al usuario de la base de datos.          |
| `POSTGRES_DB`       | `focalboard_db`       | Nombre de la base de datos creada durante la inicialización. |

**Nota:** ee recomienda sustituir `focalboard_password` por una contraseña segura tanto en la cadena de conexión (`FB_DBCONNSTR`) como en `POSTGRES_PASSWORD` antes de desplegar en entornos compartidos o de producción.

## Volúmenes y persistencia

| Volumen / Ruta       | Tipo          | Servicio        | Propósito                                                                                |
| -------------------- | ------------- | --------------- | ---------------------------------------------------------------------------------------- |
| `focalboard-data`    | Docker Volume | `focalboard`    | Almacena archivos subidos, imágenes y adjuntos asociados a las tarjetas.                 |
| `focalboard-db-data` | Docker Volume | `focalboard-db` | Almacena los ficheros del clúster de datos de PostgreSQL (esquemas, tablas y registros). |

## Comprobación de estado y dependencias

Para evitar errores de conexión al arrancar el stack, el servicio `focalboard` cuenta con una condición de dependencia estricta:

- **Healthcheck en `focalboard-db`**: ejecuta periódicamente `pg_isready -U focalboard_user -d focalboard_db` cada 5 segundos.
- **Orden de arranque (`depends_on`)**: `focalboard` espera activamente a que `focalboard-db` alcance el estado `service_healthy` antes de inicializar el proceso principal de la aplicación.

## Archivos relacionados

- [compose.yml](./compose.yml) → definición del stack de servicios, salud de contenedores y volúmenes.

## Notas adicionales

- **Primer acceso y registro**: al acceder por primera vez a `http://localhost:8000`, la aplicación solicitará registrar la primera cuenta de usuario, la cual asumirá el rol de administrador inicial.
- **Reinicio automático**: ambos servicios cuentan con la directiva `restart: unless-stopped` para reanudar automáticamente la ejecución tras reinicios del host o del motor Docker.