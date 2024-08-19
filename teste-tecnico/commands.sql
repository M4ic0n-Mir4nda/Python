CREATE DATABASE IF NOT EXISTS carford;

CREATE TABLE IF NOT EXISTS owner (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS cars (
    id INT AUTO_INCREMENT PRIMARY KEY,
    color ENUM('yellow', 'blue', 'gray'),
    model ENUM('hatch', 'sedan', 'convertible'),
    id_owner INT,
    FOREIGN KEY (id_owner) REFERENCES owner(id)
);
