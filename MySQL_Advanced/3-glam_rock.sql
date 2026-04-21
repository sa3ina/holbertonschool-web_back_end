-- List all bands with Glam rock as their main style, ranked by their longevity up to the year 2024
SELECT band_name, (2024 - formed) AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;