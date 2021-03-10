# Blog

Dearrollo de un blog a través de Django, todo el proceso de desarrollo se está llevando acabo durante los directos de este [canal](https://www.twitch.tv/pylord_) 

### Como instalar 

Para instalar el código en tu máquina local realiza los siguientes pasos:

1. clona el repositorio en tu directorio de preferencia `git clone https://github.com/MarcosLopez7/blog.git` 
2. Asegurate de tener python en la versión 3.8
3. Si estás en linux, probablemente necesites instalar este paquete `python3-venv`
4. Ingresa al directorio del repositorio `cd blog`
5. Inicializa el entorno de python `python -m venv .`
6. Activa el entorno de python en Linux o mac corre: `source bin/activate` en Windows: `Scripts\activate.bat`
7. Instala las dependencias en requirements.txt `pip install -r requirements.txt` 
8. Ingresa al directorio principal del proyecto `cd blog`
9. Crea la base de datos de SQLite a través de las migraciones con el siguiente comando `python manage.py migrate`
10. Si todo saliò bien, corre el servidor de desarrollo de Django con `python manage.py runserver`, accede al navegador con localhost:8000 y deberìas ver la app corriendo sin problema :)

### Variables de entorno

En los commits más recientes, se implementaron variables de entorno que son usadas para ocultar strings que contienen contraseñas o llaves de acceso a API's externos con el fin de que no se expongan en el repositorio en texto plano y mantener segura nuestra app.

Para exportar una variable de entorno y que ésta sea usada en la aplicación corre el siguiente comando en la misma terminal donde corres `python manage.py runserver`:

- Para linux o MacOS: `export MI_VARIABLE_DE_ENTORNO='valor de mi variable'`
- Para Windows: `setx MI_VARIABLE_DE_ENTORNO "valor de mi variable"`

Luego cuando quieras usar la viable dentro del código:

- Importas la biblioteca de os `import os`
- Usa el método os.getenv() para obtener el valor de la variable `MI_VARIABLE_DE_PYTHON = os.getenv('MI_VARIABLE_DE_ENTORNO')`

###### Nota

Probablemente tengas que exportar las variables cada vez que inicies una nueva terminal, para que estás variables queden guardadas para todas las nuevas terminales que se inicialicen, en linux o MacOS puedes agregar los comandos para exportar las variables dentro de `~/.bashrc`. El siguiente link es una explicación de como funciona el archivo [~/.bashrc](https://www.zeppelinux.es/descripcion-y-uso-de-los-archivos-bashrc-y-etc-bashrc/) 

Para que en windows queden guardadas las variables a nivel sistema necesitas cambiarlos desde propiedades del sistema, el siguiente link es para ver [como modificar las variables desde ahí](https://www.architectryan.com/2018/08/31/how-to-change-environment-variables-on-windows-10/)

#### Guardar las variables dentro de un archivo .env o .bat

En caso que sean demasiadas variables de entorno que necesitas exportar, puedes guardar todas juntas dentro un archivo de bash (o un bat en Windows), cada línea en este archivo ejecuta el comando export con la variable que quieres exportar, el archivo para Linux o MacOS se vería de esta forma:

    export MI_VARIABLE_DE_ENTORNO_1='valor de mi variable 1'
    export MI_VARIABLE_DE_ENTORNO_2='valor de mi variable 2'
    export MI_VARIABLE_DE_ENTORNO_3='valor de mi variable 3'
    ...
    
En Windows se vería así:

    setx MI_VARIABLE_DE_ENTORNO_1 "valor de mi variable 1"
    setx MI_VARIABLE_DE_ENTORNO_2 "valor de mi variable 2"
    setx MI_VARIABLE_DE_ENTORNO_3 "valor de mi variable 3"
    ...

El archivo lo agregas dentro el directorio raíz del repositorio como `nombre_de_mi_archivo.env` o `nombre_de_mi_archivo.bat` (no lo agregues en otro lugar al menos que modifiques el archivo .gitignore para que no se suba el archivo al repositorio, tampoco uses una extensión diferente a `.env` o `.bat` al menos que el archivo .gitignore sea también modificado) 

Para activar el archivo .env abre en la misma terminal donde se ejecuta `python manage.py runserver` ejecuta el comando `source nombre_de_mi_archivo.env`

En windows para el archivo .bat en la misma terminal donde se ejecuta `python manage.py runserver` ejecuta el comando `.\nombre_de_mi_archivo.bat`

### Crea un superusario para el admin

Para usar el admin crea tu super usuario con el comando `python manage.py createsuperuser` llena los datos que te piden y accede al sitio del admin desde localhost:8000/admin
