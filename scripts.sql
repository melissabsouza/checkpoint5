CREATE TABLE LOGIN_CP(
    id number primary key
    login varchar (200),
    senha varchar(200)
);

CREATE TABLE CADASTRO_CP(
    id number primary key
    login varchar (200),
    senha varchar(200),
    email varchar(200),
    nome varchar(200),,
    rg number,
    cpf number not null,
    data_nascimento varchar(200),
    endereco varchar(200),
    role varchar(200),
);