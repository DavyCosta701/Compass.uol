-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;
USE `mydb` ;

-- -----------------------------------------------------
-- Placeholder table for view `mydb`.`dim_carro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`dim_carro` (`idCarro` INT, `kilometragem` INT, `classificacao` INT, `modelo` INT, `ano` INT, `marca` INT);

-- -----------------------------------------------------
-- Placeholder table for view `mydb`.`dim_cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`dim_cliente` (`idCliente` INT, `nome_cliente` INT, `cidade_cliente` INT, `estado_cliente` INT, `pais_cliente` INT);

-- -----------------------------------------------------
-- Placeholder table for view `mydb`.`dim_data`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`dim_data` (`idData` INT, `horalocacao` INT, `horaentrega` INT, `datalocacao` INT, `dataentrega` INT);

-- -----------------------------------------------------
-- Placeholder table for view `mydb`.`dim_vendedor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`dim_vendedor` (`idvendedor` INT, `nome_vendedor` INT, `sexo_vendedor` INT, `estado_vendedor` INT);

-- -----------------------------------------------------
-- Placeholder table for view `mydb`.`fact_locacao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`fact_locacao` (`idlocacao` INT, `qtddiaria` INT, `vlrdiaria` INT, `combustivel` INT, `cliente_idCliente` INT, `vendedor_idvendedor` INT, `carro_idcarro` INT, `data_idData` INT);

-- -----------------------------------------------------
-- View `mydb`.`dim_carro`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`dim_carro`;
USE `mydb`;
CREATE  OR REPLACE VIEW `dim_carro` AS
    SELECT 
        idcarro AS idCarro,
        kmcarro AS kilometragem,
        classicarro AS classificacao,
        modelo_carro AS modelo,
        anocarro AS ano,
        marca_carro AS marca
    FROM
        carro AS c
            JOIN
        modelo_carro mc ON c.modelo_carro_idmodelo_carro = mc.idmodelo_carro
            JOIN
        anocarro ac ON c.anocarro_idanocarro = ac.idanocarro
            JOIN
        marca_carro mac ON c.marca_carro_idmarca_carro = mac.idmarca_carro
;

-- -----------------------------------------------------
-- View `mydb`.`dim_cliente`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`dim_cliente`;
USE `mydb`;
CREATE  OR REPLACE VIEW `dim_cliente` AS
    SELECT 
        idCliente AS idCliente,
        nomeCliente AS nome_cliente,
        cidade_cliente AS cidade_cliente,
        estado_cliente AS estado_cliente,
        pais_cliente AS pais_cliente
    FROM
        cliente AS c
            JOIN
       cidade_cliente ci ON c.cidade_cliente_idcidade_cliente = ci.idcidade_cliente
            JOIN
        estado_cliente e ON ci.estado_cliente_idestado_cliente = e.idestado_cliente
            JOIN
        pais_cliente p ON p.idpais_cliente = e.pais_cliente_idpais_cliente
;

-- -----------------------------------------------------
-- View `mydb`.`dim_data`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`dim_data`;
USE `mydb`;
CREATE  OR REPLACE VIEW `dim_data` AS
    SELECT 
		iddatalocacao as idData,
        horalocacao, horaentrega, datalocacao, dataentrega
    FROM
        locacao lo
            JOIN
        datalocacao dl ON lo.datalocacao_iddatalocacao = dl.iddatalocacao
            JOIN
        dataentrega de ON lo.dataentrega_iddataentrega = de.iddataentrega;

-- -----------------------------------------------------
-- View `mydb`.`dim_vendedor`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`dim_vendedor`;
USE `mydb`;
CREATE  OR REPLACE VIEW `dim_vendedor` AS
    SELECT 
        idvendedor, nome_vendedor, sexo_vendedor, estado_vendedor
    FROM
        vendedor v
            JOIN
        estado_vendedor ev ON v.estado_vendedor_idestado_vendedor = ev.idestado_vendedor;

-- -----------------------------------------------------
-- View `mydb`.`fact_locacao`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`fact_locacao`;
USE `mydb`;
CREATE  OR REPLACE VIEW `fact_locacao` AS
    SELECT 
        idlocacao,
        qtddiaria,
        vlrdiaria,
        tipocombustivel,
        datalocacao_iddatalocacao,
        dataentrega_iddataentrega,
        cliente_idCliente,
        vendedor_idvendedor,
        carro_idcarro,
        idData as data_idData
    FROM
        locacao l
            JOIN
        combustivel c ON l.combustivel_idcombustivel = c.idcombustivel
            JOIN
        dim_data dd ON l.dataentrega_iddataentrega = dd.idData;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
