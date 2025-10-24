-- Task 1: Create MySQL user user_0d_1 with all privileges
-- user_0d_1 password: user_0d_1_pwd
-- Must not fail if the user already exists.

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

FLUSH PRIVILEGES;
