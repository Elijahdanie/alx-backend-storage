-- This scripts finds the number of fans
-- of different metal bands grouped by their origin

SELECT origin, SUM(fans) as nb_fans
GROUP BY origin
ORDER BY nb_fans DESC;
