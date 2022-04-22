-- This selects the bands with style Glam_rock
-- ranked by their lifespan

SELECT band_name, COALESCE(split, 2020) - formed as lifespan
WHERE style like '%Glam_rock%'
ORDER BY lifespan DESC;
