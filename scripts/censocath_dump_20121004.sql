-- MySQL dump 10.13  Distrib 5.1.63, for debian-linux-gnu (i486)
--
-- Host: localhost    Database: censocath
-- ------------------------------------------------------
-- Server version	5.1.63-0ubuntu0.10.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `censocath`
--

/*!40000 DROP DATABASE IF EXISTS `censocath`*/;

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `censocath` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `censocath`;

--
-- Table structure for table `Calle`
--

DROP TABLE IF EXISTS `Calle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Calle` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(255) DEFAULT NULL,
  `IdColonia` int(11) DEFAULT NULL,
  `IdSector` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `IdSector` (`IdSector`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Calle`
--

LOCK TABLES `Calle` WRITE;
/*!40000 ALTER TABLE `Calle` DISABLE KEYS */;
/*!40000 ALTER TABLE `Calle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Colonia`
--

DROP TABLE IF EXISTS `Colonia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Colonia` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Colonia`
--

LOCK TABLES `Colonia` WRITE;
/*!40000 ALTER TABLE `Colonia` DISABLE KEYS */;
INSERT INTO `Colonia` (`Id`, `Nombre`) VALUES (1,'San Pablo Xochimehuacan'),(2,'Santa Bárbara'),(3,'Mariscal'),(4,'Barranca Honda'),(5,'28 de Octubre'),(6,'Francisco I. Madero'),(7,'Miravalle'),(10,'San cuanácaro'),(11,'Terepitengo'),(12,'(u\'San cuan\\xe1caro\',)'),(13,'(u\'Terepitengo\',)');
/*!40000 ALTER TABLE `Colonia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Encuesta`
--

DROP TABLE IF EXISTS `Encuesta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Encuesta` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Fecha` datetime DEFAULT NULL,
  `IdEncuestador` int(11) DEFAULT NULL,
  `Observacion` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `IdEncuestador` (`IdEncuestador`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Encuesta`
--

LOCK TABLES `Encuesta` WRITE;
/*!40000 ALTER TABLE `Encuesta` DISABLE KEYS */;
/*!40000 ALTER TABLE `Encuesta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Encuestador`
--

DROP TABLE IF EXISTS `Encuestador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Encuestador` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Encuestador`
--

LOCK TABLES `Encuestador` WRITE;
/*!40000 ALTER TABLE `Encuestador` DISABLE KEYS */;
INSERT INTO `Encuestador` (`Id`, `Nombre`) VALUES (1,'Otro'),(2,'Esperanza Márquez Méndez'),(3,'Carlos Alberto Bañuelos Moro');
/*!40000 ALTER TABLE `Encuestador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Familia`
--

DROP TABLE IF EXISTS `Familia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Familia` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `IdCalle` int(11) DEFAULT NULL,
  `IdManzana` int(11) DEFAULT NULL,
  `IdEncuesta` int(11) DEFAULT NULL,
  `NoExt` varchar(255) DEFAULT NULL,
  `NoInt` varchar(255) DEFAULT NULL,
  `Lote` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `IdCalle` (`IdCalle`),
  KEY `IdEncuesta` (`IdEncuesta`),
  KEY `IdManzana` (`IdManzana`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Familia`
--

LOCK TABLES `Familia` WRITE;
/*!40000 ALTER TABLE `Familia` DISABLE KEYS */;
/*!40000 ALTER TABLE `Familia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Manzana`
--

DROP TABLE IF EXISTS `Manzana`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Manzana` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(255) DEFAULT NULL,
  `IdColonia` int(11) DEFAULT NULL,
  `IdSector` int(11) DEFAULT NULL,
  `IdCalle` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `IdCalle` (`IdCalle`),
  KEY `IdColonia` (`IdColonia`),
  KEY `IdSector` (`IdSector`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Manzana`
--

LOCK TABLES `Manzana` WRITE;
/*!40000 ALTER TABLE `Manzana` DISABLE KEYS */;
/*!40000 ALTER TABLE `Manzana` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Parentesco`
--

DROP TABLE IF EXISTS `Parentesco`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Parentesco` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Parentesco`
--

LOCK TABLES `Parentesco` WRITE;
/*!40000 ALTER TABLE `Parentesco` DISABLE KEYS */;
INSERT INTO `Parentesco` (`Id`, `Nombre`) VALUES (1,'Padre'),(2,'Madre'),(3,'Hijo'),(4,'Hija'),(5,'Otro');
/*!40000 ALTER TABLE `Parentesco` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Persona`
--

DROP TABLE IF EXISTS `Persona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Persona` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `IdParentesco` int(11) DEFAULT NULL,
  `Nombre` varchar(255) DEFAULT NULL,
  `Edad` int(11) DEFAULT NULL,
  `IdSexo` int(11) DEFAULT NULL,
  `IdReligion` int(11) DEFAULT NULL,
  `LugarOrigen` varchar(255) DEFAULT NULL,
  `IdFamilia` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `IdFamilia` (`IdFamilia`),
  KEY `IdParentesco` (`IdParentesco`),
  KEY `IdReligion` (`IdReligion`),
  KEY `IdSexo` (`IdSexo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Persona`
--

LOCK TABLES `Persona` WRITE;
/*!40000 ALTER TABLE `Persona` DISABLE KEYS */;
/*!40000 ALTER TABLE `Persona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Religion`
--

DROP TABLE IF EXISTS `Religion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Religion` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Religion`
--

LOCK TABLES `Religion` WRITE;
/*!40000 ALTER TABLE `Religion` DISABLE KEYS */;
INSERT INTO `Religion` (`Id`, `Nombre`) VALUES (1,'Católica'),(2,'Cristiana'),(3,'Santos de los últimos días'),(4,'Testigos de Jehová'),(5,'Piedra Angular'),(6,'Luz del día'),(7,'Budistas'),(8,'Otros');
/*!40000 ALTER TABLE `Religion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Sexo`
--

DROP TABLE IF EXISTS `Sexo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Sexo` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Sexo`
--

LOCK TABLES `Sexo` WRITE;
/*!40000 ALTER TABLE `Sexo` DISABLE KEYS */;
INSERT INTO `Sexo` (`Id`, `Nombre`) VALUES (1,'Hombre'),(2,'Mujer'),(3,'Otro');
/*!40000 ALTER TABLE `Sexo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2012-10-04  1:44:32
