# API SIMULACIÓN SERVICIO URGENCIAS DE HOSPITAL

## 1. Resumen

Este contenedor contiene un microservicio sintético desarrollado con FastAPI que emite en tiempo real admisiones clínicas de urgencias estructuradas bajo el Sistema de Triaje Manchester (MTS) y notificaciones de alta hospitalaria. Está diseñado como generador de flujos continuos  para prácticas de ingesta, validación, transformación y persistencia en arquitecturas de IA y Big Data.

Este componente se construye dinámicamente mediante un `Dockerfile` local y se integra en la red corporativa compartida para alimentar canalizaciones de datos (Kafka, Spark Streaming, scripts Python o bases de datos NoSQL).

- **Servicio**: api-urgencias
- **Contexto Build**: `./compose/api-urgencias`
- **Imagen resultante**: Local (api-urgencias:latest)
- **Puertos**: `28000`:`28000`
- **Red**: `shared-network` (externa)
- **Persistencia**: En memoria (RAM)


## 2. Arquitectura de construcción (Dockerfile)

La imagen se construye a medida para optimizar el peso final y acelerar el ciclo de desarrollo:

- **Imagen base**: `python:3.11-slim`, seleccionada para minimizar la superficie de vulnerabilidades y mantener la imagen por debajo de los 150 MB.
- **Variables de entorno del entorno Python**:
  - `PYTHONUNBUFFERED=1`: fuerza la salida inmediata de `stdout` y `stderr` a los logs del contenedor Docker sin retención en búfer.
  - `PYTHONDONTWRITEBYTECODE=1`: evita generar ficheros `.pyc` dentro del contenedor.
- **Servidor ASGI**: se utiliza Uvicorn con un único worker (`--workers 1`), condición obligatoria dado que el estado del censo hospitalario se gestiona en la memoria RAM del proceso.


## 3. Puertos expuestos

- Puerto `28000`: interfaz HTTP unificada
- Documentación interactiva Swagger UI: [http://IP_SERVIDOR:28000/docs](http://IP_SERVIDOR:28000/docs)
- Endpoint de consumo de eventos: [http://IP_SERVIDOR:28000/api/v1/urgencias/novedades](http://IP_SERVIDOR:28000/api/v1/urgencias/novedades)
- Endpoints del panel de control docente



## 4. Especificación de la API REST

La API expone los siguientes endpoints:


| Método | Endpoint                               | Perfil            | Descripción                                                                      |
| ------ | -------------------------------------- | ----------------- | -------------------------------------------------------------------------------- |
| `GET`  | `/api/v1/urgencias/novedades`          | Alumnos (Polling) | Devuelve los nuevos ingresos y altas acumulados y vacía los buffers intermedios. |
| `POST` | `/api/v1/profesor/inyectar-emergencia` | Docente           | Fuerza la llegada inmediata de un paciente crítico (Nivel Manchester 1 o 2).     |
| `POST` | `/api/v1/profesor/forzar-alta`         | Docente           | Genera el alta médica de un episodio concreto o del paciente más antiguo.        |
| `GET`  | `/api/v1/simulador/estado`             | Monitorización    | Muestra el recuento del censo activo y el tamaño actual de las colas.            |
| `POST` | `/api/v1/simulador/reset`              | Docente           | Limpia todos los buffers y el censo activo para reiniciar la práctica.           |


## 5. Dinámica de la simulación

Ciclo del temporizador interno:

- Cada 10 a 15 segundos: genera una admisión clínica -> se añade a buffer_nuevos_ingresos -> se registra en Censo Activo.
- Cada 20 a 30 segundos: genera un alta hospitalaria -> se retira del Censo Activo -> se añade a buffer_altas.

Consumo destructivo de novedades:
Al invocar `/api/v1/urgencias/novedades`, el microservicio entrega los eventos pendientes y ejecuta el método `clear` sobre las listas intermedias, simulando una cola transaccional.


## 6. Archivos relacionados

- [`Dockerfile`](./Dockerfile): instrucciones de compilación del entorno Python y dependencias.
- [`compose.yml`](./compose.yml): orquestación del contenedor, mapeo de puertos y enlace de red.
- [`requirements.txt`](./requirements.txt): librerías mínimas requeridas (fastapi, uvicorn, pydantic).
- [`main.py`](./main.py): código fuente del servidor, modelos Pydantic y lógica de generación.
- [`api_urgencias.zip`](./api_urgencias.zip): fichero comprimidos en formato ZIP


## 7. Consideraciones operativas

- **Concurrencia en aula**: dado que el endpoint /novedades vacía las colas en cada llamada, si varios alumnos realizan peticiones contra el mismo contenedor competirán por los eventos (comportamiento tipo cola de trabajo / work queue). Para evaluaciones individuales se recomienda desplegar una réplica del contenedor por grupo o modificar el endpoint para aceptar un parámetro de filtrado temporal (cursor_timestamp).
- **Persistencia volátil**: los datos generados no se guardan en volúmenes Docker; reiniciar el contenedor reinicializa el contador de episodios y vacía el censo.
- **Red compartida**: requiere que exista la red Docker `shared-network` previamente a la orden `docker compose up -d`.