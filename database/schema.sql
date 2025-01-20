CREATE DATABASE if NOT EXISTS db_cinema;
USE db_cinema;

CREATE TABLE if not exists reservations(
    id INT AUTO_INCREMENT primary key;
    customer_name VARCHAR(100) not null;
    movie_name VARCHAR(100) not null;
    seat_number VARCHAR(100) not null;
    reservation_name DATETIME not null;

)




