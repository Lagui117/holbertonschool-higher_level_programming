-- Task 4: Create table id_not_null
-- Columns:
--   id INT NOT NULL DEFAULT 1
--   name VARCHAR(256)
-- If table already exists, do not fail.

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);
