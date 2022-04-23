-- Creates a function 'safeDiv' that returns the result of
-- division between two numbers passed in the function

DELIMITER //

CREATE FUNCTION SafeDiv (
    a INT,
    b INT,
)
RETURNS INT

BEGIN
    DECLARE result = 0;
    IF b = 0 THEN
        SET result = 0;
    ELSE
        SET result = (a / b);
    END IF
    RETURN result
END //

DELIMITER;
