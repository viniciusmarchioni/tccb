-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: db_fut
-- ------------------------------------------------------
-- Server version	8.0.37

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `times`
--

DROP TABLE IF EXISTS `times`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `times` (
  `id` int NOT NULL,
  `nome` varchar(50) DEFAULT NULL,
  `logo` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `times`
--

LOCK TABLES `times` WRITE;
/*!40000 ALTER TABLE `times` DISABLE KEYS */;
INSERT INTO `times` VALUES (118,'Bahia','https://media.api-sports.io/football/teams/118.png'),(119,'Internacional','https://media.api-sports.io/football/teams/119.png'),(120,'Botafogo','https://media.api-sports.io/football/teams/120.png'),(121,'Palmeiras','https://media.api-sports.io/football/teams/121.png'),(123,'Sport Recife','https://media.api-sports.io/football/teams/123.png'),(124,'Fluminense','https://media.api-sports.io/football/teams/124.png'),(126,'Sao Paulo','https://media.api-sports.io/football/teams/126.png'),(127,'Flamengo','https://media.api-sports.io/football/teams/127.png'),(128,'Santos','https://media.api-sports.io/football/teams/128.png'),(129,'Ceara','https://media.api-sports.io/football/teams/129.png'),(130,'Gremio','https://media.api-sports.io/football/teams/130.png'),(131,'Corinthians','https://media.api-sports.io/football/teams/131.png'),(133,'Vasco DA Gama','https://media.api-sports.io/football/teams/133.png'),(135,'Cruzeiro','https://media.api-sports.io/football/teams/135.png'),(136,'Vitoria','https://media.api-sports.io/football/teams/136.png'),(152,'Juventude','https://media.api-sports.io/football/teams/152.png'),(154,'Fortaleza EC','https://media.api-sports.io/football/teams/154.png'),(794,'RB Bragantino','https://media.api-sports.io/football/teams/794.png'),(1062,'Atletico-MG','https://media.api-sports.io/football/teams/1062.png'),(7848,'Mirassol','https://media.api-sports.io/football/teams/7848.png');
/*!40000 ALTER TABLE `times` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-07 23:22:29
