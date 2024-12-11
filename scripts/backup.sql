-- MySQL dump 10.13  Distrib 8.0.40, for Linux (x86_64)
--
-- Host: localhost    Database: ESG_db
-- ------------------------------------------------------
-- Server version	8.0.40

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=153 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add act',6,'add_act'),(22,'Can change act',6,'change_act'),(23,'Can delete act',6,'delete_act'),(24,'Can view act',6,'view_act'),(25,'Can add act fac',7,'add_actfac'),(26,'Can change act fac',7,'change_actfac'),(27,'Can delete act fac',7,'delete_actfac'),(28,'Can view act fac',7,'view_actfac'),(29,'Can add ef',8,'add_ef'),(30,'Can change ef',8,'change_ef'),(31,'Can delete ef',8,'delete_ef'),(32,'Can view ef',8,'view_ef'),(33,'Can add es',9,'add_es'),(34,'Can change es',9,'change_es'),(35,'Can delete es',9,'delete_es'),(36,'Can view es',9,'view_es'),(37,'Can add gwps',10,'add_gwps'),(38,'Can change gwps',10,'change_gwps'),(39,'Can delete gwps',10,'delete_gwps'),(40,'Can view gwps',10,'view_gwps'),(41,'Can add act',11,'add_act'),(42,'Can change act',11,'change_act'),(43,'Can delete act',11,'delete_act'),(44,'Can view act',11,'view_act'),(45,'Can add act fac',12,'add_actfac'),(46,'Can change act fac',12,'change_actfac'),(47,'Can delete act fac',12,'delete_actfac'),(48,'Can view act fac',12,'view_actfac'),(49,'Can add ef',13,'add_ef'),(50,'Can change ef',13,'change_ef'),(51,'Can delete ef',13,'delete_ef'),(52,'Can view ef',13,'view_ef'),(53,'Can add es',14,'add_es'),(54,'Can change es',14,'change_es'),(55,'Can delete es',14,'delete_es'),(56,'Can view es',14,'view_es'),(57,'Can add gwps',15,'add_gwps'),(58,'Can change gwps',15,'change_gwps'),(59,'Can delete gwps',15,'delete_gwps'),(60,'Can view gwps',15,'view_gwps'),(61,'Can add session',16,'add_session'),(62,'Can change session',16,'change_session'),(63,'Can delete session',16,'delete_session'),(64,'Can view session',16,'view_session'),(65,'Can add employee',17,'add_employee'),(66,'Can change employee',17,'change_employee'),(67,'Can delete employee',17,'delete_employee'),(68,'Can view employee',17,'view_employee'),(69,'Can add equipment',18,'add_equipment'),(70,'Can change equipment',18,'change_equipment'),(71,'Can delete equipment',18,'delete_equipment'),(72,'Can view equipment',18,'view_equipment'),(73,'Can add material',19,'add_material'),(74,'Can change material',19,'change_material'),(75,'Can delete material',19,'delete_material'),(76,'Can view material',19,'view_material'),(77,'Can add project',20,'add_project'),(78,'Can change project',20,'change_project'),(79,'Can delete project',20,'delete_project'),(80,'Can view project',20,'view_project'),(81,'Can add supplier',21,'add_supplier'),(82,'Can change supplier',21,'change_supplier'),(83,'Can delete supplier',21,'delete_supplier'),(84,'Can view supplier',21,'view_supplier'),(85,'Can add user',22,'add_user'),(86,'Can change user',22,'change_user'),(87,'Can delete user',22,'delete_user'),(88,'Can view user',22,'view_user'),(89,'Can add usage',23,'add_usage'),(90,'Can change usage',23,'change_usage'),(91,'Can delete usage',23,'delete_usage'),(92,'Can view usage',23,'view_usage'),(93,'Can add supply',24,'add_supply'),(94,'Can change supply',24,'change_supply'),(95,'Can delete supply',24,'delete_supply'),(96,'Can view supply',24,'view_supply'),(97,'Can add works on',25,'add_workson'),(98,'Can change works on',25,'change_workson'),(99,'Can delete works on',25,'delete_workson'),(100,'Can view works on',25,'view_workson'),(101,'Can add usage m',26,'add_usagem'),(102,'Can change usage m',26,'change_usagem'),(103,'Can delete usage m',26,'delete_usagem'),(104,'Can view usage m',26,'view_usagem'),(105,'Can add usage eq',27,'add_usageeq'),(106,'Can change usage eq',27,'change_usageeq'),(107,'Can delete usage eq',27,'delete_usageeq'),(108,'Can view usage eq',27,'view_usageeq'),(109,'Can add boundary',28,'add_boundary'),(110,'Can change boundary',28,'change_boundary'),(111,'Can delete boundary',28,'delete_boundary'),(112,'Can view boundary',28,'view_boundary'),(113,'Can add emission',29,'add_emission'),(114,'Can change emission',29,'change_emission'),(115,'Can delete emission',29,'delete_emission'),(116,'Can view emission',29,'view_emission'),(117,'Can add gas',30,'add_gas'),(118,'Can change gas',30,'change_gas'),(119,'Can delete gas',30,'delete_gas'),(120,'Can view gas',30,'view_gas'),(121,'Can add record',31,'add_record'),(122,'Can change record',31,'change_record'),(123,'Can delete record',31,'delete_record'),(124,'Can view record',31,'view_record'),(125,'Can add source',32,'add_source'),(126,'Can change source',32,'change_source'),(127,'Can delete source',32,'delete_source'),(128,'Can view source',32,'view_source'),(129,'Can add daily record',33,'add_dailyrecord'),(130,'Can change daily record',33,'change_dailyrecord'),(131,'Can delete daily record',33,'delete_dailyrecord'),(132,'Can view daily record',33,'view_dailyrecord'),(133,'Can add daily record modified',34,'add_dailyrecordmodified'),(134,'Can change daily record modified',34,'change_dailyrecordmodified'),(135,'Can delete daily record modified',34,'delete_dailyrecordmodified'),(136,'Can view daily record modified',34,'view_dailyrecordmodified'),(137,'Can add green house gas',35,'add_greenhousegas'),(138,'Can change green house gas',35,'change_greenhousegas'),(139,'Can delete green house gas',35,'delete_greenhousegas'),(140,'Can view green house gas',35,'view_greenhousegas'),(141,'Can add ppn',36,'add_ppn'),(142,'Can change ppn',36,'change_ppn'),(143,'Can delete ppn',36,'delete_ppn'),(144,'Can view ppn',36,'view_ppn'),(145,'Can add repair log',37,'add_repairlog'),(146,'Can change repair log',37,'change_repairlog'),(147,'Can delete repair log',37,'delete_repairlog'),(148,'Can view repair log',37,'view_repairlog'),(149,'Can add resource',38,'add_resource'),(150,'Can change resource',38,'change_resource'),(151,'Can delete resource',38,'delete_resource'),(152,'Can view resource',38,'view_resource');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$dpWMPZKV8W5M16NdQvrhnd$WRqM8iiKe7wxGWF9dcyEWew0R3fTXIqM/kRwbW8PE1M=',NULL,0,'test1','','','',0,1,'2024-08-05 08:11:27.365692');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `boundary`
--

DROP TABLE IF EXISTS `boundary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `boundary` (
  `BID` varchar(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `type` varchar(100) NOT NULL,
  `created_by` varchar(12) NOT NULL,
  `created_date` date NOT NULL,
  `last_modified_by` varchar(12) NOT NULL,
  `last_modified_date` date NOT NULL,
  PRIMARY KEY (`BID`),
  KEY `boundary_ibfk_1` (`created_by`),
  KEY `boundary_ibfk_2` (`last_modified_by`),
  CONSTRAINT `boundary_ibfk_1` FOREIGN KEY (`created_by`) REFERENCES `employees` (`EID`),
  CONSTRAINT `boundary_ibfk_2` FOREIGN KEY (`last_modified_by`) REFERENCES `employees` (`EID`),
  CONSTRAINT `check_bid_format` CHECK (regexp_like(`BID`,_utf8mb4'^04[0-9]{9}$'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `boundary`
--

LOCK TABLES `boundary` WRITE;
/*!40000 ALTER TABLE `boundary` DISABLE KEYS */;
INSERT INTO `boundary` VALUES ('04116011003','綠韻茶坊','臺北市文山區指南路三段40巷8號','茶田','022024010004','2024-01-01','022024010004','2024-01-01'),('04221027001','茶香樓','新北市汐止區忠孝東路104號1樓','辦公室','022024010004','2024-01-01','022024010004','2024-01-01'),('04236001002','翠葉工場','新北市土城區擺接堡路1號1樓','加工廠','022024010004','2024-01-01','022024010004','2024-01-01');
/*!40000 ALTER TABLE `boundary` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `daily_record`
--

DROP TABLE IF EXISTS `daily_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `daily_record` (
  `dailyID` int NOT NULL AUTO_INCREMENT,
  `PID` varchar(10) NOT NULL,
  `PN` varchar(6) NOT NULL,
  `date` date NOT NULL,
  `runtime` float DEFAULT NULL,
  `amount` float NOT NULL,
  `unit` varchar(10) NOT NULL,
  `current_factor` float NOT NULL,
  `created_by` varchar(12) NOT NULL,
  `created_date` date NOT NULL,
  `last_modified_by` varchar(12) NOT NULL,
  `last_modified_date` date NOT NULL,
  PRIMARY KEY (`dailyID`),
  KEY `daily_record_ibfk_1` (`PID`),
  KEY `daily_record_ibfk_2` (`PN`),
  KEY `daily_record_ibfk_3` (`created_by`),
  KEY `daily_record_ibfk_4` (`last_modified_by`),
  CONSTRAINT `daily_record_ibfk_1` FOREIGN KEY (`PID`) REFERENCES `projects` (`PID`),
  CONSTRAINT `daily_record_ibfk_2` FOREIGN KEY (`PN`) REFERENCES `product_part_number` (`PN`),
  CONSTRAINT `daily_record_ibfk_3` FOREIGN KEY (`created_by`) REFERENCES `employees` (`EID`),
  CONSTRAINT `daily_record_ibfk_4` FOREIGN KEY (`last_modified_by`) REFERENCES `employees` (`EID`)
) ENGINE=InnoDB AUTO_INCREMENT=70 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `daily_record`
--

LOCK TABLES `daily_record` WRITE;
/*!40000 ALTER TABLE `daily_record` DISABLE KEYS */;
INSERT INTO `daily_record` VALUES (1,'01240105','060021','2024-01-05',3.5,2,'台',0.8,'022024010003','2024-01-05','022024010003','2024-01-05'),(2,'01240105','060016','2024-01-06',NULL,1,'袋',0.65,'022024010003','2024-01-06','022024010003','2024-01-06'),(3,'01240105','060018','2024-01-07',NULL,1,'袋',0.63,'022024010003','2024-01-07','022024010003','2024-01-07'),(4,'01240105','060023','2024-01-08',NULL,4,'袋',0.58,'022024010003','2024-01-08','022024010003','2024-01-08'),(5,'01240105','060022','2024-01-09',NULL,1,'項',0.59,'022024010003','2024-01-09','022024010003','2024-01-09'),(6,'01240105','060025','2024-01-10',2,1,'度',0.156,'022024010003','2024-01-10','022024010003','2024-01-10'),(7,'01240105','060021','2024-01-12',3.5,2,'台',0.8,'022024010003','2024-01-12','022024010003','2024-01-12'),(8,'01240105','060016','2024-01-13',NULL,1,'袋',0.65,'022024010003','2024-01-13','022024010003','2024-01-13'),(9,'01240105','060018','2024-01-14',NULL,1,'袋',0.63,'022024010003','2024-01-14','022024010003','2024-01-14'),(10,'01240105','060023','2024-01-15',NULL,4,'袋',0.58,'022024010003','2024-01-15','022024010003','2024-01-15'),(11,'01240105','060022','2024-01-16',NULL,1,'項',0.59,'022024010003','2024-01-16','022024010003','2024-01-16'),(12,'01240105','060025','2024-01-17',2,1,'度',0.156,'022024010003','2024-01-17','022024010003','2024-01-17'),(13,'01240105','060021','2024-02-05',3.5,2,'台',0.8,'022024010003','2024-02-05','022024010003','2024-02-05'),(14,'01240105','060016','2024-02-06',NULL,1,'袋',0.65,'022024010003','2024-02-06','022024010003','2024-02-06'),(15,'01240105','060018','2024-02-07',NULL,1,'袋',0.63,'022024010003','2024-02-07','022024010003','2024-02-07'),(16,'01240105','060023','2024-02-08',NULL,4,'袋',0.58,'022024010003','2024-02-08','022024010003','2024-02-08'),(17,'01240105','060022','2024-02-09',NULL,1,'項',0.59,'022024010003','2024-02-09','022024010003','2024-02-09'),(18,'01240105','060025','2024-02-10',2,1,'度',0.156,'022024010003','2024-02-10','022024010003','2024-02-10'),(19,'01240106','060001','2024-04-01',4,1,'台',0.8,'022024010003','2024-04-01','022024010003','2024-04-01'),(20,'01240106','060002','2024-04-01',4.5,1,'台',0.79,'022024010003','2024-04-01','022024010003','2024-04-01'),(21,'01240106','060003','2024-04-01',NULL,2,'項',0.78,'022024010003','2024-04-01','022024010003','2024-04-01'),(22,'01240106','060001','2024-04-05',4,1,'台',0.8,'022024010003','2024-04-05','022024010003','2024-04-05'),(23,'01240106','060002','2024-04-05',4.5,1,'台',0.79,'022024010003','2024-04-05','022024010003','2024-04-05'),(24,'01240106','060003','2024-04-05',NULL,2,'項',0.78,'022024010003','2024-04-05','022024010003','2024-04-05'),(25,'01240106','060001','2024-04-10',4,1,'台',0.8,'022024010003','2024-04-10','022024010003','2024-04-10'),(26,'01240106','060002','2024-04-10',4.5,1,'台',0.79,'022024010003','2024-04-10','022024010003','2024-04-10'),(27,'01240106','060003','2024-04-10',NULL,2,'項',0.78,'022024010003','2024-04-10','022024010003','2024-04-10'),(28,'01240106','060001','2024-04-15',4,1,'台',0.8,'022024010003','2024-04-15','022024010003','2024-04-15'),(29,'01240106','060002','2024-04-15',4.5,1,'台',0.79,'022024010003','2024-04-15','022024010003','2024-04-15'),(30,'01240106','060003','2024-04-15',NULL,2,'項',0.78,'022024010003','2024-04-15','022024010003','2024-04-15'),(31,'01240106','060001','2024-04-20',4,1,'台',0.8,'022024010003','2024-04-20','022024010003','2024-04-20'),(32,'01240106','060002','2024-04-20',4.5,1,'台',0.79,'022024010003','2024-04-20','022024010003','2024-04-20'),(33,'01240106','060003','2024-04-20',NULL,2,'項',0.78,'022024010003','2024-04-20','022024010003','2024-04-20'),(34,'01240106','060001','2024-04-25',4,1,'台',0.8,'022024010003','2024-04-25','022024010003','2024-04-25'),(35,'01240106','060002','2024-04-25',4.5,1,'台',0.79,'022024010003','2024-04-25','022024010003','2024-04-25'),(36,'01240106','060003','2024-04-25',NULL,2,'項',0.78,'022024010003','2024-04-25','022024010003','2024-04-25'),(37,'01240106','060001','2024-05-01',4,1,'台',0.8,'022024010003','2024-05-01','022024010003','2024-05-01'),(38,'01240106','060002','2024-05-01',4.5,1,'台',0.79,'022024010003','2024-05-01','022024010003','2024-05-01'),(39,'01240106','060003','2024-05-01',NULL,2,'項',0.78,'022024010003','2024-05-01','022024010003','2024-05-01'),(40,'01240107','060005','2024-04-01',5,1,'台',0.76,'022024010004','2024-04-01','022024010004','2024-04-01'),(41,'01240107','060007','2024-04-04',6,1,'台',0.74,'022024010004','2024-04-04','022024010004','2024-04-04'),(42,'01240107','060008','2024-04-07',3.5,1,'台',0.73,'022024010004','2024-04-07','022024010004','2024-04-07'),(43,'01240107','060009','2024-04-10',4.5,1,'台',0.72,'022024010004','2024-04-10','022024010004','2024-04-10'),(44,'01240107','060013','2024-04-13',6,1,'台',0.71,'022024010004','2024-04-13','022024010004','2024-04-13'),(45,'01240107','060005','2024-04-16',5,1,'台',0.76,'022024010004','2024-04-16','022024010004','2024-04-16'),(46,'01240107','060007','2024-05-02',6,1,'台',0.74,'022024010004','2024-05-02','022024010004','2024-05-02'),(47,'01240107','060008','2024-05-05',3.5,1,'台',0.73,'022024010004','2024-05-05','022024010004','2024-05-05'),(48,'01240107','060009','2024-05-08',4.5,1,'台',0.72,'022024010004','2024-05-08','022024010004','2024-05-08'),(49,'01240107','060013','2024-05-11',6,1,'台',0.71,'022024010004','2024-05-11','022024010004','2024-05-11'),(50,'01240107','060005','2024-05-14',5,1,'台',0.76,'022024010004','2024-05-14','022024010004','2024-05-14'),(51,'01240107','060007','2024-05-17',6,1,'台',0.74,'022024010004','2024-05-17','022024010004','2024-05-17'),(52,'01240107','060008','2024-06-02',3.5,1,'台',0.73,'022024010004','2024-06-02','022024010004','2024-06-02'),(53,'01240107','060009','2024-06-05',4.5,1,'台',0.72,'022024010004','2024-06-05','022024010004','2024-06-05'),(54,'01240107','060013','2024-06-08',6,1,'台',0.71,'022024010004','2024-06-08','022024010004','2024-06-08'),(55,'01240107','060005','2024-06-11',5,1,'台',0.76,'022024010004','2024-06-11','022024010004','2024-06-11'),(56,'01240107','060007','2024-06-14',6,1,'台',0.74,'022024010004','2024-06-14','022024010004','2024-06-14'),(57,'01240107','060008','2024-06-17',3.5,1,'台',0.73,'022024010004','2024-06-17','022024010004','2024-06-17'),(58,'01240107','060009','2024-07-02',4.5,1,'台',0.72,'022024010004','2024-07-02','022024010004','2024-07-02'),(59,'01240107','060013','2024-07-05',6,1,'台',0.71,'022024010004','2024-07-05','022024010004','2024-07-05'),(60,'01240107','060005','2024-07-08',5,1,'台',0.76,'022024010004','2024-07-08','022024010004','2024-07-08'),(61,'01240107','060007','2024-07-11',6,1,'台',0.74,'022024010004','2024-07-11','022024010004','2024-07-11'),(62,'01240107','060008','2024-07-14',3.5,1,'台',0.73,'022024010004','2024-07-14','022024010004','2024-07-14'),(63,'01240107','060009','2024-07-17',4.5,1,'台',0.72,'022024010004','2024-07-17','022024010004','2024-07-17'),(64,'01240107','060013','2024-08-02',6,1,'台',0.71,'022024010004','2024-08-02','022024010004','2024-08-02'),(65,'01240107','060005','2024-08-05',5,1,'台',0.76,'022024010004','2024-08-05','022024010004','2024-08-05'),(66,'01240107','060007','2024-08-08',6,1,'台',0.74,'022024010004','2024-08-08','022024010004','2024-08-08'),(67,'01240107','060008','2024-08-11',3.5,1,'台',0.73,'022024010004','2024-08-11','022024010004','2024-08-11'),(68,'01240107','060009','2024-08-14',4.5,1,'台',0.72,'022024010004','2024-08-14','022024010004','2024-08-14'),(69,'01240107','060013','2024-08-17',6,1,'台',0.71,'022024010004','2024-08-17','022024010004','2024-08-17');
/*!40000 ALTER TABLE `daily_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `daily_record_modified`
--

DROP TABLE IF EXISTS `daily_record_modified`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `daily_record_modified` (
  `dailyID_modified` int NOT NULL,
  `dailyID_origin` int NOT NULL,
  `PID` varchar(10) NOT NULL,
  `PN` varchar(6) NOT NULL,
  `date` date NOT NULL,
  `runtime` float DEFAULT NULL,
  `amount` float NOT NULL,
  `unit` varchar(10) NOT NULL,
  `current_factor` float NOT NULL,
  `created_by` varchar(12) NOT NULL,
  `created_date` date NOT NULL,
  `status` int NOT NULL,
  PRIMARY KEY (`dailyID_modified`),
  KEY `daily_record_modified_ibfk_1` (`PID`),
  KEY `daily_record_modified_ibfk_2` (`PN`),
  KEY `daily_record_modified_ibfk_3` (`created_by`),
  KEY `daily_record_modified_ibfk_4` (`dailyID_origin`),
  CONSTRAINT `daily_record_modified_ibfk_1` FOREIGN KEY (`PID`) REFERENCES `projects` (`PID`),
  CONSTRAINT `daily_record_modified_ibfk_2` FOREIGN KEY (`PN`) REFERENCES `product_part_number` (`PN`),
  CONSTRAINT `daily_record_modified_ibfk_3` FOREIGN KEY (`created_by`) REFERENCES `employees` (`EID`),
  CONSTRAINT `daily_record_modified_ibfk_4` FOREIGN KEY (`dailyID_origin`) REFERENCES `daily_record` (`dailyID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `daily_record_modified`
--

LOCK TABLES `daily_record_modified` WRITE;
/*!40000 ALTER TABLE `daily_record_modified` DISABLE KEYS */;
/*!40000 ALTER TABLE `daily_record_modified` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'helloworld','act'),(7,'helloworld','actfac'),(8,'helloworld','ef'),(9,'helloworld','es'),(10,'helloworld','gwps'),(11,'login','act'),(12,'login','actfac'),(13,'login','ef'),(14,'login','es'),(15,'login','gwps'),(28,'pm','boundary'),(33,'pm','dailyrecord'),(34,'pm','dailyrecordmodified'),(29,'pm','emission'),(17,'pm','employee'),(18,'pm','equipment'),(30,'pm','gas'),(35,'pm','greenhousegas'),(19,'pm','material'),(36,'pm','ppn'),(20,'pm','project'),(31,'pm','record'),(37,'pm','repairlog'),(38,'pm','resource'),(32,'pm','source'),(21,'pm','supplier'),(24,'pm','supply'),(23,'pm','usage'),(27,'pm','usageeq'),(26,'pm','usagem'),(22,'pm','user'),(25,'pm','workson'),(16,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-08-02 07:24:19.672000'),(2,'auth','0001_initial','2024-08-02 07:24:20.707217'),(3,'admin','0001_initial','2024-08-02 07:24:20.939531'),(4,'admin','0002_logentry_remove_auto_add','2024-08-02 07:24:20.954980'),(5,'admin','0003_logentry_add_action_flag_choices','2024-08-02 07:24:20.978110'),(6,'contenttypes','0002_remove_content_type_name','2024-08-02 07:24:21.110089'),(7,'auth','0002_alter_permission_name_max_length','2024-08-02 07:24:21.212032'),(8,'auth','0003_alter_user_email_max_length','2024-08-02 07:24:21.259136'),(9,'auth','0004_alter_user_username_opts','2024-08-02 07:24:21.281122'),(10,'auth','0005_alter_user_last_login_null','2024-08-02 07:24:21.376793'),(11,'auth','0006_require_contenttypes_0002','2024-08-02 07:24:21.385533'),(12,'auth','0007_alter_validators_add_error_messages','2024-08-02 07:24:21.409542'),(13,'auth','0008_alter_user_username_max_length','2024-08-02 07:24:21.525911'),(14,'auth','0009_alter_user_last_name_max_length','2024-08-02 07:24:21.633259'),(15,'auth','0010_alter_group_name_max_length','2024-08-02 07:24:21.677381'),(16,'auth','0011_update_proxy_permissions','2024-08-02 07:24:21.698053'),(17,'auth','0012_alter_user_first_name_max_length','2024-08-02 07:24:21.803437'),(18,'helloworld','0001_initial','2024-08-02 07:24:21.817863'),(19,'login','0001_initial','2024-08-02 07:24:21.840660'),(20,'pm','0001_initial','2024-08-07 05:53:11.943703'),(21,'pm','0002_usage_amount_usage_unit','2024-08-07 06:03:57.626789'),(22,'sessions','0001_initial','2024-08-07 06:03:57.772434'),(23,'pm','0003_usage_amount_usage_unit','2024-08-08 07:20:46.140220'),(24,'ESG','0001_initial','2024-10-09 09:33:26.761191'),(25,'ESG','0002_alter_source_table','2024-10-09 09:33:26.801066'),(26,'ESG','0003_delete_equipment_delete_material_delete_boundary_and_more','2024-10-09 09:33:26.939790');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emission`
--

DROP TABLE IF EXISTS `emission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `emission` (
  `emissionID` int NOT NULL,
  `RID` varchar(14) NOT NULL,
  `GID` int NOT NULL,
  `amount_kg` float NOT NULL,
  PRIMARY KEY (`emissionID`),
  UNIQUE KEY `unique_emission` (`RID`,`GID`),
  KEY `emission_ibfk_1` (`GID`),
  CONSTRAINT `emission_ibfk_1` FOREIGN KEY (`GID`) REFERENCES `green_house_gas` (`GID`),
  CONSTRAINT `emission_ibfk_2` FOREIGN KEY (`RID`) REFERENCES `resource` (`RID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emission`
--

LOCK TABLES `emission` WRITE;
/*!40000 ALTER TABLE `emission` DISABLE KEYS */;
INSERT INTO `emission` VALUES (1,'03202306050001',1,0.55),(2,'03202306050001',2,0.01),(3,'03202306050002',1,0.54),(4,'03202306050002',2,0.01),(5,'03202305050003',1,0.51),(6,'03202305050003',2,0.01),(7,'03202305050004',2,0.02),(8,'03202305050004',1,0.24),(9,'03202304050005',1,0.69),(10,'03202305010006',1,0.046),(11,'03202305010006',3,0.003),(12,'03202305010007',1,0.045),(13,'03202305010007',3,0.003),(14,'03202306010008',1,0.043),(15,'03202306010008',3,0.003),(16,'03202306010009',1,0.047),(17,'03202306010009',3,0.003),(18,'03202304050010',1,0.25),(19,'03202304050010',2,0.02),(20,'03202306050011',1,0.18),(21,'03202306050011',2,0.02),(22,'03202304050012',1,0.23),(23,'03202304050012',2,0.02),(24,'03202306010013',1,0.66),(25,'03202306010014',3,0.003),(26,'03202306010014',1,0.043),(27,'03202306010015',1,0.042),(28,'03202306010015',3,0.003),(29,'03202305050016',1,0.11),(30,'03202305050016',2,0.02),(31,'03202306070017',1,0.494),(32,'03202306070018',1,0.156);
/*!40000 ALTER TABLE `emission` ENABLE KEYS */;
UNLOCK TABLES;

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
INSERT INTO `employees` VALUES ('022024010001','趙海琉',2,'kairu@email.com','0912345678','Taiwan',1),('022024010002','北川拓實',1,'takumi@email.com','0918765432','Japan',1),('022024010003','織山尚大',2,'shouta@email.com','0923456789','Japan',1),('022024010004','李皇輝',2,'konki@email.com','0934567890','Taiwan',1),('022024010005','平塚翔馬',1,'shouma@email.com','0945678901','Japan',0),('022024010006','安嶹秀生',1,'hideki@email.com','0956789012','Japan',1),('022024010007','元木湧',1,'waku@email.com','0967890123','Japan',1),('022024010008','王颯太',2,'souta@email.com','0978901234','Taiwan',1),('022024010009','深田龍生',2,'ryusei@email.com','0989012345','Japan',1),('022024010010','檜山光成',1,'kousei@email.com','0990123456','Japan',1),('022024010011','青木滉平',1,'kouhei@email.com','0912345689','Japan',1),('022024010012','衛陸人',1,'rikuto@email.com','0923456790','Taiwan',1),('022024010013','蔣將聖',1,'shousei@email.com','0934567801','Taiwan',1),('022024040014','沈廉',2,'ren@email.com','0945678912','Taiwan',1),('022024040015','山井飛翔',2,'tsubasa@email.com','0956789023','Japan',1),('022024040016','瀧陽次郎',1,'yojiro@email.com','0967890134','Japan',1),('022024080017','朱悠仁',1,'yujin@email.com','0978901245','Taiwan',1),('022024080018','秦星輝',2,'hoshki@email.com','0989012356','Taiwan',1),('022024110019','長瀨結星',2,'yousei@email.com','0990123467','Japan',1),('022024110020','許涉',1,'wataru@email.com','0912345790','Taiwan',1);
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `green_house_gas`
--

DROP TABLE IF EXISTS `green_house_gas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `green_house_gas` (
  `GID` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `gwp` float NOT NULL,
  PRIMARY KEY (`GID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `green_house_gas`
--

LOCK TABLES `green_house_gas` WRITE;
/*!40000 ALTER TABLE `green_house_gas` DISABLE KEYS */;
INSERT INTO `green_house_gas` VALUES (1,'二氧化碳',1),(2,'甲烷',25),(3,'氧化亞氮',198),(4,'氫氟碳化物',14800),(5,'全氟碳化物',17700),(6,'六氟化物',22800),(7,'三氟化物',17200);
/*!40000 ALTER TABLE `green_house_gas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_part_number`
--

DROP TABLE IF EXISTS `product_part_number`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_part_number` (
  `PN` varchar(6) NOT NULL,
  `name` varchar(255) NOT NULL,
  `total_amount` int NOT NULL,
  `unit` varchar(20) DEFAULT NULL,
  `average_factor` float NOT NULL,
  PRIMARY KEY (`PN`),
  CONSTRAINT `check_pn_format` CHECK (regexp_like(`PN`,_utf8mb4'^06[0-9]{4}$'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_part_number`
--

LOCK TABLES `product_part_number` WRITE;
/*!40000 ALTER TABLE `product_part_number` DISABLE KEYS */;
INSERT INTO `product_part_number` VALUES ('060001','單人式採茶機',1,'台',0.8),('060002','雙人式採茶機',1,'台',0.79),('060003','人工採摘工具',10,'項',0.78),('060004','日光萎凋：自然陽光、攤曬工具',0,'項',0.77),('060005','熱風萎凋機',1,'台',0.76),('060006','室內萎凋設備：冷氣機、浪菁機',1,'台',0.75),('060007','炒菁機',1,'台',0.74),('060008','揉捻機（手動與電動）',2,'台',0.73),('060009','初乾機',3,'台',0.72),('060010','烘乾設備',0,'台',0.71),('060011','蓮花機',0,'台',0.7),('060012','平揉機',1,'台',0.69),('060013','箱型乾燥機（焙茶機）',1,'台',0.68),('060014','抽氣風扇',0,'台',0.67),('060015','日光燈',4,'盞',0.66),('060016','化肥（氮磷鉀）',10,'袋',0.65),('060017','有機肥',8,'袋',0.64),('060018','農藥（非有機）',5,'袋',0.63),('060019','有機除蟲劑（蘇力菌、白殭菌）',2,'袋',0.62),('060020','除草機',1,'台',0.61),('060021','翻土機',4,'台',0.6),('060022','修剪工具',10,'項',0.59),('060023','堆肥',40,'袋',0.58),('060024','電力',0,'度',0.494),('060025','自來水',0,'度',0.156);
/*!40000 ALTER TABLE `product_part_number` ENABLE KEYS */;
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
  `BID` varchar(11) NOT NULL,
  PRIMARY KEY (`PID`),
  KEY `projects_ibfk_2` (`BID`),
  KEY `projects_ibfk_1` (`PMID`),
  CONSTRAINT `projects_ibfk_1` FOREIGN KEY (`PMID`) REFERENCES `employees` (`EID`),
  CONSTRAINT `projects_ibfk_2` FOREIGN KEY (`BID`) REFERENCES `boundary` (`BID`),
  CONSTRAINT `check_pid_format` CHECK (regexp_like(`PID`,_utf8mb4'^01[0-9]{6}$'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects`
--

LOCK TABLES `projects` WRITE;
/*!40000 ALTER TABLE `projects` DISABLE KEYS */;
INSERT INTO `projects` VALUES ('01240101','包種茶種植','','022024040014','04116011003'),('01240102','包種茶採收','','022024040014','04116011003'),('01240103','包種茶加工','','022024010004','04236001002'),('01240104','包種茶包裝','','022024010004','04236001002'),('01240105','鐵觀音種植','[\n    {\"step\": 1, \"equipments\": [{\"PN\": \"060021\", \"amount\": 2, \"unit\": \"台\"}], \"materials\": [], \"description\": \"土地準備：土地翻耕\"}, \n    {\"step\": 2, , \"equipments\": [], \"materials\": [{\"PN\": \"060016\", \"amount\": 1, \"unit\": \"袋\"},{\"PN\": \"060018\", \"amount\": 1, \"unit\": \"袋\"},{\"PN\": \"060023\", \"amount\": 4, \"unit\": \"袋\"}], \"description\": \"施用化肥與有機肥料\"}, \n    {\"step\": 3, , \"equipments\": [], \"materials\": [{\"PN\": \"060025\", \"amount\": 1, \"unit\": \"度\"}], \"description\": \"灌溉與水分管理\"}, \n    {\"step\": 4, , \"equipments\": [{\"PN\": \"060022\", \"amount\": 1, \"unit\": \"項\"}], \"materials\": [], \"description\": \"茶樹修剪與管理\"}\n]','022024010003','04116011003'),('01240106','鐵觀音採收','[\n    {\"step\": 1, \"equipments\": [{\"PN\": \"060001\", \"amount\": 1, \"unit\": \"台\"},{\"PN\": \"060002\", \"amount\": 1, \"unit\": \"台\"},{\"PN\": \"060003\", \"amount\": 2, \"unit\": \"項\"}], \"materials\": [], \"description\": \"採摘茶葉\"}, \n    {\"step\": 2, , \"equipments\": [], \"materials\": [], \"description\": \"篩選與分級\"}\n]','022024010003','04116011003'),('01240107','鐵觀音加工','[\n    {\"step\": 1, \"equipments\": [{\"PN\": \"060005\", \"amount\": 1, \"unit\": \"台\"}], \"materials\": [], \"description\": \"熱風萎凋\"}, \n    {\"step\": 2, , \"equipments\": [{\"PN\": \"060007\", \"amount\": 1, \"unit\": \"台\"}], \"materials\": [], \"description\": \"炒菁（殺青）階段\"}, \n    {\"step\": 3, , \"equipments\": [{\"PN\": \"060008\", \"amount\": 1, \"unit\": \"台\"}], \"materials\": [], \"description\": \"揉捻茶葉\"}, \n    {\"step\": 4, , \"equipments\": [{\"PN\": \"060009\", \"amount\": 1, \"unit\": \"台\"}], \"materials\": [], \"description\": \"初乾燥階段\"}, \n    {\"step\": 5, , \"equipments\": [{\"PN\": \"060013\", \"amount\": 1, \"unit\": \"台\"}], \"materials\": [], \"description\": \"焙茶（烘乾）\"}\n]','022024010004','04236001002'),('01240108','鐵觀音包裝','','022024010004','04236001002'),('01240109','銷售','','022024040015','04221027001');
/*!40000 ALTER TABLE `projects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `repair_log`
--

DROP TABLE IF EXISTS `repair_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `repair_log` (
  `repairID` int NOT NULL AUTO_INCREMENT,
  `RID` varchar(14) NOT NULL,
  `date` date NOT NULL,
  `notes` mediumtext,
  PRIMARY KEY (`repairID`),
  KEY `repair_log_ibfk_1` (`RID`),
  CONSTRAINT `repair_log_ibfk_1` FOREIGN KEY (`RID`) REFERENCES `resource` (`RID`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `repair_log`
--

LOCK TABLES `repair_log` WRITE;
/*!40000 ALTER TABLE `repair_log` DISABLE KEYS */;
INSERT INTO `repair_log` VALUES (1,'03202304050005','2024-04-10','年度定期檢修，檢查所有運作機構，無異常發現。'),(2,'03202304050010','2024-04-10','年度定期檢修，檢查萎凋功能，調整乾燥速率。'),(3,'03202304050012','2024-04-10','年度檢修，檢查電動揉捻機運轉是否正常。'),(4,'03202305050003','2024-05-15','年度定期檢修，檢查熱風萎凋機風速和溫度調節系統。'),(5,'03202305050004','2024-05-15','年度定期檢修，檢查炒菁機電動控制系統及溫控系統。'),(6,'03202305050016','2024-05-15','年度檢修，檢查除草機運行狀況及油量。'),(7,'03202306050001','2024-06-01','年度定期檢修，檢查單人式採茶機的採茶和運行系統。'),(8,'03202306050002','2024-06-01','年度定期檢修，檢查雙人式採茶機的動力系統及驅動機構。'),(9,'03202306050011','2024-06-01','年度定期檢修，檢查箱型乾燥機的運行和溫控系統。');
/*!40000 ALTER TABLE `repair_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resource`
--

DROP TABLE IF EXISTS `resource`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `resource` (
  `RID` varchar(14) NOT NULL,
  `name` varchar(255) NOT NULL,
  `PN` varchar(6) NOT NULL,
  `amount` int NOT NULL,
  `unit` varchar(10) NOT NULL,
  `purchase_date` date NOT NULL,
  `disposal_date` date NOT NULL,
  `age` int NOT NULL,
  `SID` varchar(12) NOT NULL,
  `factor` float DEFAULT NULL,
  `form` varchar(10) DEFAULT NULL,
  `category` varchar(10) DEFAULT NULL,
  `status` int NOT NULL DEFAULT '1',
  PRIMARY KEY (`RID`),
  KEY `resource_ibfk_1` (`PN`),
  KEY `resource_ibfk_2` (`SID`),
  CONSTRAINT `resource_ibfk_1` FOREIGN KEY (`PN`) REFERENCES `product_part_number` (`PN`),
  CONSTRAINT `resource_ibfk_2` FOREIGN KEY (`SID`) REFERENCES `suppliers` (`SID`),
  CONSTRAINT `check_srid_format` CHECK (regexp_like(`RID`,_utf8mb4'^03[0-9]{12}$'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resource`
--

LOCK TABLES `resource` WRITE;
/*!40000 ALTER TABLE `resource` DISABLE KEYS */;
INSERT INTO `resource` VALUES ('03202304050005','平揉機 (綠茶機械)','060012',1,'台','2023-04-10','2028-04-10',5,'052024010001',0.69,'類別一','範疇一',1),('03202304050010','室內萎凋設備 (頂尖農機)','060006',1,'台','2023-04-15','2028-04-15',5,'052024040004',0.75,'類別一','範疇一',1),('03202304050012','揉捻機（電動） (寶茂農機)','060008',2,'台','2023-04-01','2028-04-01',5,'052024050005',0.73,'類別一','範疇一',1),('03202305010006','有機肥 (茶田農業)','060017',5,'袋','2023-05-10','2024-05-10',1,'052024020002',0.64,'類別一','範疇一',2),('03202305010007','農藥（非有機） (茶田農業)','060018',3,'袋','2023-05-20','2024-05-20',1,'052024020002',0.63,'類別一','範疇一',2),('03202305050003','熱風萎凋機 (綠茶機械)','060005',1,'台','2023-05-15','2028-05-15',5,'052024010001',0.76,'類別一','範疇一',1),('03202305050004','炒菁機 (綠茶機械)','060007',1,'台','2023-05-20','2028-05-20',5,'052024010001',0.74,'類別一','範疇一',1),('03202305050016','除草機 (和興農業)','060020',1,'台','2023-05-01','2028-05-01',5,'052024070007',0.61,'類別一','範疇一',1),('03202306010008','有機除蟲劑（蘇力菌） (宏茂農業)','060019',2,'袋','2023-06-05','2024-06-05',1,'052024030003',0.62,'類別一','範疇一',2),('03202306010009','化肥（氮磷鉀） (宏茂農業)','060016',10,'袋','2023-06-10','2024-06-10',1,'052024030003',0.65,'類別一','範疇一',2),('03202306010013','日光燈 (寶茂農機)','060015',4,'盞','2023-06-05','2024-06-05',1,'052024050005',0.66,'類別一','範疇一',1),('03202306010014','有機肥 (山水茶業)','060017',3,'袋','2023-06-01','2024-06-01',1,'052024060006',0.64,'類別一','範疇一',2),('03202306010015','農藥（非有機） (山水茶業)','060018',2,'袋','2023-06-10','2024-06-10',1,'052024060006',0.63,'類別一','範疇一',2),('03202306020020','堆肥（瑞豐農業）','060023',40,'袋','2023-06-01','2025-06-01',2,'052024090009',0.58,'類別一','範疇一',1),('03202306050001','單人式採茶機 (綠茶機械)','060001',1,'台','2023-06-01','2028-06-01',5,'052024010001',0.8,'類別一','範疇一',1),('03202306050002','雙人式採茶機 (綠茶機械)','060002',1,'台','2023-06-01','2028-06-01',5,'052024010001',0.79,'類別一','範疇一',1),('03202306050011','箱型乾燥機（焙茶機） (頂尖農機)','060013',1,'台','2023-06-01','2028-06-01',5,'052024040004',0.68,'類別一','範疇一',1),('03202306050019','翻土機（瑞豐農業）','060021',4,'台','2023-06-01','2028-06-01',5,'052024090009',0.6,'類別一','範疇一',1),('03202306070017','電力供應 (台電)','060024',0,'度','2023-06-01','2030-06-01',7,'052024130013',0.494,'類別二','範疇二',2),('03202306070018','水源供應 (台水)','060025',0,'度','2023-06-01','2030-06-01',7,'052024140014',0.156,'類別四','範疇三',2),('03202306150021','修剪工具（富林農業）','060022',10,'項','2023-06-01','2038-06-01',15,'052024120012',0.59,'類別一','範疇一',1),('03202306150022','人工採摘工具（富林農業）','060003',10,'項','2023-06-01','2038-06-01',15,'052024120012',0.78,'類別一','範疇一',1),('03202306150023','人工採摘工具（草原農機）','060009',3,'台','2023-06-01','2038-06-01',15,'052024110011',0.72,'類別一','範疇一',1);
/*!40000 ALTER TABLE `resource` ENABLE KEYS */;
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
  CONSTRAINT `check_sid_format` CHECK (regexp_like(`SID`,_utf8mb4'^05[0-9]{10}$')),
  CONSTRAINT `check_sphone_format` CHECK (regexp_like(`phone`,_utf8mb4'^[0-9]+$'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suppliers`
--

LOCK TABLES `suppliers` WRITE;
/*!40000 ALTER TABLE `suppliers` DISABLE KEYS */;
INSERT INTO `suppliers` VALUES ('052024010001','綠茶機械有限公司','0933123456','台灣','新北市三峽區大鶯路56號'),('052024020002','茶田農業器材','0987654321','台灣','台北市大安區復興南路2段88號'),('052024030003','宏茂農業科技','0912345678','台灣','台中市北區大明路45號'),('052024040004','頂尖農機公司','0966554433','台灣','台北市中山區建國北路1段10號'),('052024050005','寶茂農機設備','0918765432','台灣','新竹市香山區光明街7號'),('052024060006','山水茶業科技','0933012345','台灣','台北市中山區長春路201號'),('052024070007','和興農業機械','0945123456','台灣','新北市板橋區中山路2段159號'),('052024080008','永勝茶業器材','0901222333','台灣','台北市士林區天母西路35號'),('052024090009','瑞豐農業科技','0978777888','台灣','新北市蘆洲區長安街12號'),('052024100010','茶香農機行','0955777888','台灣','新北市汐止區建國路52號'),('052024110011','草原農機行','0935667788','台灣','台北市內湖區港墘路103號'),('052024120012','富林農業設備','0922333444','台灣','台北市松山區南京東路5段220號'),('052024130013','台灣電力公司','0212345678','台灣','台北市中山區建國北路1段100號'),('052024140014','台灣自來水公司','0287654321','台灣','台北市信義區基隆路2段12號');
/*!40000 ALTER TABLE `suppliers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usage`
--

DROP TABLE IF EXISTS `usage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usage` (
  `usageID` int NOT NULL AUTO_INCREMENT,
  `PID` varchar(10) NOT NULL,
  `PN` varchar(6) NOT NULL,
  `amount` int NOT NULL,
  `unit` varchar(45) NOT NULL,
  PRIMARY KEY (`usageID`),
  UNIQUE KEY `unique_usage` (`PID`,`PN`),
  KEY `usage_ibfk_2` (`PN`),
  CONSTRAINT `usage_ibfk_1` FOREIGN KEY (`PID`) REFERENCES `projects` (`PID`),
  CONSTRAINT `usage_ibfk_2` FOREIGN KEY (`PN`) REFERENCES `product_part_number` (`PN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usage`
--

LOCK TABLES `usage` WRITE;
/*!40000 ALTER TABLE `usage` DISABLE KEYS */;
/*!40000 ALTER TABLE `usage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `works_on`
--

DROP TABLE IF EXISTS `works_on`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `works_on` (
  `workID` int NOT NULL AUTO_INCREMENT,
  `EID` varchar(12) NOT NULL,
  `PID` varchar(10) NOT NULL,
  `position` varchar(255) NOT NULL,
  `role_on_sys` varchar(100) NOT NULL,
  PRIMARY KEY (`workID`),
  UNIQUE KEY `unique_work` (`PID`,`EID`),
  KEY `works_on_ibfk_1` (`EID`),
  CONSTRAINT `works_on_ibfk_1` FOREIGN KEY (`EID`) REFERENCES `employees` (`EID`),
  CONSTRAINT `works_on_ibfk_2` FOREIGN KEY (`PID`) REFERENCES `projects` (`PID`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `works_on`
--

LOCK TABLES `works_on` WRITE;
/*!40000 ALTER TABLE `works_on` DISABLE KEYS */;
INSERT INTO `works_on` VALUES (1,'022024010001','01240101','茶農','member'),(2,'022024010001','01240102','茶農','member'),(3,'022024010002','01240101','茶農','member'),(4,'022024010002','01240102','茶農','member'),(5,'022024010003','01240105','田地管理人','admin'),(6,'022024010003','01240106','田地管理人','admin'),(7,'022024010004','01240103','工廠管理人','admin'),(8,'022024010004','01240104','工廠管理人','admin'),(9,'022024010004','01240107','工廠管理人','admin'),(10,'022024010004','01240108','工廠管理人','admin'),(11,'022024010005','01240101','茶農','member'),(12,'022024010005','01240102','茶農','member'),(13,'022024010006','01240105','茶農','member'),(14,'022024010006','01240106','茶農','member'),(15,'022024010007','01240109','主管','admin'),(16,'022024010008','01240105','茶農','member'),(17,'022024010008','01240106','茶農','member'),(18,'022024010009','01240105','茶農','member'),(19,'022024010009','01240106','茶農','member'),(20,'022024010010','01240103','作業人員','member'),(21,'022024010010','01240104','作業人員','member'),(22,'022024010010','01240107','作業人員','member'),(23,'022024010010','01240108','作業人員','member'),(24,'022024010011','01240103','作業人員','member'),(25,'022024010011','01240104','作業人員','member'),(26,'022024010011','01240107','作業人員','member'),(27,'022024010011','01240108','作業人員','member'),(28,'022024010012','01240103','作業人員','member'),(29,'022024010012','01240104','作業人員','member'),(30,'022024010012','01240107','作業人員','member'),(31,'022024010012','01240108','作業人員','member'),(32,'022024010013','01240103','包裝人員','member'),(33,'022024010013','01240104','包裝人員','member'),(34,'022024010013','01240107','包裝人員','member'),(35,'022024010013','01240108','包裝人員','member'),(36,'022024040014','01240101','田地管理人','admin'),(37,'022024040014','01240102','田地管理人','admin'),(38,'022024040015','01240109','行政','admin'),(39,'022024040016','01240109','會計','admin'),(40,'022024080017','01240109','業務','member'),(41,'022024080018','01240109','業務','member'),(42,'022024110019','01240101','茶農','member'),(43,'022024110019','01240102','茶農','member'),(44,'022024110020','01240105','茶農','member'),(45,'022024110020','01240106','茶農','member');
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

-- Dump completed on 2024-12-09 13:41:27
