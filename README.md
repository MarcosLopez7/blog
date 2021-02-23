# blog

Repositorio de Blog que está desarrollandose en [stream](https://www.twitch.tv/pylord_) 

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

### Crea un superusario para el admin

Para usar el admin crea tu super usuario con el comando `python manage.py createsuperuser` llena los datos que te piden y accede al sitio del admin desde localhost:8000/admin