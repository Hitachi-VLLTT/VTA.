sqlmap
Build Status Python 2.6|2.7|3.x License PyPI version GitHub closed issues Twitter

sqlmap es una herramienta para pruebas de penetración "penetration testing" de software libre que automatiza el proceso de detección y explotación de fallos mediante inyección de SQL además de tomar el control de servidores de bases de datos. Contiene un poderoso motor de detección, así como muchas de las funcionalidades escenciales para el "pentester" y una amplia gama de opciones desde la recopilación de información para identificar el objetivo conocido como "fingerprinting" mediante la extracción de información de la base de datos, hasta el acceso al sistema de archivos subyacente para ejecutar comandos en el sistema operativo a través de conexiones alternativas conocidas como "Out-of-band".

Capturas de Pantalla
Screenshot

Visita la colección de capturas de pantalla que demuestra algunas de las características en la documentación(wiki).

Instalación
Se puede descargar el "tarball" más actual haciendo clic aquí o el "zipball" aquí.

Preferentemente, se puede descargar sqlmap clonando el repositorio Git:

git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev
sqlmap funciona con las siguientes versiones de Python 2.6, 2.7 y 3.x en cualquier plataforma.

Uso
Para obtener una lista de opciones básicas:

python sqlmap.py -h
Para obtener una lista de todas las opciones:

python sqlmap.py -hh
Se puede encontrar una muestra de su funcionamiento aquí. Para obtener una visión general de las capacidades de sqlmap, así como un listado funciones soportadas y descripción de todas las opciones y modificadores, junto con ejemplos, se recomienda consultar el manual de usuario.

Enlaces
Página principal: http://sqlmap.org
Descargar: . tar.gz o .zip
Fuente de Cambios "Commit RSS feed": https://github.com/sqlmapproject/sqlmap/commits/master.atom
Seguimiento de problemas "Issue tracker": https://github.com/sqlmapproject/sqlmap/issues
Manual de usuario: https://github.com/sqlmapproject/sqlmap/wiki
Preguntas frecuentes (FAQ): https://github.com/sqlmapproject/sqlmap/wiki/FAQ
Twitter: @sqlmap
Demostraciones: http://www.youtube.com/user/inquisb/videos
Imágenes: https://github.com/sqlmapproject/sqlmap/wiki/Screenshots
