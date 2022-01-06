CREATE TABLE utente(
	id varchar(255) PRIMARY KEY NOT NULL,
	passwd varchar(255) not null,
	nome varchar(50) not null,
	cognome varchar(50) not null,
	cellulare char(10) not null,
	mail varchar(255) not null); 

CREATE TABLE festa(
	idfesta int PRIMARY KEY NOT NULL AUTO_INCREMENT,
	nbambini smallint unsigned DEFAULT 10,
	via varchar(255) not null,
	civico varchar(255) not null,
	citta varchar(255) not null,
	cap char(5) not null,
	dataf date not null,
	oini time not null,
	durata smallint unsigned DEFAULT 2,
	tipo ENUM('Comunione','Compleanno','Matrimonio','Misc'),
	qualita ENUM('Silver','Gold','Platinum'),
	prezzo double(6,2) not null,
	id1 varchar(255) not null, 
	FOREIGN KEY (id1) REFERENCES utente(id));