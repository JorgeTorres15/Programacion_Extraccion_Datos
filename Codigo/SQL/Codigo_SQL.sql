drop database if exists Metacritics;
create database Metacritics;
use Metacritics;

CREATE TABLE Plataforma (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(255) UNIQUE
);

CREATE TABLE Desarrollador (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(255) UNIQUE
);

CREATE TABLE Publicado_por (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(255) UNIQUE
);

CREATE TABLE Genero (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(255) UNIQUE
);

CREATE TABLE Videojuegos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(255),
    Fecha_Lanzamiento varchar(100),
    Meta_Score INT,
    Catalogado_por_Meta VARCHAR(255),
    User_Score DECIMAL(3, 1),
    Catalogado_por_Usuario VARCHAR(255),
    Plataforma_ID INT,
    Desarrollador_ID INT,
    Publicado_por_ID INT,
    Genero_ID INT,
    FOREIGN KEY (Plataforma_ID) REFERENCES Plataforma(id) ON DELETE SET NULL,
    FOREIGN KEY (Desarrollador_ID) REFERENCES Desarrollador(id) ON DELETE SET NULL,
    FOREIGN KEY (Publicado_por_ID) REFERENCES Publicado_por(id) ON DELETE SET NULL,
    FOREIGN KEY (Genero_ID) REFERENCES Genero(id) ON DELETE SET NULL
);
