sqlmap
Build Status Python 2.6|2.7|3.x License PyPI version GitHub closed issues Twitter

sqlmap é uma ferramenta de teste de intrusão, de código aberto, que automatiza o processo de detecção e exploração de falhas de injeção SQL. Com essa ferramenta é possível assumir total controle de servidores de banco de dados em páginas web vulneráveis, inclusive de base de dados fora do sistema invadido. Ele possui um motor de detecção poderoso, empregando as últimas e mais devastadoras técnicas de teste de intrusão por SQL Injection, que permite acessar a base de dados, o sistema de arquivos subjacente e executar comandos no sistema operacional.

Imagens
Imagem

Você pode visitar a coleção de imagens que demonstra alguns dos recursos apresentados na wiki.

Instalação
Você pode baixar o arquivo tar mais recente clicando aqui ou o arquivo zip mais recente clicando aqui.

De preferência, você pode baixar o sqlmap clonando o repositório Git:

git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev
sqlmap funciona em Python nas versões 2.6, 2.7 e 3.x em todas as plataformas.

Como usar
Para obter uma lista das opções básicas faça:

python sqlmap.py -h
Para obter a lista completa de opções faça:

python sqlmap.py -hh
Você pode encontrar alguns exemplos aqui. Para ter uma visão geral dos recursos do sqlmap, lista de recursos suportados e a descrição de todas as opções, juntamente com exemplos, aconselhamos que você consulte o manual do usuário.

Links
Homepage: http://sqlmap.org
Download: .tar.gz ou .zip
Commits RSS feed: https://github.com/sqlmapproject/sqlmap/commits/master.atom
Issue tracker: https://github.com/sqlmapproject/sqlmap/issues
Manual do Usuário: https://github.com/sqlmapproject/sqlmap/wiki
Perguntas frequentes (FAQ): https://github.com/sqlmapproject/sqlmap/wiki/FAQ
Twitter: @sqlmap
Demonstrações: #1 e #2
Imagens: https://github.com/sqlmapproject/sqlmap/wiki/Screenshots
