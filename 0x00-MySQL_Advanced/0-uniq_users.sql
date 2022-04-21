--script creates users with
--id, email and name
CREATE TABLE if NOT EXISTS `users` (
       `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
       `email` VARCHAR(255) NOT NULL UNIQUE,
       `name`  VARCHAR(255)
);
