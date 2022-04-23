-- Creates a function 'safeDiv' that returns the result of
-- division between two numbers passed in the function
DELIMITER //

DROP FUNCTION IF EXISTS `SafeDiv`;

CREATE FUNCTION SafeDiv(
	a INTEGER,
    b INTEGER
) 
RETURNS FLOAT
DETERMINISTIC
BEGIN
    DECLARE result FLOAT;
    IF b = 0 THEN
	    SET result = 0;
    ELSE
        SET result = (a / b);
    END IF;
	RETURN (result);
END //
DELIMITER ;
