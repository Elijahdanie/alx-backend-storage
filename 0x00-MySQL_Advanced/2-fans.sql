-- This scripts finds the number of fans
-- of different metal bands grouped by their origin

SELECT origin, SUM(fans) as nb_fans
from metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
