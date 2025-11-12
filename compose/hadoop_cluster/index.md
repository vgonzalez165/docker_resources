# Clúster Hadoop con Jupyter

## Resumen

Este entorno despliega un clúster **Hadoop** (HDFS + YARN) de 6 nodos, junto con **Jupyter** y **Hive** para análisis de datos.

Se compone de un *NameNode* (que también ejecuta Jupyter/Hive), un *YARN Resource Manager* y cuatro *DataNodes*. 

| Servicio | Imagen | Versión | Puertos | Volúmenes | Red |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **namenode** | `vega90/hadoop-namenode:1.0` | 1.0 | `9870:9870` <br> `7777:8888` <br> `10000:10000` <br> `10002:10002` | `./notebooks:/media/notebooks` | `shared-network` |
| **yarnmanager** | `vega90/hadoop-yarn:1.0` | 1.0 | `8088:8088` <br> `19888:19888` | (ninguno) | `shared-network` |
| **datanode1** | `vega90/hadoop-datanode:1.0` | 1.0 | (ninguno) | (ninguno) | `shared-network` |
| **datanode2** | `vega90/hadoop-datanode:1.0` | 1.0 | (ninguno) | (ninguno) | `shared-network` |
| **datanode3** | `vega90/hadoop-datanode:1.0` | 1.0 | (ninguno) | (ninguno) | `shared-network` |
| **datanode4** | `vega90/hadoop-datanode:1.0` | 1.0 | (ninguno) | (ninguno) | `shared-network` |


## Servicios definidos

  - **namenode**: Nodo principal de HDFS. Gestiona la metadata del sistema de archivos. También ejecuta los servicios de Jupyter y Hive.
  - **yarnmanager**: Nodo principal de YARN. Gestiona los recursos del clúster (CPU, RAM) y la programación de tareas (Jobs).
  - **datanode(1-4)**: Nodos trabajadores de HDFS. Almacenan los bloques de datos reales.


## Puertos expuestos

  - `9870` → (NameNode) Interfaz web de **HDFS**.
  - `8088` → (YARN) Interfaz web del **Resource Manager**.
  - `19888` → (YARN) Interfaz web del **JobHistory Server**.
  - `7777` → (NameNode) Interfaz web de **Jupyter** (mapeado desde el puerto 8888 del contenedor).
  - `10000` → (NameNode) Puerto de conexión de cliente para **Hive**.
  - `10002` → (NameNode) Puerto de conexión de cliente para **HiveServer2** (para JDBC/ODBC).


## Credenciales por defecto

  * **Jupyter**: requiere un *token* para el primer acceso. Debes revisar los logs del contenedor `namenode` para encontrarlo:

## Volúmenes y persistencia

| Ruta Host (local) | Ruta Contenedor | Servicio | Propósito |
| :--- | :--- | :--- | :--- |
| `./notebooks` | `/media/notebooks` | `namenode` | Almacenamiento persistente para los *Jupyter Notebooks* creados. |

## Archivos relacionados

  - [compose.yml](./compose.yml)


## Notas adicionales

  - Esta configuración **requiere** que la red `shared-network` exista en Docker antes de ejecutar `docker-compose up`.
