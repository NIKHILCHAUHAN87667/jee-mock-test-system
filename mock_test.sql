-- MySQL dump 10.13  Distrib 9.0.1, for Win64 (x86_64)
--
-- Host: localhost    Database: mock_test
-- ------------------------------------------------------
-- Server version	9.0.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `attempt_test`
--

DROP TABLE IF EXISTS `attempt_test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attempt_test` (
  `attempt_id` int NOT NULL AUTO_INCREMENT,
  `test_id` int NOT NULL,
  `user_id` int NOT NULL,
  `start_time` datetime NOT NULL,
  `end_time` datetime NOT NULL,
  `score` int NOT NULL,
  PRIMARY KEY (`attempt_id`),
  KEY `test_id` (`test_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `attempt_test_ibfk_1` FOREIGN KEY (`test_id`) REFERENCES `mock_test` (`test_id`) ON DELETE CASCADE,
  CONSTRAINT `attempt_test_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attempt_test`
--

LOCK TABLES `attempt_test` WRITE;
/*!40000 ALTER TABLE `attempt_test` DISABLE KEYS */;
INSERT INTO `attempt_test` VALUES (2,1,1,'2025-02-15 13:44:23','2025-02-15 13:44:29',1),(3,2,2,'2025-02-15 13:50:15','2025-02-15 13:50:32',1),(4,3,1,'2025-02-15 13:54:31','2025-02-15 13:56:36',0),(5,4,1,'2025-02-15 14:15:21','2025-02-15 14:18:51',29),(6,5,1,'2025-02-15 14:59:48','2025-02-15 15:00:26',1),(7,6,2,'2025-02-15 15:06:57','2025-02-15 15:07:43',2),(8,7,1,'2025-02-15 15:17:30','2025-02-15 15:17:51',2),(9,8,1,'2025-02-15 15:24:55','2025-02-15 15:25:05',0),(10,9,1,'2025-02-15 15:39:01','2025-02-15 15:39:24',0),(11,10,1,'2025-02-15 16:24:40','2025-02-15 16:25:11',0),(12,11,1,'2025-02-15 16:35:14','2025-02-15 16:40:24',0),(13,12,1,'2025-02-16 12:24:41','2025-02-16 12:24:58',0),(14,13,1,'2025-02-16 12:31:06','2025-02-16 12:31:20',0),(15,14,1,'2025-02-16 12:32:21','2025-02-16 12:32:36',0),(16,15,1,'2025-02-16 12:34:25','2025-02-16 12:34:56',0),(17,16,1,'2025-02-16 12:40:24','2025-02-16 12:40:30',0),(18,17,1,'2025-02-16 12:40:24','2025-02-16 12:45:29',0),(19,19,1,'2025-02-16 13:22:35','2025-02-16 13:22:48',0),(20,20,1,'2025-02-16 13:23:38','2025-02-16 13:23:52',3),(21,24,1,'2025-02-16 16:23:24','2025-02-16 16:23:26',0),(22,25,1,'2025-02-16 17:05:48','2025-02-16 17:06:14',4),(23,27,1,'2025-02-16 17:53:16','2025-02-16 17:54:18',4),(24,28,1,'2025-02-16 17:57:34','2025-02-16 17:57:42',0),(25,29,1,'2025-02-16 20:14:57','2025-02-16 20:15:03',0),(26,30,2,'2025-02-19 10:54:23','2025-02-19 10:55:26',48),(27,31,2,'2025-02-19 11:01:23','2025-02-19 11:02:52',44),(28,32,2,'2025-02-19 11:11:58','2025-02-19 11:13:05',35),(29,33,2,'2025-02-19 12:09:56','2025-02-19 12:11:50',59),(30,34,2,'2025-02-19 16:50:51','2025-02-19 16:52:17',59),(31,35,2,'2025-02-19 17:03:21','2025-02-19 17:05:17',80),(32,36,1,'2025-02-21 14:23:20','2025-02-21 14:24:43',0),(33,37,1,'2025-02-21 14:26:23','2025-02-21 14:26:28',0),(34,38,1,'2025-02-21 14:32:42','2025-02-21 14:34:37',0),(35,40,1,'2025-02-21 15:35:08','2025-02-21 15:35:13',4),(36,90,2,'2025-03-06 18:12:56','2025-03-06 18:13:30',0);
/*!40000 ALTER TABLE `attempt_test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mock_test`
--

DROP TABLE IF EXISTS `mock_test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mock_test` (
  `test_id` int NOT NULL AUTO_INCREMENT,
  `question_id` int NOT NULL,
  PRIMARY KEY (`test_id`),
  KEY `question_id` (`question_id`),
  CONSTRAINT `mock_test_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `question_bank` (`question_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=140 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mock_test`
--

LOCK TABLES `mock_test` WRITE;
/*!40000 ALTER TABLE `mock_test` DISABLE KEYS */;
INSERT INTO `mock_test` VALUES (49,160),(107,160),(11,161),(35,161),(48,161),(97,161),(2,162),(34,162),(37,162),(55,162),(91,162),(13,163),(58,163),(118,163),(68,164),(115,164),(72,165),(113,165),(82,166),(136,166),(81,167),(127,167),(75,168),(131,168),(56,169),(93,169),(33,170),(42,170),(103,170),(47,171),(92,171),(59,172),(114,172),(1,173),(19,173),(62,173),(111,173),(71,174),(108,174),(14,175),(85,175),(132,175),(80,176),(125,176),(3,177),(79,177),(137,177),(31,178),(51,178),(105,178),(15,179),(53,179),(99,179),(30,180),(50,180),(95,180),(63,181),(116,181),(20,182),(61,182),(112,182),(69,183),(109,183),(4,184),(16,184),(17,184),(76,184),(135,184),(88,185),(133,185),(84,186),(138,186),(6,187),(24,187),(25,187),(29,187),(41,187),(106,187),(40,188),(104,188),(22,189),(38,189),(57,189),(100,189),(60,190),(120,190),(64,191),(119,191),(5,192),(65,192),(110,192),(8,193),(78,193),(128,193),(86,194),(134,194),(77,195),(129,195),(52,196),(101,196),(23,197),(27,197),(44,197),(96,197),(9,198),(28,198),(32,198),(46,198),(102,198),(18,199),(73,199),(122,199),(70,200),(124,200),(67,201),(123,201),(83,202),(130,202),(89,203),(139,203),(87,204),(126,204),(21,205),(26,205),(36,205),(45,205),(90,205),(43,206),(98,206),(12,207),(54,207),(94,207),(7,208),(66,208),(121,208),(10,209),(74,209),(117,209);
/*!40000 ALTER TABLE `mock_test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `performance`
--

DROP TABLE IF EXISTS `performance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `performance` (
  `performance_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `best_score` int DEFAULT NULL,
  `average_score` decimal(5,2) DEFAULT NULL,
  `total_tests` int NOT NULL,
  PRIMARY KEY (`performance_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `performance_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `performance`
--

LOCK TABLES `performance` WRITE;
/*!40000 ALTER TABLE `performance` DISABLE KEYS */;
INSERT INTO `performance` VALUES (2,1,29,1.85,26),(3,2,80,36.44,9);
/*!40000 ALTER TABLE `performance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question_bank`
--

DROP TABLE IF EXISTS `question_bank`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `question_bank` (
  `question_id` int NOT NULL AUTO_INCREMENT,
  `subject` varchar(100) DEFAULT NULL,
  `question` text NOT NULL,
  `option_a` varchar(100) DEFAULT NULL,
  `option_b` varchar(100) DEFAULT NULL,
  `option_c` varchar(100) DEFAULT NULL,
  `option_d` varchar(100) DEFAULT NULL,
  `correct_option` varchar(100) DEFAULT NULL,
  `diagram` json DEFAULT NULL,
  PRIMARY KEY (`question_id`)
) ENGINE=InnoDB AUTO_INCREMENT=210 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question_bank`
--

LOCK TABLES `question_bank` WRITE;
/*!40000 ALTER TABLE `question_bank` DISABLE KEYS */;
INSERT INTO `question_bank` VALUES (160,'Physics','What is the SI unit of force?','Newton','Joule','Watt','Pascal','Newton','{}'),(161,'Physics','What is the speed of light in vacuum?','3 x 10^8 m/s','5 x 10^6 m/s','1 x 10^7 m/s','2 x 10^9 m/s','3 x 10^8 m/s','{}'),(162,'Physics','Which law states that every action has an equal and opposite reaction?','Newton\'s First Law','Newton\'s Second Law','Newton\'s Third Law','Law of Gravitation','Newton\'s Third Law','{}'),(163,'Chemistry','What is the chemical formula of water?','H2O','CO2','O2','NaCl','H2O','{}'),(164,'Chemistry','Which gas is known as laughing gas?','Oxygen','Carbon Dioxide','Nitrous Oxide','Hydrogen','Nitrous Oxide','{}'),(165,'Chemistry','What is the pH value of pure water?','7','1','14','5','7','{}'),(166,'Maths','What is the derivative of x^2?','2x','x','x^2','0','2x','{}'),(167,'Maths','What is the integral of 1/x dx?','ln(x)','x^2','e^x','1/x','ln(x)','{}'),(168,'Maths','If a triangle has sides 3, 4, and 5, what type of triangle is it?','Scalene','Isosceles','Right-angled','Equilateral','Right-angled','{}'),(169,'Physics','What is the SI unit of force?','Newton','Joule','Watt','Pascal','Newton','{}'),(170,'Physics','What is the speed of light in vacuum?','3 x 10^8 m/s','5 x 10^6 m/s','1 x 10^7 m/s','2 x 10^9 m/s','3 x 10^8 m/s','{}'),(171,'Physics','Which law states that every action has an equal and opposite reaction?','Newton\'s First Law','Newton\'s Second Law','Newton\'s Third Law','Law of Gravitation','Newton\'s Third Law','{}'),(172,'Chemistry','What is the chemical formula of water?','H2O','CO2','O2','NaCl','H2O','{}'),(173,'Chemistry','Which gas is known as laughing gas?','Oxygen','Carbon Dioxide','Nitrous Oxide','Hydrogen','Nitrous Oxide','{}'),(174,'Chemistry','What is the pH value of pure water?','7','1','14','5','7','{}'),(175,'Maths','What is the derivative of x^2?','2x','x','x^2','0','2x','{}'),(176,'Maths','What is the integral of 1/x dx?','ln(x)','x^2','e^x','1/x','ln(x)','{}'),(177,'Maths','If a triangle has sides 3, 4, and 5, what type of triangle is it?','Scalene','Isosceles','Right-angled','Equilateral','Right-angled','{}'),(178,'Physics','What is the SI unit of force?','Newton','Joule','Watt','Pascal','Newton','{}'),(179,'Physics','What is the speed of light in vacuum?','3 x 10^8 m/s','5 x 10^6 m/s','1 x 10^7 m/s','2 x 10^9 m/s','3 x 10^8 m/s','{}'),(180,'Physics','Which law states that every action has an equal and opposite reaction?','Newton\'s First Law','Newton\'s Second Law','Newton\'s Third Law','Law of Gravitation','Newton\'s Third Law','{}'),(181,'Chemistry','What is the chemical formula of water?','H2O','CO2','O2','NaCl','H2O','{}'),(182,'Chemistry','Which gas is known as laughing gas?','Oxygen','Carbon Dioxide','Nitrous Oxide','Hydrogen','Nitrous Oxide','{}'),(183,'Chemistry','What is the pH value of pure water?','7','1','14','5','7','{}'),(184,'Maths','What is the derivative of x^2?','2x','x','x^2','0','2x','{}'),(185,'Maths','What is the integral of 1/x dx?','ln(x)','x^2','e^x','1/x','ln(x)','{}'),(186,'Maths','If a triangle has sides 3, 4, and 5, what type of triangle is it?','Scalene','Isosceles','Right-angled','Equilateral','Right-angled','{}'),(187,'Physics','What is the SI unit of force?','Newton','Joule','Watt','Pascal','Newton','{}'),(188,'Physics','What is the speed of light in vacuum?','3 x 10^8 m/s','5 x 10^6 m/s','1 x 10^7 m/s','2 x 10^9 m/s','3 x 10^8 m/s','{}'),(189,'Physics','Which law states that every action has an equal and opposite reaction?','Newton\'s First Law','Newton\'s Second Law','Newton\'s Third Law','Law of Gravitation','Newton\'s Third Law','{}'),(190,'Chemistry','What is the chemical formula of water?','H2O','CO2','O2','NaCl','H2O','{}'),(191,'Chemistry','Which gas is known as laughing gas?','Oxygen','Carbon Dioxide','Nitrous Oxide','Hydrogen','Nitrous Oxide','{}'),(192,'Chemistry','What is the pH value of pure water?','7','1','14','5','7','{}'),(193,'Maths','What is the derivative of x^2?','2x','x','x^2','0','2x','{}'),(194,'Maths','What is the integral of 1/x dx?','ln(x)','x^2','e^x','1/x','ln(x)','{}'),(195,'Maths','If a triangle has sides 3, 4, and 5, what type of triangle is it?','Scalene','Isosceles','Right-angled','Equilateral','Right-angled','{}'),(196,'Physics','What is the SI unit of force?','Newton','Joule','Watt','Pascal','Newton','{}'),(197,'Physics','What is the speed of light in vacuum?','3 x 10^8 m/s','5 x 10^6 m/s','1 x 10^7 m/s','2 x 10^9 m/s','3 x 10^8 m/s','{}'),(198,'Physics','Which law states that every action has an equal and opposite reaction?','Newton\'s First Law','Newton\'s Second Law','Newton\'s Third Law','Law of Gravitation','Newton\'s Third Law','{}'),(199,'Chemistry','What is the chemical formula of water?','H2O','CO2','O2','NaCl','H2O','{}'),(200,'Chemistry','Which gas is known as laughing gas?','Oxygen','Carbon Dioxide','Nitrous Oxide','Hydrogen','Nitrous Oxide','{}'),(201,'Chemistry','What is the pH value of pure water?','7','1','14','5','7','{}'),(202,'Maths','What is the derivative of x^2?','2x','x','x^2','0','2x','{}'),(203,'Maths','What is the integral of 1/x dx?','ln(x)','x^2','e^x','1/x','ln(x)','{}'),(204,'Maths','If a triangle has sides 3, 4, and 5, what type of triangle is it?','Scalene','Isosceles','Right-angled','Equilateral','Right-angled','{}'),(205,'Physics','What is the SI unit of force?','Newton','Joule','Watt','Pascal','Newton','{}'),(206,'Physics','What is the speed of light in vacuum?','3 x 10^8 m/s','5 x 10^6 m/s','1 x 10^7 m/s','2 x 10^9 m/s','3 x 10^8 m/s','{}'),(207,'Physics','Which law states that every action has an equal and opposite reaction?','Newton\'s First Law','Newton\'s Second Law','Newton\'s Third Law','Law of Gravitation','Newton\'s Third Law','{}'),(208,'Chemistry','What is the chemical formula of water?','H2O','CO2','O2','NaCl','H2O','{}'),(209,'Chemistry','Which gas is known as laughing gas?','Oxygen','Carbon Dioxide','Nitrous Oxide','Hydrogen','Nitrous Oxide','{}');
/*!40000 ALTER TABLE `question_bank` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` enum('student','admin') NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Nikhil Chauhan','nikhil@gmail.com','$2b$12$UuKg3UkyqV0M7nKC8EdQLOT9.5zna8.oq/dZEG72zX2FHe4cUqXcS','student'),(2,'shruti ','shruti@gmail.com','$2b$12$.UVjmLOE3CYKbkGyAoHtN.NQYg/v3Q.f8NENUU87Z9fRfzeBEtNs.','student'),(3,'Aryan Chavan','aryan@gmail.com','$2b$12$3nXVrxP9iPlENzOMNTZTIenzVaLuzfkGpGg/0H5AyI7UOutOps/7K','student'),(4,'user1','user1@gmail.com','$2b$12$xCeN6ufvrSoATEaBPnMQh.9EbUDrTpra9CtTS7nprHaShix9IULAq','admin');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-18 20:58:06
