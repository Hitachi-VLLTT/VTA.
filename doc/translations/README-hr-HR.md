sqlmap
Build Status Python 2.6|2.7|3.x License PyPI version GitHub closed issues Twitter

sqlmap je alat namijenjen za penetracijsko testiranje koji automatizira proces detekcije i eksploatacije sigurnosnih propusta SQL injekcije te preuzimanje poslužitelja baze podataka. Dolazi s moćnim mehanizmom za detekciju, mnoštvom korisnih opcija za napredno penetracijsko testiranje te široki spektar opcija od onih za prepoznavanja baze podataka, preko dohvaćanja podataka iz baze, do pristupa zahvaćenom datotečnom sustavu i izvršavanja komandi na operacijskom sustavu korištenjem tzv. "out-of-band" veza.

Slike zaslona
Slika zaslona

Možete posjetiti kolekciju slika zaslona gdje se demonstriraju neke od značajki na wiki stranicama.

Instalacija
Možete preuzeti zadnji tarball klikom ovdje ili zadnji zipball klikom ovdje.

Po mogućnosti, možete preuzeti sqlmap kloniranjem Git repozitorija:

git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev
sqlmap radi bez posebnih zahtjeva korištenjem Python verzije 2.6, 2.7 i/ili 3.x na bilo kojoj platformi.

Korištenje
Kako biste dobili listu osnovnih opcija i prekidača koristite:

python sqlmap.py -h
Kako biste dobili listu svih opcija i prekidača koristite:

python sqlmap.py -hh
Možete pronaći primjer izvršavanja ovdje. Kako biste dobili pregled mogućnosti sqlmap-a, liste podržanih značajki te opis svih opcija i prekidača, zajedno s primjerima, preporučen je uvid u korisnički priručnik.

Poveznice
Početna stranica: http://sqlmap.org
Preuzimanje: .tar.gz ili .zip
RSS feed promjena u kodu: https://github.com/sqlmapproject/sqlmap/commits/master.atom
Prijava problema: https://github.com/sqlmapproject/sqlmap/issues
Korisnički priručnik: https://github.com/sqlmapproject/sqlmap/wiki
Najčešće postavljena pitanja (FAQ): https://github.com/sqlmapproject/sqlmap/wiki/FAQ
Twitter: @sqlmap
Demo: http://www.youtube.com/user/inquisb/videos
Slike zaslona: https://github.com/sqlmapproject/sqlmap/wiki/Screenshots
