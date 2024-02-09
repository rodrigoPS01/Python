CREATE DATABASE escola;
USE escola;

CREATE TABLE alunos(
	id_aluno INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255),
    idade INT,
    endereco VARCHAR(50)
);

CREATE TABLE professores(
	id_professor INT PRIMARY KEY AUTO_INCREMENT,
	nome_professor VARCHAR(255),
    endereco VARCHAR(50),
    especializacao VARCHAR(50)
);

CREATE TABLE turma(
	identificador VARCHAR(50),
    horario_inicio DATE,
    dia_semana INT
);

CREATE TABLE diciplina(
	identificador INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50),
    qtde_aulas INT    
)

#2° PROGRAMA

CREATE DATABASE locadora;
USE locadora;

CREATE TABLE filmes(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(255),
    genero VARCHAR(50),
    duracoa TIME
);

CREATE TABLE jogos(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(255),
    categoria VARCHAR(50),
    num_jogadores VARCHAR(50)
);

CREATE TABLE series(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(255),
    categoria VARCHAR(50),
    num_temporada TIME
);

CREATE TABLE alugue_filme(
	id INT PRIMARY KEY AUTO_INCREMENT,
	id_filmes INT,
    FOREIGN KEY (id_filmes) REFERENCES filmes(id),
    valor FLOAT,
    horario TIME
);

CREATE TABLE alugue_filme(
	id INT PRIMARY KEY AUTO_INCREMENT,
	id_jogos INT,
    FOREIGN KEY (id_jogos) REFERENCES jogos(id),
    valor FLOAT,
    horario TIME
);

CREATE TABLE alugue_series(
	id INT PRIMARY KEY AUTO_INCREMENT,
	id_series INT,
    FOREIGN KEY (id_series) REFERENCES series(id),
    valor FLOAT,
    horario TIME
)

# 3° PROGRAMA
CREATE DATABASE plano_saude;
USE plano_saude;

CREATE TABLE planos(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255),
    valor FLOAT
);

CREATE TABLE clientes(
	id  INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255),
    endereco VARCHAR(255),
    cpf VARCHAR(11),
    telefone VARCHAR(11),
    id_plano INT,
    FOREIGN KEY (id_plano) REFERENCES planos(id)
);

CREATE TABLE dependentes(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255),
    id_clientes INT,
    FOREIGN KEY (id_clientes) REFERENCES clientes(id)
)
