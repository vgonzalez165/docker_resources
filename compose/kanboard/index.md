# Kanboard

## Resumen

**Kanboard** es una herramienta de gestión de proyectos de código abierto basada en la metodología visual **Kanban**. Se centra en la simplicidad, el minimalismo y la eficiencia, permitiendo organizar tareas en tableros visuales, gestionar flujos de trabajo, asignar responsables y monitorizar el progreso en tiempo real sin sobrecarga técnica.

Este stack levanta una instancia funcional de Kanboard utilizando su configuración predeterminada con base de datos embebida (**SQLite**).

| Servicio | Imagen                   | Versión | Puertos | Volúmenes                                           | Red por defecto |
| -------- | ------------------------ | ------- | ------- | --------------------------------------------------- | --------------- |
| kanboard | kanboard/kanboard:latest | latest  | 8080:80 | `kanboard-data`, `kanboard-plugins`, `kanboard-ssl` | default         |


## Servicios definidos

- **kanboard** → servidor de aplicaciones que aloja la plataforma Kanboard, con interfaz web accesible a través del puerto HTTP `80`.


## Puertos expuestos

- `8080` → acceso a la interfaz web de Kanboard desde el host (mapeado al puerto interno `80`).


## Credenciales y acceso inicial

A diferencia de otros servicios, esta configuración inicial no requiere variables de entorno obligatorias para arrancar, ya que Kanboard inicializa de forma automática su base de datos SQLite con credenciales por defecto:

| Parámetro              | Valor por defecto       | Descripción                                      |
| ---------------------- | ----------------------- | ------------------------------------------------ |
| **Usuario inicial**    | `admin`                 | Nombre de usuario del administrador por defecto. |
| **Contraseña inicial** | `admin`                 | Clave de acceso predeterminada.                  |
| **Ruta de acceso web** | `http://localhost:8080` | URL local de inicio de sesión.                   |


Por motivos de seguridad, es fundamental **cambiar la contraseña** del usuario `admin` inmediatamente tras el primer inicio de sesión desde el apartado de configuración de usuario.


## Volúmenes y persistencia

| Volumen / Ruta     | Tipo          | Servicio   | Propósito                                                                                |
| ------------------ | ------------- | ---------- | ---------------------------------------------------------------------------------------- |
| `kanboard-data`    | Docker Volume | `kanboard` | Almacena la base de datos SQLite (`db.sqlite`), archivos adjuntos y subidas de usuarios. |
| `kanboard-plugins` | Docker Volume | `kanboard` | Mantiene instalados y persistentes los complementos y extensiones de la comunidad.       |
| `kanboard-ssl`     | Docker Volume | `kanboard` | Contenedor para certificados y claves SSL/TLS en caso de configurar HTTPS interno.       |



## Archivos relacionados

- [compose.yml](./compose.yml) → definición del stack de servicios y volúmenes de Docker.


## Notas adicionales

- **Base de datos por defecto**: el contenedor utiliza SQLite alojado en el volumen persistente `kanboard-data`. No requiere un contenedor de base de datos externo (como MariaDB o PostgreSQL) para funcionar.
- **Acceso web**: se puede acceder a la aplicación desde cualquier navegador web visitando `http://localhost:8080` o sustituyendo `localhost` por la dirección IP del servidor.
- **Gestión de plugins**: los complementos descargados directamente desde el directorio de extensiones de la interfaz gráfica se guardan en el volumen `kanboard-plugins`, por lo que no se perderán al recrear el contenedor.
- **Reinicio automático**: el contenedor está configurado con la política `restart: unless-stopped`, por lo que se reactivará automáticamente si el demonio de Docker se reinicia.