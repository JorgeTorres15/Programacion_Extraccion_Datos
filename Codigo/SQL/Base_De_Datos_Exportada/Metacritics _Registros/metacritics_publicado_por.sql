-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: metacritics
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `publicado_por`
--

DROP TABLE IF EXISTS `publicado_por`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `publicado_por` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Nombre` (`Nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `publicado_por`
--

LOCK TABLES `publicado_por` WRITE;
/*!40000 ALTER TABLE `publicado_por` DISABLE KEYS */;
INSERT INTO `publicado_por` VALUES (65,'2D Boy'),(9,'2K Games'),(66,'989 Studios'),(4,'Activision'),(70,'Aksys Games'),(37,'Atari SA'),(23,'Atlus'),(16,'Bandai Namco Games'),(36,'Bay 12 Games'),(17,'Bethesda Softworks'),(67,'Bigmode'),(78,'Bizarre Creations'),(72,'Black Tabby Games'),(33,'Blizzard Entertainment'),(55,'Bungie'),(11,'Capcom'),(58,'Cardboard Computer'),(53,'CD Projekt'),(80,'Crows Crows Crows'),(75,'DECK13 Spotlight'),(13,'EA Games'),(22,'EA Sports'),(39,'EA Sports Big'),(49,'Eidos Interactive'),(14,'Electronic Arts'),(56,'Finji'),(60,'Fox Interactive'),(59,'Funcom'),(79,'Graphsim Entertainment'),(54,'Hooded Horse'),(28,'id Software'),(71,'increpare'),(62,'Infogrames'),(21,'Interplay'),(74,'Kinmoku'),(19,'Konami'),(12,'Larian Studios Games'),(15,'Limited Run Games'),(47,'Looking Glass Studios'),(30,'LucasArts'),(45,'Maddy Makes Games'),(44,'Maxis'),(27,'MicroProse'),(6,'Microsoft Game Studios'),(77,'MINT ROCKET'),(40,'MTV Games'),(2,'Namco'),(35,'Namco Bandai Games'),(1,'Nintendo'),(38,'Number None Inc.'),(52,'Out Of The Park Developments'),(61,'Paradox Interactive'),(42,'PLAYDEAD'),(68,'Playstack'),(32,'PlayStation Studios'),(57,'Psygnosis'),(5,'Rare Ltd.'),(51,'RedOctane'),(3,'Rockstar Games'),(10,'SCEA'),(7,'Sega'),(18,'Sierra Entertainment'),(25,'Sony Interactive Entertainment'),(24,'Square EA'),(43,'Square Enix'),(50,'Stardock'),(41,'Supergiant Games'),(73,'Team Cherry'),(76,'Team Meat'),(29,'Tecmo'),(34,'THQ'),(48,'tobyfox'),(31,'Ubisoft'),(20,'Valve Software'),(8,'VU Games'),(26,'Warner Bros. Interactive Entertainment'),(69,'Wube Software LTD.'),(46,'Xbox Game Studios'),(64,'Yacht Club Games'),(63,'ZA/UM');
/*!40000 ALTER TABLE `publicado_por` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-08 20:40:14
