create database Videojuegos;
use Videojuegos;


// Roles //
create if not exists role Scrum-master
create if not exists role Equipo-BD


//Tabla_main//
create if not exists table Type_review(
  id_type_review int primary key autoincrement,
  type varchar(50), not null default "Sin descripcion" 
);

create if not exists table reviews(
  id_review int primary key autoincrement,
  calificacion interger(2,2) default 0,
  review varchar(1000) default "Sin reseña",
  id_type_review int,
  foreign key (id_type_review) references type_review (id_type_review)
);

create if not exists table Videogames(
-- Pendiente quedo a lo que me sugieren ustedes
);
