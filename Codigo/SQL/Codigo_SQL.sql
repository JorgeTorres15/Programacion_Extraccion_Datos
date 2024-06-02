# esta es la base de datos con las tablas normalizadas
drop database if exists Metacritics;
create database Metacritics;
use Metacritics;

CREATE TABLE Plataforma (
    id_plataforma INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(255) UNIQUE
);
select * from Plataforma;


CREATE TABLE Desarrollador (
    id_desarrollador INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(255) UNIQUE
);

CREATE TABLE Publicado_por (
    id_publicado_por INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(255) UNIQUE
);

CREATE TABLE Genero (
    id_genero INT AUTO_INCREMENT PRIMARY KEY,
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
    FOREIGN KEY (Plataforma_ID) REFERENCES Plataforma(id_plataforma),
    FOREIGN KEY (Desarrollador_ID) REFERENCES Desarrollador(id_desarrollador),
    FOREIGN KEY (Publicado_por_ID) REFERENCES Publicado_por(id_publicado_por),
    FOREIGN KEY (Genero_ID) REFERENCES Genero(id_genero)
);
select * from Videojuegos;
