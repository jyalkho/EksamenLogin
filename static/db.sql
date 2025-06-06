CREATE DATABASE users_db;
USE users_db;
CREATE TABLE users ( id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(50),password VARCHAR(50),mobile VARCHAR(15) );
INSERT INTO users (username, password, mobile) VALUES ('admin', '1234');
CREATE USER 'jonas'@'localhost' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON users_db.* TO 'app_user'@'10.2.2.55' IDENTIFIED BY '1234';
FLUSH PRIVILEGES;
