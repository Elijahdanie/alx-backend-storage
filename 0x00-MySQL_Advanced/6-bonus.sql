-- Adds new correction to the student
DELIMITER \\
CREATE PROCEDURE AddBonus(IN user_id, IN project_name, IN score)
BEGIN
    INSERT INTO projects VALUES(name)
    SELECT * FROM projects WHERE name=project_name
    WHERE IF NOT EXISTS (SELECT * FROM projects WHERE name=project_name) LIMIT 1;

    INSERT INTO corrections (user_id, project_id, score)
    VALUES(user_id, (SELECT id from projects WHERE name=project_name), score);
END

DELIMITER