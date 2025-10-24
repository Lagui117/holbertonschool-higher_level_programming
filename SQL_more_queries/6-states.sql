-- Task 6: Create database hbtn_0d_usa and table states
-- Table states:
--   id INT NOT NULL AUTO_INCREMENT PRIMARY KEY
--   name VARCHAR(256) NOT NULL
-- Must not fail if DB or table already exist.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
