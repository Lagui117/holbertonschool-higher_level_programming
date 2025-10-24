-- Task 8: List all cities of California
-- Output columns: id, name
-- Sort by id ASC
-- No JOIN allowed. Use subquery.

SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
