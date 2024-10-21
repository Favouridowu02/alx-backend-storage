-- An sql script that lista all bands with Glam rock as the main style, ranked by their longevity

/* SELECT `band_name`,
	IF (split IS NOT NULL, split - formed, 2022 - formed) AS lifespan
FROM metal_bands WHERE style = "Glam rock" ORDER BY lifespan;i */


SELECT `band_name`, (IFNULL(split, 2022) - formed) AS lifespan
FROM metal_bands
WHERE FIND_IN_SET('Glam rock', IFNULL(style, "")) > 0
ORDER BY lifespan DESC;
