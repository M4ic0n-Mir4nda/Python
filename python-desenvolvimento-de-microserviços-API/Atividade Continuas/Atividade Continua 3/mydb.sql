CREATE TABLE Alunos (
id int primary key auto_increment,
nome varchar(100) not null,
idade int not null,
turma varchar(30)
);

INSERT INTO Alunos (nome, idade, turma)
VALUE
('Mariano Silva', 25, 'ADS-3B');