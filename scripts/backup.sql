-- MySQL dump 10.13  Distrib 8.0.39, for Linux (x86_64)
--
-- Host: localhost    Database: ESG_db
-- ------------------------------------------------------
-- Server version	8.0.39

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
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `EID` varchar(12) NOT NULL,
  `name` varchar(255) NOT NULL,
  `gender` int NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(11) NOT NULL,
  `nation` varchar(255) NOT NULL,
  `status` int NOT NULL DEFAULT '1',
  PRIMARY KEY (`EID`),
  CONSTRAINT `check_eid_format` CHECK (regexp_like(`EID`,_utf8mb4'^02[0-9]{10}$')),
  CONSTRAINT `check_email_format` CHECK (regexp_like(`email`,_utf8mb4'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$')),
  CONSTRAINT `check_phone_format` CHECK (regexp_like(`phone`,_utf8mb4'^[0-9]+$')),
  CONSTRAINT `employees_chk_1` CHECK (((`gender` = 1) or (`gender` = 2)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES ('022020112701','aaa',2,'aaa@mail.com','0911111111','JP',1),('022021021602','mmm',1,'mmm@mail.com','0922222222','TW',1),('022021032503','ddd',1,'ddd@mail.com','0933333333','UK',1),('022021110504','www',2,'www@mail.com','0944444444','UK',1),('022022051705','iii',1,'iii@mail.com','0955555555','VE',1),('022022062106','kkk',2,'kkk@mail.com','0966666666','TW',1),('022022062707','rrr',1,'rrr@mail.com','0977777777','VE',1),('022022070508','sss',1,'sss@mail.com','0988888888','JP',1),('022023050509','fff',2,'fff@mail.com','0999999999','VE',1),('022024040210','ccc',2,'ccc@mail.com','0910101010','TW',1);
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `equipments`
--

DROP TABLE IF EXISTS `equipments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `equipments` (
  `EQID` varchar(12) NOT NULL,
  `name` varchar(255) NOT NULL,
  `amount` int NOT NULL,
  `unit` varchar(10) NOT NULL,
  `coefficient` float DEFAULT NULL,
  `purchase_date` date NOT NULL,
  `disposal_date` date NOT NULL,
  `age` int NOT NULL,
  `status` int NOT NULL DEFAULT '1',
  PRIMARY KEY (`EQID`),
  CONSTRAINT `check_eqid_format` CHECK (regexp_like(`EQID`,_utf8mb4'^03[0-9]{10}$'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipments`
--

LOCK TABLES `equipments` WRITE;
/*!40000 ALTER TABLE `equipments` DISABLE KEYS */;
INSERT INTO `equipments` VALUES ('032025070008','Equipment H',2,'pcs',NULL,'2023-07-01','2025-07-01',2,1),('032025070011','Equipment K',2,'pcs',NULL,'2024-07-20','2025-07-20',1,1),('032025110009','Equipment I',9,'pcs',NULL,'2023-11-10','2025-11-10',2,1),('032026070001','Equipment A',5,'pcs',NULL,'2020-07-15','2026-07-15',6,1),('032027070003','Equipment C',1,'pcs',NULL,'2021-07-10','2027-07-10',6,1),('032028070005','Equipment E',8,'pcs',NULL,'2022-07-15','2028-07-15',6,1),('032029010004','Equipment D',1,'pcs',NULL,'2022-01-01','2029-01-01',7,1),('032029040002','Equipment B',5,'pcs',NULL,'2021-04-01','2029-04-01',8,1),('032030020007','Equipment G',6,'pcs',NULL,'2023-02-05','2030-02-05',7,1),('032030090006','Equipment F',7,'pcs',NULL,'2022-09-01','2030-09-01',8,1),('032033020010','Equipment J',1,'pcs',NULL,'2024-02-01','2033-02-01',9,1);
/*!40000 ALTER TABLE `equipments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `materials`
--

DROP TABLE IF EXISTS `materials`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `materials` (
  `MID` varchar(14) NOT NULL,
  `name` varchar(255) NOT NULL,
  `amount` int NOT NULL,
  `unit` varchar(10) NOT NULL,
  `coefficient` float DEFAULT NULL,
  `purchase_date` date NOT NULL,
  `age` int NOT NULL,
  PRIMARY KEY (`MID`),
  CONSTRAINT `check_mid_format` CHECK (regexp_like(`MID`,_utf8mb4'^04[0-9]{12}$'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `materials`
--

LOCK TABLES `materials` WRITE;
/*!40000 ALTER TABLE `materials` DISABLE KEYS */;
INSERT INTO `materials` VALUES ('04202401010001','Material A',50,'kg',NULL,'2024-01-10',1),('04202403020002','Material B',30,'kg',NULL,'2024-03-15',2),('04202405010003','Material C',40,'kg',NULL,'2024-05-20',1),('04202406010004','Material D',25,'kg',NULL,'2024-06-25',1),('04202407010005','Material E',60,'kg',NULL,'2024-07-10',1),('04202407010007','Material G',35,'kg',NULL,'2024-07-15',1),('04202407010008','Material H',45,'kg',NULL,'2024-07-20',1),('04202407020006','Material F',55,'kg',NULL,'2024-07-13',2),('04202408010009','Material I',65,'kg',NULL,'2024-08-05',1),('04202408020010','Material J',50,'kg',NULL,'2024-08-05',2);
/*!40000 ALTER TABLE `materials` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects`
--

DROP TABLE IF EXISTS `projects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects` (
  `PID` varchar(10) NOT NULL,
  `pname` varchar(255) NOT NULL,
  `flow` mediumtext,
  `PMID` varchar(12) NOT NULL,
  PRIMARY KEY (`PID`),
  KEY `projects_ibfk_1` (`PMID`),
  CONSTRAINT `projects_ibfk_1` FOREIGN KEY (`PMID`) REFERENCES `users` (`UID`),
  CONSTRAINT `check_pid_format` CHECK (regexp_like(`PID`,_utf8mb4'^01[0-9]{6}$'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects`
--

LOCK TABLES `projects` WRITE;
/*!40000 ALTER TABLE `projects` DISABLE KEYS */;
INSERT INTO `projects` VALUES ('01240701','Project A','[\n  {\"step\": 1, \"equipments\": [\"032027070003\"], \"materials\": [\"04202403020002\"], \"description\": \"Initial setup and preparation\"},\n  {\"step\": 2, \"equipments\": [\"032029040002\", \"032028070005\", \"032025070011\"], \"materials\": [\"04202401010001\", \"04202406010004\"], \"description\": \"Processing and assembly\"},\n  {\"step\": 3, \"equipments\": [\"032030020007\"], \"materials\": [\"04202407010005\", \"\"04202407010008], \"description\": \"Final inspection and testing\"}\n]','022024040210'),('01240702','Project B','[\n  {\"step\": 1, \"equipments\": [\"032026070001\"], \"materials\": [\"\"], \"description\": \"Design and planning\"},\n  {\"step\": 2, \"equipments\": [\"032030090006\", \"032025070008\", \"032025110009\"], \"materials\": [\"04202405010003\", \"04202407020006\", \"04202407010007\", \"04202408010009\"], \"description\": \"Fabrication and construction\"},\n  {\"step\": 3, \"equipments\": [\"032033020010\"], \"materials\": [\"04202407010008\"], \"description\": \"Quality check and packaging\"},\n  {\"step\": 4, \"equipments\": [\"032030020007\"], \"materials\": [\"04202407010005\", \"04202408020010\"], \"description\": \"Final inspection and testing\"}\n]','022022070508');
/*!40000 ALTER TABLE `projects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suppliers`
--

DROP TABLE IF EXISTS `suppliers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suppliers` (
  `SID` varchar(12) NOT NULL,
  `name` varchar(255) NOT NULL,
  `phone` varchar(11) NOT NULL,
  `nation` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  PRIMARY KEY (`SID`),
  CONSTRAINT `check_sid_format` CHECK (regexp_like(`SID`,_utf8mb4'^06[0-9]{10}$')),
  CONSTRAINT `check_sphone_format` CHECK (regexp_like(`phone`,_utf8mb4'^[0-9]+$'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suppliers`
--

LOCK TABLES `suppliers` WRITE;
/*!40000 ALTER TABLE `suppliers` DISABLE KEYS */;
INSERT INTO `suppliers` VALUES ('062020010001','Supplier A','0912345678','TW','1234 Taiwan St, Taipei'),('062020010002','Supplier B','0923456789','TW','5678 Taiwan Rd, Taipei'),('062020010003','Supplier C','0934567890','TW','9101 Taiwan Ave, Kaohsiung'),('062020010004','Supplier D','0945678901','TW','2345 Taiwan Blvd, Taichung'),('062020020005','Supplier E','0956789012','TW','6789 Taiwan Ln, Tainan'),('062020020006','Supplier F','0967890123','TW','3456 Taiwan Dr, Hsinchu'),('062020100007','Supplier G','0978901234','JP','7890 Tokyo St, Shibuya'),('062020100008','Supplier H','0989012345','JP','1234 Osaka Rd, Namba'),('062020100009','Supplier I','0990123456','JP','5678 Kyoto Ave, Gion'),('062021040010','Supplier J','0901234567','TW','9101 Taoyuan St, Taoyuan'),('062021080011','Supplier K','0912345670','TW','3456 Chiayi Ln, Chiayi'),('062022030012','Supplier L','0923456781','TW','6789 Pingtung Dr, Pingtung'),('062022070013','Supplier M','0934567892','TW','9101 Yunlin Blvd, Yunlin'),('062023050014','Supplier N','0945678903','TW','1234 Hualien Ct, Hualien'),('062023050015','Supplier O','0956789014','TW','5678 Keelung Pl, Keelung');
/*!40000 ALTER TABLE `suppliers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supply`
--

DROP TABLE IF EXISTS `supply`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `supply` (
  `SID` varchar(12) NOT NULL,
  `EQID` varchar(12) DEFAULT NULL,
  `MID` varchar(14) DEFAULT NULL,
  KEY `supply_ibfk_1` (`SID`),
  KEY `supply_ibfk_2` (`EQID`),
  KEY `supply_ibfk_3` (`MID`),
  CONSTRAINT `supply_ibfk_1` FOREIGN KEY (`SID`) REFERENCES `suppliers` (`SID`),
  CONSTRAINT `supply_ibfk_2` FOREIGN KEY (`EQID`) REFERENCES `equipments` (`EQID`),
  CONSTRAINT `supply_ibfk_3` FOREIGN KEY (`MID`) REFERENCES `materials` (`MID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supply`
--

LOCK TABLES `supply` WRITE;
/*!40000 ALTER TABLE `supply` DISABLE KEYS */;
INSERT INTO `supply` VALUES ('062020010001','032025070008',NULL),('062020010002','032025070011',NULL),('062020010003','032025110009',NULL),('062020010004','032026070001',NULL),('062020020005','032027070003',NULL),('062020020006','032028070005',NULL),('062020100007','032029010004',NULL),('062020100008','032029040002',NULL),('062020100009','032030020007',NULL),('062021040010','032030090006',NULL),('062021080011','032033020010',NULL),('062020100007',NULL,'04202401010001'),('062022030012',NULL,'04202403020002'),('062020010004',NULL,'04202405010003'),('062023050014',NULL,'04202406010004'),('062020010001',NULL,'04202407010005'),('062020100009',NULL,'04202407010007'),('062021080011',NULL,'04202407010008'),('062023050015',NULL,'04202407020006'),('062020010002',NULL,'04202408010009'),('062022070013',NULL,'04202408020010'),('062020100007',NULL,'04202401010001'),('062022030012',NULL,'04202403020002'),('062020010004',NULL,'04202406010004'),('062021080011',NULL,'04202407010008'),('062023050014',NULL,'04202408020010');
/*!40000 ALTER TABLE `supply` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usage`
--

DROP TABLE IF EXISTS `usage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usage` (
  `PID` varchar(10) NOT NULL,
  `EQID` varchar(12) DEFAULT NULL,
  `MID` varchar(14) DEFAULT NULL,
  KEY `PID` (`PID`),
  KEY `usage_ibfk_2` (`EQID`),
  KEY `usage_ibfk_3` (`MID`),
  CONSTRAINT `usage_ibfk_1` FOREIGN KEY (`PID`) REFERENCES `projects` (`PID`),
  CONSTRAINT `usage_ibfk_2` FOREIGN KEY (`EQID`) REFERENCES `equipments` (`EQID`),
  CONSTRAINT `usage_ibfk_3` FOREIGN KEY (`MID`) REFERENCES `materials` (`MID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usage`
--

LOCK TABLES `usage` WRITE;
/*!40000 ALTER TABLE `usage` DISABLE KEYS */;
INSERT INTO `usage` VALUES ('01240701','032027070003',NULL),('01240701','032029040002',NULL),('01240701','032028070005',NULL),('01240701','032025070011',NULL),('01240701','032030020007',NULL),('01240702','032026070001',NULL),('01240702','032030090006',NULL),('01240702','032025070008',NULL),('01240702','032025110009',NULL),('01240702','032033020010',NULL),('01240702','032030020007',NULL),('01240701',NULL,'04202403020002'),('01240701',NULL,'04202401010001'),('01240701',NULL,'04202406010004'),('01240701',NULL,'04202407010005'),('01240701',NULL,'04202407010008'),('01240702',NULL,'04202405010003'),('01240702',NULL,'04202407020006'),('01240702',NULL,'04202407010007'),('01240702',NULL,'04202408010009'),('01240702',NULL,'04202407010008'),('01240702',NULL,'04202407010005'),('01240702',NULL,'04202408020010');
/*!40000 ALTER TABLE `usage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `UID` varchar(12) NOT NULL,
  `password` varchar(255) NOT NULL,
  `access` varchar(255) NOT NULL,
  PRIMARY KEY (`UID`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`UID`) REFERENCES `employees` (`EID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('022020112701','aaa456','01240701, 01240702'),('022022070508','sss789','01240702'),('022024040210','ccc123','01240701');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `works_on`
--

DROP TABLE IF EXISTS `works_on`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `works_on` (
  `EID` varchar(12) NOT NULL,
  `PID` varchar(10) NOT NULL,
  `position` varchar(255) NOT NULL,
  PRIMARY KEY (`EID`,`PID`),
  KEY `PID` (`PID`),
  CONSTRAINT `works_on_ibfk_1` FOREIGN KEY (`EID`) REFERENCES `employees` (`EID`),
  CONSTRAINT `works_on_ibfk_2` FOREIGN KEY (`PID`) REFERENCES `projects` (`PID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `works_on`
--

LOCK TABLES `works_on` WRITE;
/*!40000 ALTER TABLE `works_on` DISABLE KEYS */;
INSERT INTO `works_on` VALUES ('022020112701','01240701','top manager'),('022020112701','01240702','top manager'),('022021021602','01240702','Construction Technician'),('022021032503','01240701','Processing Technician'),('022021110504','01240701','Testing Specialist'),('022022051705','01240702','Packaging Specialist'),('022022062106','01240702','Design Engineer'),('022022062707','01240701','Setup Engineer'),('022022062707','01240702','Setup Engineer'),('022022070508','01240702','project manager'),('022023050509','01240702','Testing Specialist'),('022024040210','01240701','project manager');
/*!40000 ALTER TABLE `works_on` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-31 16:49:44
