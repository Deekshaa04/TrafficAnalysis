SELECT
    intersection_name,
    AVG(vehicle_count) AS avg_vehicle_count
FROM
    datavision.transformed_data
GROUP BY
    intersection_name
ORDER BY
    avg_vehicle_count DESC
LIMIT 1;
