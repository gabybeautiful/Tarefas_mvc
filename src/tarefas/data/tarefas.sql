CREATE DATABASE IF NOT EXISTS `tarefas`;

USE `tarefas`;

CREATE TABLE IF NOT EXISTS `tarefa`(
    `id_tarefa` BIGINT INT NOT NULL  PRIMARY KEY,
    `titulo_tarefa` VARCHAR(100)NOT NULL,
    `data_conclusao` DATETIME NULL
);
