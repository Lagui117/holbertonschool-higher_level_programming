# Python - Object-relational mapping

This project explores Object-Relational Mapping (ORM) in Python, connecting Python applications to MySQL databases using MySQLdb and SQLAlchemy.

## Learning Objectives

- How to connect to a MySQL database from a Python script
- How to SELECT rows in a MySQL table from a Python script
- How to INSERT rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table
- Using MySQLdb module for direct SQL queries
- Using SQLAlchemy ORM for object-oriented database access

## Concepts

### Without ORM (MySQLdb)
Direct SQL queries using MySQLdb to interact with the database.

### With ORM (SQLAlchemy)
Object-oriented approach where you work with Python objects instead of writing SQL queries.

## Requirements

- Python 3.8.5
- MySQLdb version 2.0.x
- SQLAlchemy version 1.4.x
- MySQL 8.0
- pycodestyle compliant
- All files must be executable
- All modules, classes, and functions must have documentation

## Installation

### MySQL 8.0
```bash
sudo apt update
sudo apt install mysql-server
```

### MySQLdb
```bash
sudo apt-get install python3-dev libmysqlclient-dev zlib1g-dev
sudo pip3 install mysqlclient==2.0.3
```

### SQLAlchemy
```bash
sudo pip3 install SQLAlchemy==1.4.22
```

## Tasks Overview

- **0-5**: MySQLdb direct SQL queries
- **6-14**: SQLAlchemy ORM implementation

## Author

Project created as part of Holberton School curriculum.