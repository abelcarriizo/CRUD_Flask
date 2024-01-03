# CRUD_Flask

## Descripción del Proyecto

CRUD_Flask es una aplicación web desarrollada en Flask que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en una base de datos llamada MariaDB. La aplicación sigue una estructura organizativa para facilitar su comprensión y mantenimiento.

## Estructura del Repositorio

- **/.venv**: Contiene el entorno virtual de Python. Este directorio se creará al instalar las dependencias del proyecto.

- **/models**: Almacena los modelos de datos de la aplicación.

- **/routes**: Contiene los archivos de rutas que definen las URL y las funciones asociadas.

- **/templates**: Contiene las plantillas HTML utilizadas para renderizar las vistas en la aplicación.

- **/utils**: Incluye utilidades y funciones auxiliares utilizadas en el proyecto.

- **.env**: Archivo que contiene las variables de entorno necesarias para la configuración de la aplicación. Este archivo se generará al instalar el programa.

- **.gitignore**: Lista de archivos y directorios que se deben ignorar al realizar operaciones con Git.

- **app.py**: Archivo principal que configura y ejecuta la aplicación Flask.

- **boot.sh**: Script para ejecutar la aplicación. Asegúrate de dar permisos de ejecución a este script antes de su uso.

- **env_config.py**: Configuración de las variables de entorno utilizadas por la aplicación.

- **index.py**: Punto de entrada principal para ejecutar la aplicación.

- **install.sh**: Script para instalar las dependencias necesarias para la ejecución del programa. Asegúrate de dar permisos de ejecución a este script antes de su uso.

- **requirements.txt**: Contiene la lista de paquetes y versiones necesarios para el funcionamiento del programa.

```plaintext
IMPORTANTE.

Antes de continuar es necesario que tomes en cuenta estos puntos:

- Asegúrate de tener instalada la librería venv de Python ejecutando el siguiente comando:
sudo apt install python3.10-venv

- Se asume que MariaDB esta instalado.
```

### Paso Previo: Creación de la Base de Datos MariaDB

Antes de clonar el repositorio, asegúrate de crear la base de datos en MariaDB.

```sql
CREATE DATABASE nombre_de_la_base_de_datos;
```

### Pasos para la Ejecución:

1. **Clona el repositorio:**

```bash
git clone https://github.com/abelcarriizo/CRUD_Flask.git
cd CRUD_Flask
```

*Nota: Asegúrate de dar permisos de ejecución a los scripts `install.sh` y `boot.sh`:*

```bash
chmod +x install.sh boot.sh
```

2. **Instala las dependencias y configura el entorno virtual:**

```bash
./install.sh
```

*Después de ejecutar `install.sh`, se te pedirá proporcionar la información necesaria para configurar las variables de entorno en el archivo `.env`. Completa los siguientes campos cuando se te solicite:*

- **USER:** (Tu nombre de usuario para la base de datos)
- **PASSWORD:** (Tu contraseña para la base de datos)
- **HOST:** (El host donde se encuentra la base de datos, generalmente localhost)
- **DATABASE:** (El nombre de la base de datos creada anteriormente)

*Estos valores son necesarios para la correcta ejecución de la aplicación.*

3. **Ejecuta la aplicación:**

```bash
./boot.sh
```

La aplicación estará disponible en [http://localhost:5000](http://localhost:5000).

*¡Disfruta de CRUD_Flask!*
