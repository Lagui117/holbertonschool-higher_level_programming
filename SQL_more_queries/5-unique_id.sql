-- Task 5: Create table unique_id
-- Columns:
--   id INT UNIQUE DEFAULT 1
--   name VARCHAR(256)
-- If table already exists, do not fail.

CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
