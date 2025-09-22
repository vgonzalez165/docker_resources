# 📦 Neo4j

## 📋 Resumen

Neo4j es una base de datos orientada a grafos diseñada para almacenar, consultar y analizar datos con relaciones complejas de forma eficiente. Utiliza un modelo en el que la información se representa mediante nodos y relaciones, facilitando consultas avanzadas sobre estructuras interconectadas como redes sociales, rutas y recomendaciones


| Servicio  | Imagen      | Versión | Puertos   | Volúmenes                | Red     |
|-----------|-------------|---------|-----------|--------------------------|---------|
| neo4j     | neo4j:5     | 5       | `7074` `7687` | `/data` `/logs` `/var/lib/neo4j/import` `/plugins`       | shared_network |



## 🛠️ Servicios definidos

- **nep4j** → base de datos orienta a grafos Neo4j


## 🌐 Puertos expuestos

- `7474` → Interfaz web de administración y consulta
- `7687` → Puerto dedicado al protocolo Bolt para conexiones de clientes.


## 🔑 Credenciales por defecto

- **Neo4j**:
  - Usuario: `neo4j`
  - Contraseña: `P@ssw0rd`

## 💾 Volúmenes y persistencia

| Ruta Host (local)        | Ruta Contenedor         | Servicio     | Propósito                                |
|--------------------------|-------------------------|--------------|------------------------------------------|
| `./neo4j_data`           | `/data`                 | `neo4j`      | Persistencia de datos                    |
| `./neo4j_logs`           | `/logs`                 | `neo4j`      | Logs de la base de datos                 |
| `./neo4j_import`         | `/var/lib/neo4j/import` | `neo4j`      | Directorio para importar archivos CSV    |
| `./neo4j_plugins`        | `/plugins`              | `neo4j`      | Plugins adicionales                      |



## 📂 Archivos relacionados

- [docker-compose.yml](./docker-compose.yml)


## 📝 Notas adicionales

- 
