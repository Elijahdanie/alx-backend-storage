-- Resets the valid_email column of table users
-- On Updateß

DELIMITER //
CREATE TRIGGER reset
BEFORE UPDATE
ON users
FOR EACH ROW
BEGIN
	IF NEW.email != OLD.email THEN
	SET NEW.valid_email = 0;
END IF;
END; //
