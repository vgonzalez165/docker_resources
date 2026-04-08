# Usamos Eclipse Temurin 21 sobre Ubuntu (Jammy). 
# Es el estándar actual de Java y 100% compatible con VS Code.
FROM eclipse-temurin:21-jdk-jammy

# Evitamos preguntas durante la instalación
ENV DEBIAN_FRONTEND=noninteractive

# 1. Instalar herramientas básicas y cliente MySQL
RUN apt-get update && apt-get install -y \
    default-mysql-client \
    git \
    nano \
    openssh-client \
    locales \
    && rm -rf /var/lib/apt/lists/*

# 2. Configuración de Idioma (CRÍTICO para lectores de pantalla)
# Generamos español para que los acentos y la 'ñ' no salgan como símbolos raros
RUN locale-gen es_ES.UTF-8
ENV LANG es_ES.UTF-8
ENV LANGUAGE es_ES:en
ENV LC_ALL es_ES.UTF-8

# 3. Limpieza del Prompt (CRÍTICO para el alumno)
# Cambiamos el prompt largo por un simple "> "
RUN echo 'export PS1="> "' >> /root/.bashrc && \
    echo 'export PS1="> "' >> /etc/bash.bashrc

# 4. Directorio de trabajo
WORKDIR /app