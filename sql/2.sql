SELECT
    HOUR(timestamp) AS hour_of_day,
    AVG(vehicle_count) AS average_vehicle_count
FROM
    datavision.transformed_data
GROUP BY
    HOUR(timestamp)
ORDER BY
    hour_of_day;
