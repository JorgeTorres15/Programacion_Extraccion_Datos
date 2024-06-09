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
-- Table structure for table `desarrollador`
--

DROP TABLE IF EXISTS `desarrollador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `desarrollador` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Nombre` (`Nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=147 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `desarrollador`
--

LOCK TABLES `desarrollador` WRITE;
/*!40000 ALTER TABLE `desarrollador` DISABLE KEYS */;
INSERT INTO `desarrollador` VALUES (96,'1C Entertainment'),(90,'2015'),(119,'2D Boy'),(120,'Alphadream Corporation'),(91,'Asobo Studio'),(26,'Atlus'),(82,'Bandai Namco Games'),(51,'Bay 12 Games'),(20,'Bethesda Game Studios'),(17,'BioWare'),(116,'Bizarre Creations'),(109,'Black Isle Studios'),(135,'Black Tabby Games'),(42,'Blizzard Entertainment'),(77,'Bluepoint Games'),(129,'Broccoli'),(10,'Bungie'),(95,'Camelot Software Planning'),(15,'Capcom'),(114,'Capcom R&D Division 1'),(101,'Cardboard Computer'),(72,'CD Projekt Red Studio'),(56,'Clover Studio'),(99,'Core Design Ltd.'),(75,'Creative Assembly'),(84,'Creative Business Unit III'),(41,'Criterion Games'),(146,'Crows Crows Crows'),(111,'Crystal Dynamics'),(102,'Crytek'),(108,'Digital Illusions'),(9,'DMA Design'),(86,'Dreamworks Interactive'),(55,'EA Canada'),(25,'EA Sports'),(53,'EA Sports Big'),(32,'EA Tiburon'),(121,'Eidetic'),(93,'Electronic Arts'),(80,'Ensemble Studios'),(33,'Epic Games'),(89,'Eremite Games'),(131,'Factor 5'),(44,'Firaxis Games'),(19,'From Software'),(105,'Funcom'),(46,'Game Arts'),(31,'GREZZO'),(110,'Guerrilla'),(73,'HAL Labs'),(59,'Harmonix Music Systems'),(127,'HexaDrive'),(74,'Hitmaker'),(18,'HuneX'),(35,'id Software'),(100,'Incognito Inc.'),(133,'increpare'),(36,'Infinity Ward'),(98,'Insomniac Games'),(58,'Intelligent Systems'),(132,'Ion Storm'),(13,'Irrational Games'),(22,'KCEJ'),(113,'KCEK'),(57,'KCET'),(138,'Kinmoku'),(140,'Klei Entertainment'),(43,'Kojima Productions'),(128,'Konami'),(16,'Larian Studios Games'),(145,'Lead Pursuit'),(126,'Lionhead Studios'),(124,'LocalThunk'),(79,'Looking Glass Studios'),(38,'LucasArts'),(70,'Maddy Makes Games'),(141,'Matthias Linda'),(69,'Maxis'),(24,'Media Molecule'),(71,'Microsoft Game Studios'),(144,'MINT ROCKET'),(106,'Monolith Productions'),(67,'Monolith Soft'),(137,'Moon Studios'),(34,'MPS Labs'),(2,'Namco'),(50,'Namco Bandai Games'),(14,'Naughty Dog'),(5,'Neversoft Entertainment'),(40,'NexTech'),(1,'Nintendo'),(4,'Nintendo EAD Tokyo'),(92,'Northway Games'),(52,'Number None Inc.'),(87,'Out Of The Park Developments'),(107,'Paradox Interactive'),(94,'PlatinumGames'),(63,'PLAYDEAD'),(64,'Playground Games'),(21,'Polyphony Digital'),(62,'Psygnosis'),(6,'Rare Ltd.'),(54,'Raster'),(103,'Ready at Dawn'),(122,'RedLynx'),(47,'Relic Entertainment'),(8,'Retro Studios'),(7,'Rockstar Games'),(49,'Rockstar Leeds'),(3,'Rockstar North'),(27,'Rockstar San Diego'),(23,'Rockstar Vienna'),(30,'Rocksteady Studios'),(117,'SCE Japan Studio'),(29,'SCE Santa Monica'),(104,'SCEA'),(130,'SCEA San Diego Studios'),(61,'Sega'),(45,'Sega AM2'),(123,'Shared Memory'),(68,'Silicon Knights'),(134,'Smilebit'),(66,'Square Enix'),(28,'SquareSoft'),(81,'Stardock'),(60,'Supergiant Games'),(136,'Team Cherry'),(142,'Team Meat'),(37,'Team Ninja'),(85,'ThatGameCompany'),(78,'tobyfox'),(83,'TOSE'),(76,'Turn 10'),(65,'Ubisoft'),(88,'Ubisoft Montpellier'),(39,'Ubisoft Montreal'),(118,'Ubisoft Paris'),(48,'Ubisoft Shanghai'),(12,'Valve Software'),(143,'Visceral Games'),(11,'Visual Concepts'),(97,'Volition Inc.'),(125,'Wube Software LTD.'),(115,'Yacht Club Games'),(139,'Yuke\'s'),(112,'ZA/UM');
/*!40000 ALTER TABLE `desarrollador` ENABLE KEYS */;
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
