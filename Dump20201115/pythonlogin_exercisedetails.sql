-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: pythonlogin
-- ------------------------------------------------------
-- Server version	8.0.20

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
-- Table structure for table `exercisedetails`
--

DROP TABLE IF EXISTS `exercisedetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exercisedetails` (
  `userid` int DEFAULT NULL,
  `username` varchar(30) DEFAULT NULL,
  `exerciseid` int DEFAULT NULL,
  `correctans` varchar(100) DEFAULT NULL,
  `response1` varchar(100) DEFAULT NULL,
  `hintmsg` varchar(500) DEFAULT NULL,
  `failure` int DEFAULT NULL,
  `success` int DEFAULT NULL,
  `score` int DEFAULT '0',
  `time1` time DEFAULT NULL,
  `category` varchar(15) DEFAULT NULL,
  `levelp` int DEFAULT NULL,
  `nattempts` int DEFAULT NULL,
  `rid` int NOT NULL AUTO_INCREMENT,
  UNIQUE KEY `rid` (`rid`)
) ENGINE=InnoDB AUTO_INCREMENT=1182 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exercisedetails`
--

LOCK TABLES `exercisedetails` WRITE;
/*!40000 ALTER TABLE `exercisedetails` DISABLE KEYS */;
INSERT INTO `exercisedetails` VALUES (9,'lakshmi',1,'Major. John, a charming gentleman, could open a box ,a book and a cage.','Major John a charming gentleman could open a box a book and a cage','0',0,0,0,'22:14:48','comma',1,0,1178),(9,'lakshmi',1,'Major. John, a charming gentleman, could open a box ,a book and a cage.','Major. John a charming gentleman could open a box a book and a cage.','Correct Answer.Fullstop at appropriate place.Always put a period/fullstop after a title',0,1,0,'22:15:07','comma',1,0,1179),(9,'lakshmi',1,'Major. John, a charming gentleman, could open a box ,a book and a cage.','Major. John a charming gentleman could open a box a book and a cage.','Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP',0,1,0,'22:15:08','comma',1,0,1180),(9,'lakshmi',1,'Major. John, a charming gentleman, could open a box ,a book and a cage.','Major. John a charming gentleman could open a box a book and a cage.','Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP',0,1,0,'22:15:08','comma',1,0,1181);
/*!40000 ALTER TABLE `exercisedetails` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-15 22:21:42
