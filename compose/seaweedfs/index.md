# SeaweedFS (S3 Corporativo)

## Resumen

**SeaweedFS** es un sistema de almacenamiento distribuido de objetos y archivos de **código abierto (Apache 2.0)**, diseñado para gestionar miles de millones de ficheros con **baja latencia**, **mínimo consumo de recursos** y **alta concurrencia**.
Incorpora de serie una **API compatible con Amazon S3**, lo que permite integrarlo de forma nativa en canalizaciones de **IA y Big Data** mediante librerías estándar como `boto3`, PySpark, DuckDB o Pandas.

Este stack despliega un servidor SeaweedFS unificado (Master, Volume, Filer y S3 Gateway) conectado a una red corporativa compartida. Utiliza un archivo de configuración declarativo para aplicar políticas de **control de acceso basado en identidades (IAM)**, asegurando un entorno de **solo lectura** para los alumnos y restringiendo la interfaz de administración web al equipo docente.

| Servicio    | Imagen                       | Versión | Puertos                            | Volúmenes                                             | Red                        |
| ----------- | ---------------------------- | ------- | ---------------------------------- | ----------------------------------------------------- | -------------------------- |
| `seaweedfs` | `chrislusf/seaweedfs:latest` | latest  | `8333:8333`, `127.0.0.1:7777:8888` | `./data:/data`, `./s3.json:/etc/seaweedfs/s3.json:ro` | `shared-network` (externa) |

## Servicios definidos

* **seaweedfs** → servidor de almacenamiento de objetos con soporte para API S3 (puerto `8333`) y gestor de archivos Filer (puerto `8888`).

## Puertos expuestos

* `8333` → punto de entrada a la **API S3** accesible en la red corporativa para scripts de ingesta y análisis (`boto3`, PySpark, LangChain, etc.).
* `127.0.0.1:8888` → consola web y explorador de archivos del Filer, **restringido exclusivamente al anfitrión local** (`localhost`) para administración docente.

## Control de acceso y políticas S3 (`s3.json`)

El control de permisos se gestiona a través de identidades definidas en el archivo `./s3.json`:

| Identidad       | Claves de acceso                 | Acciones permitidas                         | Propósito / Alcance                                                                           |
| --------------- | -------------------------------- | ------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `admin_docente` | `admin`<br>`AdminSecretKey2026!` | `Admin`, `Read`, `Write`, `List`, `Tagging` | Control total del servidor: creación de buckets y carga del corpus oficial.                   |
| `alumnos`       | `alumno`<br>`paso`               | `Read`, `List`                              | Consulta de catálogos y descarga de datasets en cualquier bucket; bloquea creación y borrado. |
| `anonymous`     | *(Sin autenticación)*            | `Read`, `List`                              | Permite la lectura anónima y descarga de datos sin firma AWS para ejercicios simplificados.   |

## Volúmenes y persistencia

| Volumen / Ruta                        | Tipo                      | Servicio    | Propósito                                                                             |
| ------------------------------------- | ------------------------- | ----------- | ------------------------------------------------------------------------------------- |
| `./data:/data`                        | Bind Mount                | `seaweedfs` | Persistencia de los bloques de almacenamiento, metadatos del Filer y chunks de datos. |
| `./s3.json:/etc/seaweedfs/s3.json:ro` | Bind Mount (solo lectura) | `seaweedfs` | Inyección de credenciales, identidades y políticas de seguridad S3.                   |

## Archivos relacionados

- [`docker-compose.yml`](./compose.yml) → definición del servicio, puertos, mapeos y red compartida.
- [`s3.json`](./s3.json) → definición de usuarios IAM y privilegios de lectura/escritura en buckets.
- `./data/` → directorio local persistente en el host donde residen los datos físicos.

## Notas adicionales

- **Requisito de red:** como el stack utiliza una red externa (`shared-network`), debe crearse antes de levantar el contenedor mediante `docker network create shared-network`
- **Aislamiento de la consola web:** la vinculación a `127.0.0.1:8888` bloquea intentos de acceso web desde máquinas externas. La interfaz gráfica solo es accesible desde el propio servidor o a través de un túnel SSH (`ssh -L 8888:localhost:8888 usuario@ip-servidor`).
- **Conexión cliente S3:** para conectarse desde scripts en Python, hay que definir el endpoint explícito en `http://<ip-servidor>:8333` junto con sus credenciales de solo lectura.