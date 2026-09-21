# Servidor Minecraft (PaperMC)

## Resumen

Este stack despliega un servidor dedicado de **Minecraft: Java Edition** utilizando la imagen comunitaria optimizada `itzg/minecraft-server`. Está configurado para ejecutarse sobre **Paper**, una bifurcación (*fork*) de alto rendimiento de Spigot/CraftBukkit que mejora drásticamente los tiempos de respuesta del servidor (TPS), optimiza la gestión de entidades y reduce el consumo general de recursos.

El contenedor gestiona automáticamente la descarga de la versión especificada del servidor, acepta los términos de uso (EULA) y garantiza la **persistencia completa de los mundos, configuraciones y plugins** mediante un montaje local (*bind mount*).

| Servicio | Imagen | Versión | Puertos | Volúmenes | Red por defecto |
| -------- | ------ | ------- | ------- | --------- | --------------- |
| mc | itzg/minecraft-server:latest | latest | 25565:25565 | `./data:/data` | default |

## Servicios definidos

- **mc** → servidor de juegos dedicado de Minecraft con soporte para consola interactiva, plugins y administración remota (RCON).

## Puertos expuestos

- `25565` → puerto estándar del servidor Minecraft (TCP/UDP) para la conexión directa de los jugadores desde el cliente Java.

## Variables de entorno y configuración inicial

El contenedor se inicializa y configura a través de las siguientes variables de entorno:

| Variable | Valor | Descripción |
| -------- | ----- | ----------- |
| `EULA` | `TRUE` | Aceptación obligatoria del Acuerdo de Licencia de Usuario Final de Mojang. |
| `TYPE` | `PAPER` | Motor del servidor a utilizar; optimizado para rendimiento y compatibilidad con plugins Spigot/Paper. |
| `VERSION` | `26.2` | Versión específica del juego a descargar (puede indicarse también `LATEST`). |
| `MEMORY` | `4G` | Memoria RAM máxima asignada a la máquina virtual de Java (JVM). |
| `ONLINE_MODE` | `FALSE` | Permite el acceso a jugadores sin comprobación estricta de cuenta de Microsoft/Mojang (*offline/no-premium*). |
| `ENABLE_RCON` | `true` | Habilita el protocolo RCON para administración remota por línea de comandos. |
| `RCON_PASSWORD` | `TuPasswordSeguro` | Contraseña para conectarse y autenticarse contra la consola RCON. |

> **Seguridad:** Se recomienda encarecidamente cambiar `TuPasswordSeguro` por una contraseña robusta antes de levantar el contenedor en entornos accesibles públicamente.

## Volúmenes y persistencia

| Volumen / Ruta | Tipo | Servicio | Propósito |
| -------------- | ---- | -------- | --------- |
| `./data:/data` | Bind Mount | `mc` | Contiene los mundos (`world`, `world_nether`, `world_the_end`), configuraciones (`server.properties`), logs y la carpeta de `plugins`. |

## Archivos relacionados

- [compose.yml](./compose.yml) → definición del servicio, asignación de puertos y variables de entorno del servidor.
- `./data/` → directorio local en el host donde reside toda la configuración persistente del juego y los mundos.
- `./data/server.properties` → archivo generado tras el primer arranque con la configuración avanzada del juego (dificultad, PvP, render distance, etc.).
- `./data/plugins/` → carpeta donde se deben colocar los archivos `.jar` de los plugins adicionales.

## Notas adicionales

- **Acceso a la consola del servidor**: Gracias a las directivas `tty: true` y `stdin_open: true`, es posible conectarse a la consola interactiva de Minecraft en cualquier momento con:
  ```bash
  docker attach mc-server
  ```
  *(Para salir de la consola sin detener el servidor, presiona la combinación de teclas `Ctrl + P` seguida de `Ctrl + Q`).*
- **Instalación de plugins**: Para añadir complementos compatibles con Paper, copia los archivos `.jar` dentro de la carpeta local `./data/plugins/` y reinicia el contenedor con `docker compose restart mc`.
- **Puerto RCON**: Aunque RCON está habilitado internamente, su puerto por defecto (`25575`) no está expuesto en el bloque `ports` del host. Si requieres conectar herramientas externas de gestión RCON desde fuera del contenedor, deberás mapear el puerto `- "25575:25575"` en el `compose.yml`.
- **Rendimiento**: La asignación de memoria está establecida en 4 GB (`MEMORY: 4G`), lo cual es adecuado para partidas multijugador con grupos pequeños o medianos y una lista moderada de plugins.