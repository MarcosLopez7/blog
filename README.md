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
8. Exporta una variable de entorno con nombre `DJANGO_SECRET_KEY`, el valor de está variable debe ser semejante a una contraseña fuerte, ejemplo `6azuu$i$mk%-i92g*thfo#@j+u&(3hnl%a+68ov+lp6vifbw-j` (no uses este valor), puedes utilizar un generador de contraseñas aleatoreos para generar un valor semejante, para exportar la variable en Linux o MacOS usa el comando `export DJANGO_SECRET_KEY='valor para esta variable'` en Windows `setx DJANGO_SECRET_KEY "valor para esta variable"`, para más información sobre las variables de entorno checa [la sección adentro de este README](https://github.com/MarcosLopez7/blog#variables-de-entorno)
9. Ingresa al directorio principal del proyecto `cd blog`
10. Crea la base de datos de SQLite a través de las migraciones con el siguiente comando `python manage.py migrate`
11. Si todo salió bien, corre el servidor de desarrollo de Django con `python manage.py runserver`, accede al navegador con localhost:8000 y deberìas ver la app corriendo sin problema :)

Para la funcionalidad completa de la aplicación se necesita configurar el envío automático de correo electrónico, puedes revisar esta [sección para más información](https://github.com/MarcosLopez7/blog#configuraci%C3%B3n-del-envi%C3%B3-autom%C3%A1tico-de-correo-electr%C3%B3nico)  

### Crea un superusario para el admin

Para usar el admin crea tu super usuario con el comando `python manage.py createsuperuser` llena los datos que te piden y accede al sitio del admin desde localhost:8000/admin

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

### Configuración del envió automático de correo electrónico

Para activar la total funcionalidad de la aplicación hay que configurar algunos settings necesarios. Por defecto los settings para el correo están de la siguiente manera

    # Email Settings
    SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.sendgrid.net'
    EMAIL_HOST_USER = 'apikey' # this is exactly the value 'apikey'
    EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_SENDER = 'pylord_@tutanota.com'

La configuración anterior está para conectarse con el servicio de [SendGrid](https://sendgrid.com/), para usar está configuración, debes crear una cuenta en este servicio (la cuenta puede ser gratuita), a través de esta cuenta debes generar una API key donde también puedas incluir la dirección de correo electrónico que deseas usar como dirección de origen para todos los correos que se envíen 

Una vez generada el API key debes exportar una variable de entorno con el nombre de SENDGRID_API_KEY con el valor del API key generado por sendgrid, consulta la sección de [variables de entorno](https://github.com/MarcosLopez7/blog#variables-de-entorno) para más informaicón

###### nota

Si quieres usar otro servicio aparte de SendGrid como gmail, mailgun, etc. Puedes hacerlo pero la configuración de estos servicios en el código están fuera de alcance de está documentación
