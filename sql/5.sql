SELECT
    intersection_name,
    AVG(average_speed) AS avg_speed
FROM
    datavision.transformed_data
GROUP BY
    intersection_name;
