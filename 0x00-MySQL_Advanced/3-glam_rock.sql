-- This selects the bands with style Glam_rock
-- ranked by their lifespan

SELECT band_name, COALESCE(split, 2020) - formed AS lifespan
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
