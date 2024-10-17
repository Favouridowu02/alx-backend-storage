-- An SQL script that creates a table users 
-- id: interger, not nullable p_key, email: string(255), name: string(255)
CREATE TABLE IF NOT EXISTS users (id int NOT NULL PRIMARY KEY AUTO_INCREMENT, email varchar(255) NOT NULL UNIQUE, name varchar(255));
