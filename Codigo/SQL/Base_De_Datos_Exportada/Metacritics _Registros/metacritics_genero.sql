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
-- Table structure for table `genero`
--

DROP TABLE IF EXISTS `genero`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genero` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Nombre` (`Nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=60 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genero`
--

LOCK TABLES `genero` WRITE;
/*!40000 ALTER TABLE `genero` DISABLE KEYS */;
INSERT INTO `genero` VALUES (29,'2D Beat-\'Em-Up'),(21,'2D Fighting'),(15,'2D Platformer'),(2,'3D Fighting'),(3,'3D Platformer'),(18,'4X Strategy'),(55,'Action'),(14,'Action Adventure'),(51,'Action Puzzle'),(11,'Action RPG'),(48,'Adventure'),(46,'Aircraft Combat Sim'),(43,'Aircraft Sim'),(34,'Application'),(23,'Arcade'),(40,'Arcade Racing'),(20,'Auto Racing'),(13,'Auto Racing Sim'),(41,'Baseball Sim'),(30,'Basketball Sim'),(44,'Card Battle'),(25,'Command RTS'),(10,'Compilation'),(53,'Dancing'),(59,'First-Person Adventure'),(6,'Football Sim'),(5,'FPS'),(32,'Future Racing'),(50,'Golf'),(35,'Hockey Sim'),(16,'JRPG'),(7,'Linear Action Adventure'),(24,'Management'),(57,'Marine Combat Sim'),(42,'Metroidvania'),(33,'MMORPG'),(1,'Open-World Action'),(49,'Point-and-Click'),(54,'Rail Shooter'),(22,'Real-Time Strategy'),(28,'Rhythm'),(31,'Roguelike'),(4,'Skating'),(26,'Skiing'),(27,'Soccer Sim'),(45,'Space Combat Sim'),(8,'Survival'),(38,'Tactical FPS'),(39,'Tennis'),(17,'Third Person Shooter'),(19,'Third-Person Adventure'),(58,'Top-Down Shoot-\'Em-Up'),(37,'Turn-Based Tactics'),(52,'Tycoon'),(47,'Vehicle Combat Sim'),(36,'Virtual Life'),(12,'Visual Novel'),(9,'Western RPG'),(56,'Wrestling');
/*!40000 ALTER TABLE `genero` ENABLE KEYS */;
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
