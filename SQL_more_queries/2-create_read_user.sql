-- Task 2: Create database hbtn_0d_2 and user_0d_2
-- user_0d_2 password: user_0d_2_pwd
-- user_0d_2 must have ONLY SELECT privilege on hbtn_0d_2
-- Must not fail if DB or user already exist.

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

FLUSH PRIVILEGES;
