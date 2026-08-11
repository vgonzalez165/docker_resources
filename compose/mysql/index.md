# MySQL + phpMyAdmin

## Resumen

MySQL es una base de datos **relacional SQL** ampliamente utilizada en aplicaciones web, que almacena los datos en tablas y permite consultas complejas mediante SQL.

phpMyAdmin es una interfaz web que proporciona un acceso gráfico para administrar MySQL desde el navegador, sin necesidad de usar el cliente de consola. Permite ejecutar consultas SQL, crear tablas, gestionar usuarios y ver el contenido de la base de datos.

Este stack combina ambos servicios: la base de datos MySQL y la interfaz de administración phpMyAdmin.

| Servicio   | Imagen                       | Versión | Puertos   | Volúmenes                | Red            |
| ---------- | ---------------------------- | ------- | --------- | ------------------------ | -------------- |
| mysql      | mysql:8.0                    | 8.0     | 3306:3306 | `db_data:/var/lib/mysql` | shared-network |
| phpmyadmin | phpmyadmin/phpmyadmin:latest | latest  | 8000:80   | —                        | shared-network |

## Servicios definidos

- **mysql** → motor de base de datos relacional SQL.
- **phpmyadmin** → interfaz web para administrar MySQL.

## Puertos expuestos

- `3306` → puerto estándar de MySQL.
- `8000` → interfaz web de phpMyAdmin accesible desde el navegador.

## Credenciales por defecto

### MySQL

- **Usuario root:** `root`
- **Contraseña root:** `rootpass`
- **Base de datos creada al iniciar:** `testdb`
- **Usuario adicional:** `alumno`
- **Contraseña usuario alumno:** `alumnopass`

> Nota: todos estos valores están definidos en variables de entorno del compose.

### phpMyAdmin

Conecta automáticamente al servicio `mysql` usando el usuario root:

- **Usuario DB:** `root`
- **Contraseña DB:** `rootpass`

## Volúmenes y persistencia

| Ruta Host (local) | Ruta Contenedor  | Servicio | Propósito                                                                |
| ----------------- | ---------------- | -------- | ------------------------------------------------------------------------ |
| `db_data`         | `/var/lib/mysql` | `mysql`  | Almacenamiento de los datos para persistir aunque el contenedor se borre |

## Archivos relacionados

- [compose.yml](./compose.yml)

## Notas adicionales

- La red `shared-network` está marcada como **externa**, por lo que debe existir previamente:

  ```bash
  docker network create shared-network
  ```

- Es recomendable **no usar** estas contraseñas en entornos de producción.

- Para acceder a phpMyAdmin:
  → [http://localhost:8000](http://localhost:8000)


