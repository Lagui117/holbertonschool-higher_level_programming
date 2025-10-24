-- Task 9: List all cities with their state
-- Output columns: cities.id, cities.name, states.name
-- Sort by cities.id ASC
-- Only one SELECT.

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
