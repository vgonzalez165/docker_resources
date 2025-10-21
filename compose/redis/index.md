# Redis Database

## Resumen

**Redis** es una base de datos en memoria, de tipo clave–valor, diseñada para ser extremadamente rápida. A diferencia de bases de datos tradicionales que guardan los datos en disco, Redis los mantiene en RAM, lo que permite acceder a ellos en microsegundos.

Se utiliza principalmente como caché, cola de mensajes o para gestionar sesiones en aplicaciones web, pero también admite estructuras de datos avanzadas como listas, conjuntos, hashes o mapas ordenados.


| Servicio  | Imagen      | Versión | Puertos   | Volúmenes                | Red     |
|-----------|-------------|---------|-----------|--------------------------|---------|
| redis     | redis:7.2   | 7.2     | 6379:6379 | `redis-data:/data`<br>`./redis.conf:/usr/local/etc/redis/redis.conf`      | shared_network |


## Servicios definidos

- **redis** → base de datos clave-valor


## Puertos expuestos

* `6379` → puerto que atiende las operaciones del protocolo propio de Redis (RESP - Redis Serialization Protocol)


## Credenciales por defecto

- Sin credenciales


## Volúmenes y persistencia

| Ruta Host (local)                 | Ruta Contenedor             | Servicio     | Propósito                                |
|-----------------------------------|-----------------------------|--------------|------------------------------------------|
|                                   | `/data`                     | `redis`      | Información de la base de datos para mantener la persistencia al destruir el contenedor                   |
| `./redis.conf` | `/usr/local/etc/redis/redis.conf`   | `redis`       | Archivo de configuración de Redis, para poder ser configurado desde el equipo anfitrión
 |


## Archivos relacionados

- [compose.yml](./compose.yml)


## Notas adicionales



