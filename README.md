## 🔐 Login App – Eksamensprosjekt
En enkel innloggings- og registreringsapplikasjon laget i Python med Flask, koblet til en MariaDB-database. Applikasjonen kjører på en Raspberry Pi og gir brukere mulighet til å registrere seg og logge inn.

## 🧰 Krav
Raspberry Pi med Raspbian installert

SSH-tilgang til Pi-en

MariaDB

Python 3

## Flask og flask-mysqldb

## 🛠️ Installering
## 📡 Fra din egen maskin – Koble til Raspberry Pi via SSH
Finn IP-adressen til Pi-en.

Koble til via SSH:
ssh navn@ ip adressen til pi


mariadb -u navn -p

sql kommandoer du må skrive inn for at databasen skal fungere:

CREATE DATABASE users_db;
USE users_db;

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50),
  password VARCHAR(50)
);

INSERT INTO users (username, password) VALUES ('admin', '1234');

CREATE USER 'jonas'@'localhost' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON users_db.* TO 'app_user'@'10.2.2.55' IDENTIFIED BY '1234';
FLUSH PRIVILEGES;


## 🧠 Nyttige kommandoer i MariaDB
Vis alle databaser:
SHOW DATABASES;

Bruk en spesifikk database:
USE users_db;


Vis registrerte brukere:
SELECT * FROM users;

Slett alle brukere:
DELETE FROM users;



## 📑 Lover og regler

Jeg følger personopplysningsloven (GDPR) når jeg lager denne appen. Det betyr at jeg passer på at brukernes data, som brukernavn og passord, behandles trygt og ikke deles med andre. Jeg anbefaler å lagre passord på en sikker måte, for eksempel ved å bruke kryptering eller hashing, slik at ingen kan lese dem direkte.

Når du bruker appen min, godtar du at informasjonen du legger inn blir lagret i databasen.

Appen min er laget med åpen kildekode-verktøy som Flask, mysql-connector-python og mysqlclient.
