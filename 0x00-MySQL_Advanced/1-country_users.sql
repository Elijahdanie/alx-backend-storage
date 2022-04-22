-- Creates a table users with id email name and country
CREATE TABLE users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country NOT NULL ENUM('US', 'CO', 'TN') DEFAULT 0
);
