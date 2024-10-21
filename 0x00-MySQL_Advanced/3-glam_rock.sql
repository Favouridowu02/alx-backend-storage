-- An sql script that lista all bands with Glam rock as the main style, ranked by their longevity

/* SELECT `band_name`,
	IF (split IS NOT NULL, split - formed, 2022 - formed) AS lifespan
FROM metal_bands WHERE style = "Glam rock" ORDER BY lifespan;i */


SELECT `band_name`,
        CASE
                WHEN split IS NOT NULL THEN split - formed
                ELSE 2022 - formed
        END AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan
