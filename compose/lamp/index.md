# Apache + PHP + MySQL + phpMyAdmin

## Resumen

Este stack proporciona un entorno clásico de desarrollo web con **Apache + PHP** como servidor de aplicaciones, **MySQL** como motor de base de datos relacional y **phpMyAdmin** como herramienta de administración gráfica.


| Servicio   | Imagen                                  | Versión | Puertos | Volúmenes                | Redes                            |
| ---------- | --------------------------------------- | ------- | ------- | ------------------------ | -------------------------------- |
| apache-php | elki97413/pdo\_mysql-php-apache\:latest | latest  | 80:80   | `./www:/var/www/html`    | shared-network, internal-network |
| db (MySQL) | mysql:8.0                               | 8.0     | —       | `db_data:/var/lib/mysql` | internal-network                 |
| phpmyadmin | phpmyadmin/phpmyadmin\:latest           | latest  | 8080:80 | —                        | internal-network                 |


## Servicios definidos

* **apache-php** → servidor Apache con soporte PHP.
* **db** → servidor MySQL 8.0, solo accesible desde la red interna.
* **phpmyadmin** → interfaz web para administrar la base de datos MySQL. 


## Puertos expuestos

- `80` → acceso a la aplicación web en Apache/PHP.
- `8080` → acceso a la interfaz de phpMyAdmin.


## Credenciales por defecto

### MySQL (`db`)

- **Usuario root**: `root`
- **Contraseña root**: `rootpass`
- **Base de datos inicial**: `testdb`
- **Usuario adicional**: `alumno` / `alumnopass`

### phpMyAdmin (`phpmyadmin`)

- Accede usando las credenciales anteriores contra el servidor `db`.


## 💾 Volúmenes y persistencia

| Ruta Host (local) | Ruta Contenedor  | Servicio     | Propósito                                 |
| ----------------- | ---------------- | ------------ | ----------------------------------------- |
| `./www`           | `/var/www/html`  | `apache-php` | Código fuente PHP del proyecto.           |
| `db_data`         | `/var/lib/mysql` | `db`         | Almacén de datos de MySQL (persistencia). |


## Archivos relacionados

- [docker-compose.yml](./docker-compose.yml)


## Notas adicionales

- La base de datos MySQL **no expone puertos al host**. Solo se accede mediante `phpmyadmin` o desde `apache-php`.
- El proyecto PHP se debe montar en `./www` conectando hacia MySQL usando el host `db`
- Sse ha utilizado la imagen `elki97413/pdo\_mysql-php-apache` ya que la imagen oficial no incluye por defecto PDO ni mysqli
