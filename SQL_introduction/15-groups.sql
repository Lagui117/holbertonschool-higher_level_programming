-- Task 15: Group rows by score and count how many rows have each score
-- Output columns:
--   score
--   number (COUNT of rows with this score)
-- Sort by number DESC
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
