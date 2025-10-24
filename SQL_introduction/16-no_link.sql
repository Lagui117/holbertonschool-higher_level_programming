-- Task 16: List all rows of second_table
-- Do NOT list rows where name is NULL or empty
-- Display: score then name
-- Order: score DESC

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
  AND name != ''
ORDER BY score DESC;
