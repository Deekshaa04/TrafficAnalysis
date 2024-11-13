SELECT
    *
FROM
    datavision.transformed_data
WHERE
    day_of_week IN ('Saturday', 'Sunday');
