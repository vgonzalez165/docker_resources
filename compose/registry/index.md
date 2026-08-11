# Docker Registry + UI

## Resumen

El **Docker Registry** es un servicio que permite almacenar, distribuir y gestionar imágenes de contenedores en un repositorio privado, funcionando como alternativa local a Docker Hub.

Esta configuración incluye además una interfaz web (**Registry UI**) para visualizar y administrar las imágenes de forma más sencilla.

Este entorno es útil para disponer de un registro privado en equipos de desarrollo, en redes locales o en entornos de producción controlados.


| Servicio      | Imagen                           | Versión | Puertos   | Volúmenes                                                                                | Red            |
| ------------- | -------------------------------- | ------- | --------- | ---------------------------------------------------------------------------------------- | -------------- |
| `registry`    | registry:2                       | 2       | 5000:5000 | `registry-data:/var/lib/registry` <br> `./config.yml:/etc/docker/registry/config.yml:ro` | shared-network |
| `registry-ui` | joxit/docker-registry-ui\:latest | latest  | 8085:80   | —                                                                                        | shared-network |

## Servicios definidos

- **registry** → servicio principal que almacena y distribuye imágenes Docker.
- **registry-ui** → interfaz gráfica para gestionar el registro privado de manera visual (ver repositorios, tags, eliminar imágenes, etc.).


## Puertos expuestos

- `5000` → puerto donde se expone el **registro privado** (push/pull de imágenes).
- `8085` → puerto para acceder a la **interfaz web** del registro desde un navegador.


## Credenciales por defecto

- En esta configuración **no hay autenticación habilitada**.
- Para entornos reales se recomienda configurar autenticación con `htpasswd` y/o TLS.


## Volúmenes y persistencia

| Ruta Host (local) | Ruta Contenedor                      | Servicio   | Propósito                                                                |
| ----------------- | ------------------------------------ | ---------- | ------------------------------------------------------------------------ |
| `registry-data`   | `/var/lib/registry`                  | `registry` | Almacena las imágenes del registro de forma persistente.                 |
| `./config.yml`    | `/etc/docker/registry/config.yml:ro` | `registry` | Configuración personalizada del servicio Registry (auth, storage, etc.). |


## Archivos relacionados

- [docker-compose.yml](./docker-compose.yml)
- [config.yml](./config.yml) → configuración avanzada del registro (opcional).


## Notas adicionales

- El registro **se conecta a la red externa `shared-network`**, lo que permite usarlo junto con otros servicios de Docker Compose o Swarm.
- La opción `REGISTRY_STORAGE_DELETE_ENABLED=true` habilita el borrado de imágenes, aunque requiere ejecutar `garbage-collect` para liberar espacio realmente.
- En producción se recomienda:
  - Usar **TLS** (certificados SSL).
  - Configurar **autenticación básica**.
  - Montar almacenamiento externo (S3, MinIO, etc.) en lugar de disco local.
- Se puede sobreescribir la configuración establecida en la creación del contenedor mediante el fichero `config.yml`. A continuación, se muestra un ejemplo de contenido de este fichero:

    ```yml
    version: 0.1
    log:
    level: info
    fields:
        service: registry

    storage:
    filesystem:
        rootdirectory: /var/lib/registry   # ruta donde se guardan las imágenes
    delete:
        enabled: true                      # permite borrar imágenes (con garbage-collect)

    http:
    addr: :5000
    headers:
        X-Content-Type-Options: [nosniff]

    # Configuración de TLS (si se quiere exponer con HTTPS directamente)
    # Para entornos productivos, mejor usar Nginx o Traefik como proxy inverso
    # tls:
    #   certificate: /certs/domain.crt
    #   key: /certs/domain.key

    # Autenticación básica con htpasswd
    auth:
    htpasswd:
        realm: basic-realm
        path: /auth/htpasswd

    # Opcional: caché de blobs (mejora el rendimiento)
    proxy:
    remoteurl: https://registry-1.docker.io

    # Notificaciones (webhooks) para CI/CD u otros sistemas
    notifications:
    endpoints:
        - name: local-logger
        url: http://127.0.0.1:5001/events
        timeout: 500ms
        threshold: 5
        backoff: 1s

    ```