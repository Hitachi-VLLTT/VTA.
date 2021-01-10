sqlmap
Build Status Python 2.6|2.7|3.x License PyPI version GitHub closed issues Twitter

sqlmap est un outil Open Source de test d'intrusion. Cet outil permet d'automatiser le processus de détection et d'exploitation des failles d'injection SQL afin de prendre le contrôle des serveurs de base de données. sqlmap dispose d'un puissant moteur de détection utilisant les techniques les plus récentes et les plus dévastatrices de tests d'intrusion comme L'Injection SQL, qui permet d'accéder à la base de données, au système de fichiers sous-jacent et permet aussi l'exécution des commandes sur le système d'exploitation.

Les Captures d'écran

Les captures d'écran disponible ici démontrent des fonctionnalités de sqlmap.

Installation
Vous pouvez télécharger le fichier "tarball" le plus récent en cliquant ici. Vous pouvez aussi télécharger l'archive zip la plus récente ici.

De préférence, télécharger sqlmap en le clonant:

git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev
sqlmap fonctionne sur n'importe quel système d'exploitation avec la version 2.6, 2.7 et 3.x de Python

Utilisation
Pour afficher une liste des fonctions de bases et des commutateurs (switches), tapez:

python sqlmap.py -h
Pour afficher une liste complète des options et des commutateurs (switches), tapez:

python sqlmap.py -hh
Vous pouvez regarder une vidéo ici pour plus d'exemples. Pour obtenir un aperçu des ressources de sqlmap, une liste des fonctionnalités prises en charge, la description de toutes les options, ainsi que des exemples, nous vous recommandons de consulter le wiki.

Liens
Page d'acceuil: http://sqlmap.org
Téléchargement: .tar.gz ou .zip
Commits RSS feed: https://github.com/sqlmapproject/sqlmap/commits/master.atom
Suivi des issues: https://github.com/sqlmapproject/sqlmap/issues
Manuel de l'utilisateur: https://github.com/sqlmapproject/sqlmap/wiki
Foire aux questions (FAQ): https://github.com/sqlmapproject/sqlmap/wiki/FAQ
Twitter: @sqlmap
Démonstrations: http://www.youtube.com/user/inquisb/videos
Les captures d'écran: https://github.com/sqlmapproject/sqlmap/wiki/Screenshots
