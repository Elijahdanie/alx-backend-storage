-- Creates a function 'safeDiv' that returns the result of
-- division between two numbers passed in the function

DELIMITER //

CREATE FUNCTION SafeDiv (
    a INTEGER,
    b INTEGER
)
RETURNS INTEGER

BEGIN
    DECLARE result FLOAT;
    IF b = 0 THEN
        SET result = 0;
    ELSE
        SET result = ((a * 1.0) / b);
    END IF
    RETURN result
END //

DELIMITER;
