# Discord Bot - Python Tutorial

Este proyecto es un Bot de Discord personalizado construido con Python y la librería `discord.py`, siguiendo la arquitectura asíncrona moderna. Incluye gestión de eventos, comandos con prefijo y moderación básica.

## ⚡ Funcionalidades (Vistas en el Video)

El bot incluye las siguientes capacidades demostradas en el tutorial:

* **Eventos Automáticos:**
    * **Bienvenida:** Envía un mensaje directo (DM) automático ("Welcome to the server") cuando un nuevo miembro se une.
    * **Filtro de Groserías:** Detecta palabras prohibidas en el chat, borra el mensaje automáticamente y advierte al usuario.
    * **Log de Inicio:** Confirma en la terminal cuando el bot está listo y conectado (`on_ready`).

* **Comandos Disponibles (Prefijo: `!`):**
    * `!hello`: El bot saluda y menciona al usuario.
    * `!assign`: Asigna un rol específico (ej. "gamer") al usuario (requiere configuración de jerarquía de roles).
    * `!remove`: Elimina el rol específico del usuario.
    * `!secret`: Comando protegido que solo funciona si el usuario tiene el rol requerido; de lo contrario, muestra un error de permisos.
    * `!dm [mensaje]`: El bot te envía un mensaje privado con el texto que escribas.
    * `!reply [mensaje]`: El bot responde directamente a tu mensaje original en el chat.
      

## 🛠️ Instalación y Configuración

Basado en el entorno de desarrollo mostrado (PyCharm/VS Code):

1.  **Clonar el repositorio y crear carpeta del proyecto.**
2.  **Archivos requeridos:**
    * `main.py`: Código principal.
    * `.env`: Para guardar el token de forma segura.
    * `requirements.txt`: Dependencias del proyecto.

3.  **Instalar dependencias:**
    Ejecuta en la terminal:
    ```bash
    pip install -r requirements.txt
    ```
    *Contenido de requirements.txt:*
    ```text
    discord.py
    python-dotenv
    ```

4.  **Configuración de Variables de Entorno:**
    Crea un archivo llamado `.env` en la raíz y agrega tu token (obtenido del Portal de Desarrolladores de Discord):
    ```env
    DISCORD_TOKEN=tu_token_aqui
    ```

## ⚙️ Permisos Necesarios (Discord Developer Portal)

Para que el bot funcione como en el video, debes habilitar los **Privileged Gateway Intents** en el portal de desarrolladores:

* [x] **Message Content Intent** (Para leer comandos y filtrar groserías).
* [x] **Server Members Intent** (Para dar la bienvenida a nuevos miembros).

Al invitar el bot, asegúrate de marcar los permisos de OAuth2: *Send Messages, Manage Roles, Manage Messages, Embed Links, Add Reactions*.

## 🚀 Despliegue

El proyecto está listo para mantenerse activo 24/7 utilizando servicios en la nube como **Render**, subiendo el script de Python para ejecución continua.

