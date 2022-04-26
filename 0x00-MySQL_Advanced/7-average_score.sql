-- Createa a stored procedure for computing
--  and setting student's average score
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
   UPDATE users
   SET average_score = 
   (SELECT AVG(score)
    FROM corrections
	WHERE corrections.user_id=user_id
	GROUP BY corrections.user_id )
    WHERE id=user_id;
END //
