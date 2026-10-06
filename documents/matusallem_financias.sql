create database matusallem_financiado;

use matusallem_financiado;

CREATE TABLE if not exists tb_usuarios (
 login VARCHAR(60) NOT NULL PRIMARY KEY,
 senha VARCHAR(200)
);


CREATE TABLE if not exists tb_categorias (
 id_categoria INT auto_increment,
 login VARCHAR(60) NOT NULL,
 nome_categoria VARCHAR(60),

 PRIMARY KEY (id_categoria),

 FOREIGN KEY (login) REFERENCES tb_usuarios (login)
);


CREATE TABLE if not exists tb_despesas (
 id_despesa INT auto_increment,
 id_categoria INT NOT NULL,
 login VARCHAR(60) NOT NULL,
 dt_cadastro DATETIME,
 valor DECIMAL(7,2) NOT NULL,
 descricao_despesa VARCHAR(80),

 PRIMARY KEY (id_despesa),

 FOREIGN KEY (id_categoria) REFERENCES tb_categorias (id_categoria),
 FOREIGN KEY (login) REFERENCES tb_usuarios (login)
);


