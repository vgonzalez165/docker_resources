# Odoo / PostgreSQL

## Resumen

Este entorno despliega Odoo 16 + PostgreSQL 14 para desarrollo local: ideal para crear módulos, probar funcionalidades o aprender Odoo con datos persistentes.


| Servicio  | Imagen      | Versión | Puertos   | Volúmenes                | Red     |
|-----------|-------------|---------|-----------|--------------------------|---------|
| odoo      | odoo:16     | 16      | 8069:8069 | `~/OdooDev/volumesOdoo/addons:/mnt/extra-addons` `~/OdooDev/volumesOdoo/filestore:/var/lib/odoo/filestore`      | shared_network |
| postgres  | postgres:14 | 14      |           | `~/OdooDev/dataPG:/var/lib/postgresql/data` | shared_network |



## Servicios definidos

- **odoo** → interfaz web de Odoo
- **postgres** → base de datos relacional utilizada por Odoo


## Puertos expuestos

* `8069` → interfaz gráfica de Odoo


## Credenciales por defecto

- **PostgreSQL**:
  - Usuario: `odoo`
  - Base de datos: `postgres`
  - Contraseña: `odoo`
- **Odoo**:
  - Usuario: `odoo`
  - Contraseña: `paso`


## Volúmenes y persistencia

| Ruta Host (local)                 | Ruta Contenedor             | Servicio     | Propósito                                |
|-----------------------------------|-----------------------------|--------------|------------------------------------------|
| `~/OdooDev/volumesOdoo/addons`    | `/mnt/extra-addons`         | `odoo`       | Módulos personalizados                   |
| `~/OdooDev/volumesOdoo/filestore` | `/var/lib/odoo/filestore`   | `odoo`       | Archivos adjuntos (PDFs, imágenes, etc.) |
| `~/OdooDev/dataPG`                | `/var/lib/postgresql/data`  | `postgres`   | Datos persistentes de la base de datos   |



## Archivos relacionados

- [compose.yml](./compose.yml)


## Notas adicionales

- Eliminar el volumen `~/OdooDev/dataPG` borra toda la base de datos y la deja limpia.
