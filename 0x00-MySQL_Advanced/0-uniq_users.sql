- script creates users with
- id, email and name

CREATE TABLE IF NOT EXISTS users(id INT NOT NULL PRIMARY KEY AUTO INCREMENT,
email VARCHAR(55) NOT NULL UNIQ, name VARCHAR(255));

