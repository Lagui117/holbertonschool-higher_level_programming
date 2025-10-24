-- Task 9: Create table second_table and insert multiple rows
-- Table schema:
--   id INT
--   name VARCHAR(256)
--   score INT
-- Must NOT fail if table already exists.
-- Must insert the 4 rows in the task.

CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
