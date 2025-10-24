-- Task 4: Create table first_table in the current database
-- Table schema:
--   id   INT
--   name VARCHAR(256)
-- Must NOT fail if the table already exists.
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
