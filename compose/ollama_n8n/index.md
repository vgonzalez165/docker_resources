# Ollama + n8n

## Resumen

Ollama es una herramienta ligera y eficiente diseñada para **ejecutar Modelos de Lenguaje Grandes (LLMs) de forma local**, permitiendo gestionar y consumir modelos de inteligencia artificial (como Llama o Qwen) de manera privada sin depender de APIs externas.

n8n es una potente herramienta de **automatización de flujos de trabajo basada en nodos**. Cuenta con integraciones nativas de IA avanzada (LangChain) que facilitan la creación de agentes autónomos, asistentes y pipelines de datos inteligentes conectando múltiples servicios entre sí.

Este stack combina ambos servicios en local: el servidor de modelos de IA (Ollama) y el orquestador visual (n8n), creando la infraestructura base ideal para un entorno de *vibe coding* y automatización inteligente.

| Servicio | Imagen               | Versión | Puertos     | Volúmenes                   | Red                  |
| -------- | -------------------- | ------- | ----------- | --------------------------- | -------------------- |
| ollama   | ollama/ollama:latest | latest  | 11434:11434 | `ollama_data:/root/.ollama` | por defecto (bridge) |
| n8n      | n8nio/n8n:latest     | latest  | 5678:5678   | `n8n_data:/home/node/.n8n`  | por defecto (bridge) |

## Servicios definidos

- **ollama** → servidor local y gestor de modelos de inteligencia artificial (LLMs).
- **n8n** → plataforma de automatización de flujos de trabajo y desarrollo de agentes de IA.

## Puertos expuestos

- `11434` → puerto de la API local de Ollama (compatible con el estándar de OpenAI).
- `5678` → interfaz web de usuario y webhook receptor de n8n.


## Credenciales por defecto

### Ollama

- **Autenticación**: No requiere credenciales por defecto para conexiones en la red local o dentro de Docker.

### n8n

- **Usuario/Contraseña**: No se definen variables de entorno rígidas. El sistema solicitará **crear la primera cuenta de administrador** directamente en el navegador durante el primer acceso a `http://localhost:5678`.


## Volúmenes y persistencia

| Ruta Host (Volumen Docker) | Ruta Contenedor   | Servicio | Propósito |
| -------------------------- | ----------------- | -------- | --------- |
| `ollama_data`              | `/root/.ollama`   | `ollama` | Almacenamiento persistente de los modelos LLM descargados para evitar tener que volver a descargarlos al reiniciar el contenedor. |
| `n8n_data`                 | `/home/node/.n8n` | `n8n`    | Almacenamiento de la base de datos interna de n8n, configuraciones, credenciales guardadas e historial de flujos ejecutados. |

## Archivos relacionados

- [compose.yml](https://www.google.com/search?q=./compose.yml)

## Notas adicionales

- El servicio `n8n` tiene una directiva `depends_on` con respecto a `ollama`, asegurando que el motor de IA arranque primero.
- Para conectar n8n con Ollama dentro de la red interna de Docker, se debe configurar el nodo de Ollama en la interfaz web de n8n usando la siguiente URL base:
```text
http://ollama:11434

```

- Tras levantar el contenedor por primera vez, el servidor de Ollama estará vacío. Es necesario realizar una descarga inicial del modelo de código deseado ejecutando el comando de descarga en la terminal del host:
```bash
docker exec -it ollama ollama run qwen2.5-coder:14b

```



## Operaciones habituales con Ollama

Al ejecutarse Ollama dentro de un contenedor Docker, todas las interacciones desde la terminal del sistema operativo (Host) se realizan invocando al contenedor mediante `docker exec`.

| Operación / Propósito        | Comando Docker                                         | Notas / Descripción                                                                  |
| ---------------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| **Descargar un modelo**      | `docker exec -it ollama ollama pull qwen2.5-coder:14b` | Baja el modelo al disco en segundo plano sin iniciar una conversación.               |
| **Listar modelos locales**   | `docker exec -it ollama ollama list`                   | Muestra todos los modelos descargados en el volumen persistente y su tamaño.         |
| **Iniciar chat interactivo** | `docker exec -it ollama ollama run qwen2.5-coder:14b`  | Abre una sesión de chat en la terminal. Para salir del prompt, escribe `/exit`.      |
| **Ver modelos en RAM**       | `docker exec -it ollama ollama ps`                     | Muestra qué modelos están cargados en memoria en ese instante y cuánta RAM consumen. |
| **Eliminar un modelo**       | `docker exec -it ollama ollama rm qwen2.5-coder:14b`   | Borra el modelo del almacenamiento local para liberar espacio en disco.              |



## Modelos más adecuados para integrar con n8n

| Modelo (Tag de Ollama)         | Tamaño / RAM | Especialidad en n8n                       | Por qué elegirlo |
| ------------------------------ | ------------ | ----------------------------------------- | ---------------- |
| **`qwen2.5-coder:14b`**        | 14B (~9 GB)  | Generación de scripts y nodos de código   | El mejor equilibrio velocidad/calidad si necesitas que n8n escriba y ejecute código Python/JS sobre la marcha. |
| **`qwen2.5:32b`** *(Instruct)* | 32B (~22 GB) | Agente autónomo global y lógica compleja  | Su alta capacidad de razonamiento lo hace perfecto para actuar como el "cerebro" central de tu agente de n8n, decidiendo qué herramientas usar. |
| **`llama3.1:8b`**              | 8B (~5 GB)   | Clasificación rápida y formateo de datos  | Extremadamente rápido en CPU. Ideal para tareas repetitivas y ligeras (ej: leer un email entrante y clasificarlo como "Soporte", "Ventas" o "Spam"). |
| **`mistral-nemo:12b`**         | 12B (~8 GB)  | Extracción de datos y textos multilingües | Excelente ventana de contexto (hasta 128k tokens). Muy útil si n8n tiene que leer PDFs largos o transcripciones de audio antes de procesarlos. |

### Casos de uso típicos en tus flujos de n8n

- **Agentes Autónomos con herramientas (Tool Calling):** para esto, usa **`qwen2.5:32b`** o **`llama3.1:8b`**. Tienen soporte nativo en Ollama para entender los nodos "Tool" de n8n (pueden decidir por sí mismos cuándo consultar Wikipedia, cuándo calcular algo o cuándo llamar a una API externa).
- **Transformación y limpieza de datos:** si recibes datos en bruto (un webhook desordenado, un raspado web) y quieres transformarlo en un JSON limpio con campos específicos, **`qwen2.5:14b`** destaca formateando salidas estructuradas sin romperse.
- **Automatizaciones de alta velocidad:** si tu flujo de n8n se dispara muchas veces por minuto es mejor usar un modelo ligero como **`llama3.1:8b`**. Procesará los datos rápidamente sin .

