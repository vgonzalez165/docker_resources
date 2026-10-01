# PORTAL SIMULACIÓN SERVICIO URGENCIAS DE HOSPITAL

## 1. Resumen

Este contenedor proporciona un servidor web ligero para la distribución y descarga directa de los conjuntos de datos históricos de la práctica hospitalaria. Actúa como origen de datos por lotes (*batch*) y repositorio base (*Data Lake Landing Zone*), complementando a los microservicios de generación en tiempo real (*streaming*).

Está diseñado para prácticas de ingesta por lotes, modelado relacional/documental, preprocesamiento de datos clínicos y entrenamiento de modelos de Machine Learning dentro del marco del Curso de Especialización en Inteligencia Artificial y Big Data.

- **Servicio**: `servidor-hospital`
- **Contenedor**: `hospital_datos_web`
- **Imagen base**: `python:3-alpine` (Docker Hub oficial)
- **Puertos**: `8088:8000`
- **Directorio de trabajo**: `/var/www/html`
- **Volúmenes**: `./web:/var/www/html:ro` (montaje en solo lectura)
- **Persistencia**: Basada en sistema de archivos del host (`./web`)


## 2. Configuración del contenedor y despliegue

este servicio utiliza una arquitectura minimalista sin dependencias externas:

- **Imagen base ultraligera**: `python:3-alpine` reduce la huella de memoria y almacenamiento al mínimo (~50 MB), minimizando la superficie de ataque y acelerando los tiempos de despliegue en entornos de aula.
- **Servidor HTTP integrado**: aprovecha el módulo estándar `http.server` de Python (`python -m http.server 8000`), evitando configurar servidores web dedicados (Nginx o Apache) para la entrega de activos estáticos.
- **Inmutabilidad de datos (`:ro`)**: el volumen local `./web` se enlaza en modo solo lectura (`read-only`), impidiendo que peticiones o scripts de los alumnos puedan sobrescribir, corromper o borrar accidentalmente los ficheros fuente durante las prácticas.


## 3. Puertos expuestos

- Puerto host `8088`: mapeado internamente al puerto `8000` del contenedor.


## 4. Catálogo de conjuntos de datos (Datasets)

El servidor expone mediante HTTP plano los siguientes recursos para las prácticas:

| Recurso                     | Formato    | Tipo de dato     | Descripción y caso de uso                                           |
| --------------------------- | ---------- | ---------------- | ------------------------------------------------------------------- |
| `/admisiones_historico.csv` | CSV        | Estructurado     | Registro tabular (CSV) de admisiones previas.                       |
| `/partes_clinicos.json`     | JSON       | Semiestructurado | Informes detallados de triaje de urgencias con jerarquías anidadas. |
| `/index.html`               | HTML / CSS | Web UI           | Portal de bienvenida y descarga manual desde navegador web.         |



## 5. Archivos relacionados

- [`docker-compose.yml`](./compose.yml): orquestación del servicio `servidor-hospital` y asignación de puertos.
- [`./web/index.html`](./web/index.html): código HTML y CSS del portal de autoservicio para los alumnos.
- [`./web/admisiones_historico.csv`](./web/admisiones_historico.csv): dataset fuente estructurado con el histórico hospitalario.
- [`./web/partes_clinicos.json`](./web/partes_clinicos.json): dataset fuente semiestructurado con los informes de triaje.


## 6. Consideraciones operativas

- **Actualización en caliente**: cualquier incorporación o corrección realizada sobre los ficheros en la carpeta local `./web` se reflejará inmediatamente en el servidor sin necesidad de reiniciar el contenedor.
- **Capacidad de concurrencia**: el servidor interno `http.server` de Python es monohilo; está optimizado para entornos de laboratorio docente (descargas de decenas de alumnos o llamadas batch puntuales), pero no para benchmarks de alto rendimiento o cargas masivas concurrentes.
- **Descargas automatizadas**: los enlaces del portal web cuentan con el atributo HTML `download`, permitiendo tanto la navegación interactiva desde navegadores cliente como la descarga desatendida mediante herramientas estándar CLI (`wget`, `curl`).