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
-- Table structure for table `sentencedb`
--

DROP TABLE IF EXISTS `sentencedb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sentencedb` (
  `exerciseid` int DEFAULT NULL,
  `nopunct` varchar(300) DEFAULT NULL,
  `correctans` varchar(300) DEFAULT NULL,
  `taggedsent` varchar(300) DEFAULT NULL,
  `category` varchar(300) DEFAULT NULL,
  `level` int DEFAULT NULL,
  `displayorder` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sentencedb`
--

LOCK TABLES `sentencedb` WRITE;
/*!40000 ALTER TABLE `sentencedb` DISABLE KEYS */;
INSERT INTO `sentencedb` VALUES (0,' ',' ',' ',' ',0,' '),(1,'Do you know what Mary cooks','Do you know what Mary cooks.','Do<w>you<w>know<w>what<w>Mary<w>cooks<m>','questionmark',3,'1'),(2,'I\'d like to know where John stays','I\'d like to know where John stays.','I\'d<w>like<w>to<w>know<w>where<w>John<w>stays<m>','questionmark',3,'1'),(3,'Do you have any idea where James stays','Do you have any idea where James stays.','Do<w>you<w>have<w>any<w>idea<w>where<w>James<w>stays<m>','questionmark',3,'1'),(4,'Do you know where John stays','Do you know where John stays.','Do<w>you<w>know<w>where<w>John<w>stays<m>','questionmark',3,'1'),(5,'Could you tell me where John stays','Could you tell me where John stays?','Could<w>you<w>tell<w>me<w>where<w>John<w>stays<m>','questionmark',3,'1'),(6,'Do you know what Alice cooks','Do you know what Alice cooks.','Do<w>you<w>know<w>what<w>Alice<w>cooks<m>','questionmark',3,'1'),(7,'I\'d like to know where Alice stays','I\'d like to know where Alice stays.','I\'d<w>like<w>to<w>know<w>where<w>Alice<w>stays<m>','questionmark',3,'1'),(8,'Do you have any idea where Mary stays','Do you have any idea where Mary stays.','Do<w>you<w>have<w>any<w>idea<w>where<w>Mary<w>stays<m>','questionmark',3,'1'),(9,'Do you know where Mary stays','Do you know where Mary stays.','Do<w>you<w>know<w>where<w>Mary<w>stays<m>','questionmark',3,'1'),(10,'Could you tell me where James stays','Could you tell me where James stays?','Could<w>you<w>tell<w>me<w>where<w>James<w>stays<m>','questionmark',3,'1'),(11,'Where does James work','Where does James work?','Where<w>does<w>James<w>work<m>','questionmark',3,'1'),(12,'Where does John join','Where does John join?','Where<w>does<w>John<w>join<m>','questionmark',3,'1'),(13,'Where does James work','Where does James work?','Where<w>does<w>James<w>work<m>','questionmark',2,'1'),(14,'Where does John join','Where does John join?','Where<w>does<w>John<w>join<m>','questionmark',2,'1'),(15,'Where does Alice work','Where does Alice work?','Where<w>does<w>Alice<w>work<m>','questionmark',2,'1'),(16,'Where does Alice join','Where does Alice join?','Where<w>does<w>Alice<w>join<m>','questionmark',2,'1'),(17,'Where does Mary work','Where does Mary work?','Where<w>does<w>Mary<w>work<m>','questionmark',2,'1'),(18,'Where does James join','Where does James join?','Where<w>does<w>James<w>join<m>','questionmark',2,'1'),(19,'What does James read','What does James read?','What<w>does<w>James<w>read<m>','questionmark',2,'1'),(20,'What does John read','What does John read?','What<w>does<w>John<w>read<m>','questionmark',2,'1'),(21,'What does James read','What does James read?','What<w>does<w>James<w>read<m>','questionmark',2,'1'),(22,'What does Alice read','What does Alice read?','What<w>does<w>Alice<w>read<m>','questionmark',2,'1'),(23,'What does Alice read','What does Alice read?','What<w>does<w>Alice<w>read<m>','questionmark',2,'1'),(24,'What does Alice read','What does Alice read?','What<w>does<w>Alice<w>read<m>','questionmark',2,'1'),(25,'What does John read','What does John read?','What<w>does<w>John<w>read<m>','questionmark',2,'1'),(26,'What does Alice read','What does Alice read?','What<w>does<w>Alice<w>read<m>','questionmark',2,'1'),(27,'What does James read','What does James read?','What<w>does<w>James<w>read<m>','questionmark',2,'1'),(28,'What does Alice cook','What does Alice cook?','What<w>does<w>Alice<w>cook<m>','questionmark',2,'1'),(29,'What does Mary cook','What does Mary cook?','What<w>does<w>Mary<w>cook<m>','questionmark',2,'1'),(30,'What does James read','What does James read?','What<w>does<w>James<w>read<m>','questionmark',2,'1'),(31,'What does Alice cook','What does Alice cook?','What<w>does<w>Alice<w>cook<m>','questionmark',2,'1'),(32,'What does Mary cook','What does Mary cook?','What<w>does<w>Mary<w>cook<m>','questionmark',2,'1'),(33,'You hardly open a cage do you','You hardly open a cage, do you?','You<w>hardly<w>open<w>cage<m>do you<m>','questionmark',3,'1'),(34,'They hardly answer a question do they','They hardly answer a question, do they?','They<w>hardly<w>answer<w>question<m>do they<m>','questionmark',3,'1'),(35,'She seldom answers a question does she','She seldom answers a question, does she?','She<w>seldom<w>answers<w>question<m>does she<m>','questionmark',3,'1'),(36,'Nobody likes to close a boxdo they','Nobody likes to close a box,do they?','Nobody<w>likes<w>to<w>close<w>a<w>box<m>do they<m>','questionmark',3,'1'),(37,'None of them likes to close a boxdo they','None of them likes to close a box,do they?','None of them<w>likes<w>to<w>close<w>a<w>box<m>do they<m>','questionmark',3,'1'),(38,'You seldom read a novel do you','You seldom read a novel, do you?','You<w>seldom<w>read<w>novel<m>do you<m>','questionmark',3,'1'),(39,'You hardly read a book do you','You hardly read a book, do you?','You<w>hardly<w>read<w>book<m>do you<m>','questionmark',3,'1'),(40,'They seldom cook a biriyani do they','They seldom cook a biriyani, do they?','They<w>seldom<w>cook<w>biriyani<m>do they<m>','questionmark',3,'1'),(41,'Nobody likes to read a storydo they','Nobody likes to read a story,do they?','Nobody<w>likes<w>to<w>read<w>a<w>story<m>do they<m>','questionmark',3,'1'),(42,'Neither Mary nor James like to draw a scenarydo they','Neither Mary nor James like to draw a scenary,do they?','Neither Mary nor James<w>like<w>to<w>draw<w>a<w>scenary<m>do they<m>','questionmark',3,'1');
/*!40000 ALTER TABLE `sentencedb` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-15 22:21:40
