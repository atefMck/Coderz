-- setup sql
CREATE DATABASE IF NOT EXISTS coderz_dev_db;
CREATE USER IF NOT EXISTS 'coder_dev'@'localhost' IDENTIFIED BY 'Coderz';
GRANT ALL ON coderz_dev_db.* TO 'coder_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'coder_dev'@'localhost';
