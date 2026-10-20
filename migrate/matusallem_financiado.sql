CREATE DATABASE if NOT exists matusallem_financiado;
USE matusallem_financiado;


CREATE TABLE IF NOT EXISTS tb_usuarios (
    id_login VARCHAR(50) NOT NULL,
    senha VARCHAR(255) NOT NULL,
    PRIMARY KEY (id_login)
);


CREATE TABLE IF NOT EXISTS tb_categorias (
    id_categoria INT AUTO_INCREMENT NOT NULL,
    tipo VARCHAR(100) NOT NULL,
    id_login VARCHAR(50) NOT NULL,
    PRIMARY KEY (id_categoria),
    FOREIGN KEY (id_login) REFERENCES tb_usuarios(id_login)
);


CREATE TABLE IF NOT EXISTS tb_despesas (
    id_despesa INT AUTO_INCREMENT NOT NULL,
    id_categoria INT NOT NULL,
    id_login VARCHAR(50) NOT NULL,
    data DATE NOT NULL,
    hora TIME NOT NULL,
    descricao VARCHAR(255),
    valor DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (id_despesa),
    FOREIGN KEY (id_categoria) REFERENCES tb_categorias(id_categoria),
    FOREIGN KEY (id_login) REFERENCES tb_usuarios(id_login)
);