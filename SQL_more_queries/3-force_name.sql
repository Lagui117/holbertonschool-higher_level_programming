-- Task 3: Create table force_name
-- Columns:
--   id INT
--   name VARCHAR(256) NOT NULL
-- If table already exists, do not fail.

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
