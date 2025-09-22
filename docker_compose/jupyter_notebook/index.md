# 📦 Jupyter Data Science Notebook

## 📋 Resumen

Este entorno despliega un JupyterLab completo para ciencia de datos con Python. Utiliza la imagen oficial de Docker que incluye librerías populares como Pandas, Scikit-learn y Matplotlib, permitiendo un entorno de trabajo reproducible y listo para análisis, visualizaciones y modelos de machine learning.


| Servicio    | Imagen                         | Versión | Puertos   | Volúmenes                | Red     |
|-------------|--------------------------------|---------|-----------|--------------------------|---------|
| jupyter     | jupyter/datascience.notebook   | latest  | 8888:8888 | `./notebooks:/home/jovyan/work`      | shared_network |


## 🛠️ Servicios definidos

- **jupyter** → Entorno de desarrollo para ciencia de datos y machine learning


## 🌐 Puertos expuestos

- `8888` → Puerto para acceder a la interfaz web de JupyterLab desde el navegador


## 🔑 Credenciales por defecto

- Es necesario introducir el **token** que se muestra en el log de salida al arrancar el contenedor


## 💾 Volúmenes y persistencia

| Ruta Host (local)                 | Ruta Contenedor             | Servicio     | Propósito                                 |
|-----------------------------------|-----------------------------|--------------|-------------------------------------------|
| ./notebooks                       | `/home/jovyan/work`         | `jupyter`    | Mantiene la persistencia de los proyectos |



## 📂 Archivos relacionados

- [docker-compose.yml](./docker-compose.yml)


## 📝 Notas adicionales

- **Librerías preinstaladas**: esta imagen incluye por defecto herramientas como `NumPy`, `SciPy`, `Pandas`, `Matplotlib`, `Seaborn`, `Scikit-learn`, `NLTK`, `SQLAlchemy`, entre otras.


