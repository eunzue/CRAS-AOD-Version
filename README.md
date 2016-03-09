CRAs de Aragón
==============

Esta es una aplicación web bifurcada de la desarrollada durante el **Jacathon 2014** organizado por [Aragón Open Data](http://opendata.aragon.es), que permite visualizar detalladamente los Colegios Rurales Agrupados (CRA) de Aragón. Esta versión hace uso del ecosistema de Aragón Open Data, por lo que la configuración y comandos de esta documentación vendran tan sólo para el entorno linux, más concretamente Ubuntu.

Los datos de los CRA han sido extraídos de <http://opendata.aragon.es/catalogo/tablas-resumen-centros-rurales-agrupados-por-municipios> y <http://opendata.aragon.es/catalogo/centros-rurales-agrupados-cra>.


### Información Técnica
Nuestra app es una aplicación web Python usando el framework [Flask](http://flask.pocoo.org/), y PostgreSQL como base de datos. En el ecosistema de Aragón Open Data hacemos uso del servidor web Apache2.

Para gestionar las depencias, usamos el gestor de dependencias `pip`, que puedes instalar en Linux con:

```
curl https://bootstrap.pypa.io/get-pip.py > get-pip.py
sudo python get-pip.py
```

Recomendamos aislar el entorno de desarrollo Python con `virtualenv`:

```
sudo pip install virtualenv
cd /path_de_app
virtualenv campusOpenData
```

En caso de duda consultar la documentación oficial de [pip](https://pip.readthedocs.org/en/latest/) y de [Virtualenv](https://virtualenv.readthedocs.org/en/latest/).


Antes de instalar las librerías Python requeridas, necesitas instalar PostgreSQL en tu sistema:

Ejemplo Ubuntu: `sudo apt-get install postgresql`

Ejemplo MacOSX, con [Homebrew](http://brew.sh/): `brew install postgresql`

Después, hay que crear e importar la base de datos a PostgreSQL (recuerda que si modificas el usuario y contraseña deberas de modificar el archivo dump de la base de datos):

```
sudo -u postgres psql postgres

CREATE user cras_aragon password 'C0ntr4$3n4';

ALTER ROLE cras_aragon WITH SUPERUSER;

CREATE DATABASE CRAs WITH OWNER cras_aragon;

GRANT ALL PRIVILEGES ON DATABASE CRAs TO cras_aragon;
\q

psql -h localhost -d cras -U cras_aragon -f /path_de_app/data/datos.sql


```
No olvides modificar el fichero `app/config.py` con tus datos de conexión a base de datos si los has modificado.

Creamos el entorno para con el que se instalaran las dependencias, en el directorio donde tenemos la app

`virtualenv crasaragon`

Para poder instalar la dependecia y manejar bases de datos de PostgreSQL se necesita instalar un software especifico:

```
sudo apt-get install libpq-dev
sudo apt-get install libevent-dev
sudo apt-get install build-essential autoconf libtool pkg-config python-opengl python-imaging python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev

```

Para instalar las dependencias de las librerías Python:

```
crasaragon/bin/pip install requisites/argparse-1.4.0.tar.gz
crasaragon/bin/pip install requisites/itsdangerous-0.24.tar.gz
crasaragon/bin/pip install requisites/MarkupSafe-0.23.tar.gz
crasaragon/bin/pip install requisites/Werkzeug-0.11.3.tar.gz
crasaragon/bin/pip install requisites/Jinja2-2.8.tar.gz
crasaragon/bin/pip install requisites/wsgiref-0.1.2.zip
crasaragon/bin/pip install requisites/Flask-0.10.1.tar.gz
crasaragon/bin/pip install requisites/psycopg2-2.6.1.tar.gz

```

###Configurar apache

Según el ecosistema de Aragón Open Data esta aplicación la tenemos en opendata.aragon.es/apps/cras. Debemos activar los siguientes modulos, para ello abrimos un terminal e introducimos:

```

sudo apt-get install apache2
sudo a2enmod proxy proxy_http

```

Modificamos el fichero de configuración de apache añadiendo:

```

ProxyPass /apps/cras http://localhost:50051 retry=0
ProxyPassReverse /apps/cras http://localhost:50051

```

Recordar que despues hay que reiniciar apache para que los cambios surjan efecto.

###Arrancar la aplicación

Arrancamos la aplicación con:

```

/path_de_app/crasaragon/bin/python /path_de_app/run.py &

```

Ojo que el run.py esta la aplicación para que arranque en modo debug, se recomienda quitarlo para entornos de producción.

####Cerrar la aplicación

Ejecutamos el siguiente comando para cerrar la app:

```

killall /path_de_app/crasaragon/bin/python

```

### Notas sobre los cambios de la versión original

* Se usa otro sistema gestor de base de datos. En lugar de MySQL se usa PostgreSQL, con lo que hay modificaciones por este motivo.

* Como se ha dicho con anterioridad la app no esta directamente en el dominio, con lo que se ha tenido que modificar el script main.js. Podemos observar buscando "$.getJSON" que el primer parametro es la url, vamos que tiene aquí (/apps/cras) parte de la url. Se tendrá que modificar esto si no queremos configurarlo como el entorno de Aragón Open Data.

* Los ficheros js y css se comprimen con una aplicación como Yui Compressor con lo que ganar espacio y poder servir la web lo antes posible. Al tener que servir documentos de menor tamaño. Se dejá una versión para desarroladores con la extensión .human.js, por si se realizan cambios en el futuro.
