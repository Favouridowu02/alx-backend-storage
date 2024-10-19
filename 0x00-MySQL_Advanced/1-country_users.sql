-- An SQL script that creates atable users with id, string, name and country tables
-- Arguments include: id: int, email: string(255), name: (255), country: (Enumeration)

CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country ENUM('US', 'CO', 'TN') DEFAULT 'US');
