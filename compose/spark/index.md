# Apache Spark Cluster + JupyterLab

## Resumen

**Apache Spark** es un motor de análisis unificado para el procesamiento de datos a gran escala. Ofrece módulos para SQL, streaming, aprendizaje automático (MLlib) y procesamiento de grafos. En esta arquitectura, se despliega un cluster independiente (Standalone Mode) junto con un entorno de cliente interactivo.

El despliegue consta de tres partes principales: un **Master** (coordinador), un **Worker** (ejecutor de tareas) y un **Driver** (JupyterLab) desde donde se lanza el código PySpark.

| Servicio         | Imagen / Build                                | Versión Spark | Puertos (Host:Contenedor)             | Volúmenes                  | Dependencias |
|------------------|-----------------------------------------------|---------------|---------------------------------------|----------------------------|--------------|
| spark-master     | `spark:3.5.7-scala2.12-java11-python3-ubuntu` | 3.5.7         | 8080:8080<br>7077:7077<br>4040:4040   | -                          | -            |
| spark-worker-1   | `spark:3.5.7-scala2.12-java11-python3-ubuntu` | 3.5.7         | 8081:8081                             | -                          | spark-master |
| jupyter-driver   | *Build local (Dockerfile)* | 3.5.7         | 8899:8888                             | `./notebooks:/workspace`   | spark-master |


## Servicios definidos

- **spark-master** → Nodo coordinador del cluster. Gestiona los recursos y la planificación de tareas.
- **spark-worker-1** → Nodo trabajador. Ejecuta las tareas de cómputo asignadas por el master (2 Cores, 2GB RAM asignados).
- **jupyter-driver** → Contenedor cliente con **JupyterLab**, Python 3.10 y librerías de Spark preinstaladas. Actúa como el "Driver" que envía trabajos al cluster.


## Puertos expuestos

* `8080` → Interfaz Web (UI) del Spark Master. Muestra el estado del cluster y los workers conectados.
* `8081` → Interfaz Web (UI) del Spark Worker. Muestra logs y estado de ejecución del nodo trabajador.
* `7077` → Puerto de comunicación interna del Master (spark:// protocol).
* `4040` → Spark Context UI. Muestra el detalle de los Jobs y Stages en ejecución actual (del driver).
* `8899` → Acceso a **JupyterLab** (mapeado desde el puerto interno 8888).


## Credenciales por defecto

- **JupyterLab:** Sin token (configurado con `--NotebookApp.token=''`). Acceso directo.
- **Spark Auth:** Deshabilitada (`SPARK_RPC_AUTHENTICATION_ENABLED=no`).


## Volúmenes y persistencia

| Ruta Host (local) | Ruta Contenedor | Servicio         | Propósito                                                                 |
|-------------------|-----------------|------------------|---------------------------------------------------------------------------|
| `./notebooks`     | `/workspace`    | `jupyter-driver` | Persistencia de los cuadernos de Jupyter (.ipynb) y scripts de Python.    |


## Detalles de Construcción (Dockerfile)

La imagen `jupyter-driver` se construye localmente con las siguientes características:
* **Base:** `python:3.10-slim`
* **Java:** OpenJDK 21 (Headless)
* **Spark:** 3.5.7 (Binarios oficiales con Hadoop 3)
* **Librerías Python:** `jupyterlab`, `notebook`, `findspark`, `pyspark==3.5.7`


## Archivos relacionados

- [compose.yml](./compose.yml)
- [Dockerfile](./Dockerfile)