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
) ENGINE=InnoDB AUTO_INCREMENT=129 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add act',6,'add_act'),(22,'Can change act',6,'change_act'),(23,'Can delete act',6,'delete_act'),(24,'Can view act',6,'view_act'),(25,'Can add act fac',7,'add_actfac'),(26,'Can change act fac',7,'change_actfac'),(27,'Can delete act fac',7,'delete_actfac'),(28,'Can view act fac',7,'view_actfac'),(29,'Can add ef',8,'add_ef'),(30,'Can change ef',8,'change_ef'),(31,'Can delete ef',8,'delete_ef'),(32,'Can view ef',8,'view_ef'),(33,'Can add es',9,'add_es'),(34,'Can change es',9,'change_es'),(35,'Can delete es',9,'delete_es'),(36,'Can view es',9,'view_es'),(37,'Can add gwps',10,'add_gwps'),(38,'Can change gwps',10,'change_gwps'),(39,'Can delete gwps',10,'delete_gwps'),(40,'Can view gwps',10,'view_gwps'),(41,'Can add act',11,'add_act'),(42,'Can change act',11,'change_act'),(43,'Can delete act',11,'delete_act'),(44,'Can view act',11,'view_act'),(45,'Can add act fac',12,'add_actfac'),(46,'Can change act fac',12,'change_actfac'),(47,'Can delete act fac',12,'delete_actfac'),(48,'Can view act fac',12,'view_actfac'),(49,'Can add ef',13,'add_ef'),(50,'Can change ef',13,'change_ef'),(51,'Can delete ef',13,'delete_ef'),(52,'Can view ef',13,'view_ef'),(53,'Can add es',14,'add_es'),(54,'Can change es',14,'change_es'),(55,'Can delete es',14,'delete_es'),(56,'Can view es',14,'view_es'),(57,'Can add gwps',15,'add_gwps'),(58,'Can change gwps',15,'change_gwps'),(59,'Can delete gwps',15,'delete_gwps'),(60,'Can view gwps',15,'view_gwps'),(61,'Can add session',16,'add_session'),(62,'Can change session',16,'change_session'),(63,'Can delete session',16,'delete_session'),(64,'Can view session',16,'view_session'),(65,'Can add employee',17,'add_employee'),(66,'Can change employee',17,'change_employee'),(67,'Can delete employee',17,'delete_employee'),(68,'Can view employee',17,'view_employee'),(69,'Can add equipment',18,'add_equipment'),(70,'Can change equipment',18,'change_equipment'),(71,'Can delete equipment',18,'delete_equipment'),(72,'Can view equipment',18,'view_equipment'),(73,'Can add material',19,'add_material'),(74,'Can change material',19,'change_material'),(75,'Can delete material',19,'delete_material'),(76,'Can view material',19,'view_material'),(77,'Can add project',20,'add_project'),(78,'Can change project',20,'change_project'),(79,'Can delete project',20,'delete_project'),(80,'Can view project',20,'view_project'),(81,'Can add supplier',21,'add_supplier'),(82,'Can change supplier',21,'change_supplier'),(83,'Can delete supplier',21,'delete_supplier'),(84,'Can view supplier',21,'view_supplier'),(85,'Can add user',22,'add_user'),(86,'Can change user',22,'change_user'),(87,'Can delete user',22,'delete_user'),(88,'Can view user',22,'view_user'),(89,'Can add usage',23,'add_usage'),(90,'Can change usage',23,'change_usage'),(91,'Can delete usage',23,'delete_usage'),(92,'Can view usage',23,'view_usage'),(93,'Can add supply',24,'add_supply'),(94,'Can change supply',24,'change_supply'),(95,'Can delete supply',24,'delete_supply'),(96,'Can view supply',24,'view_supply'),(97,'Can add works on',25,'add_workson'),(98,'Can change works on',25,'change_workson'),(99,'Can delete works on',25,'delete_workson'),(100,'Can view works on',25,'view_workson'),(101,'Can add usage m',26,'add_usagem'),(102,'Can change usage m',26,'change_usagem'),(103,'Can delete usage m',26,'delete_usagem'),(104,'Can view usage m',26,'view_usagem'),(105,'Can add usage eq',27,'add_usageeq'),(106,'Can change usage eq',27,'change_usageeq'),(107,'Can delete usage eq',27,'delete_usageeq'),(108,'Can view usage eq',27,'view_usageeq'),(109,'Can add boundary',28,'add_boundary'),(110,'Can change boundary',28,'change_boundary'),(111,'Can delete boundary',28,'delete_boundary'),(112,'Can view boundary',28,'view_boundary'),(113,'Can add emission',29,'add_emission'),(114,'Can change emission',29,'change_emission'),(115,'Can delete emission',29,'delete_emission'),(116,'Can view emission',29,'view_emission'),(117,'Can add gas',30,'add_gas'),(118,'Can change gas',30,'change_gas'),(119,'Can delete gas',30,'delete_gas'),(120,'Can view gas',30,'view_gas'),(121,'Can add record',31,'add_record'),(122,'Can change record',31,'change_record'),(123,'Can delete record',31,'delete_record'),(124,'Can view record',31,'view_record'),(125,'Can add source',32,'add_source'),(126,'Can change source',32,'change_source'),(127,'Can delete source',32,'delete_source'),(128,'Can view source',32,'view_source');
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
INSERT INTO `boundary` VALUES ('04106234002','office 1','台北市大安區仁愛路4段234號5樓','office','022024040210','2024-09-09','022024040210','2024-09-09'),('04305123001','factory 1','新竹縣竹北市光明一路123號','factory','022024040210','2024-09-09','022024040210','2024-09-09');
/*!40000 ALTER TABLE `boundary` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `daily_record`
--

DROP TABLE IF EXISTS `daily_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `daily_record` (
  `dailyID` int NOT NULL,
  `PID` varchar(10) NOT NULL,
  `PN` varchar(6) NOT NULL,
  `date` date NOT NULL,
  `runtime` float DEFAULT NULL,
  `amount` float NOT NULL,
  `unit` varchar(10) NOT NULL,
  `created_by` varchar(12) NOT NULL,
  `created_date` date NOT NULL,
  `last_modified_by` varchar(12) NOT NULL,
  `last_modifiled_date` date NOT NULL,
  PRIMARY KEY (`dailyID`),
  KEY `daily_record_ibfk_1` (`PID`),
  KEY `daily_record_ibfk_2` (`PN`),
  KEY `daily_record_ibfk_3` (`created_by`),
  KEY `daily_record_ibfk_4` (`last_modified_by`),
  CONSTRAINT `daily_record_ibfk_1` FOREIGN KEY (`PID`) REFERENCES `projects` (`PID`),
  CONSTRAINT `daily_record_ibfk_2` FOREIGN KEY (`PN`) REFERENCES `product_part_number` (`PN`),
  CONSTRAINT `daily_record_ibfk_3` FOREIGN KEY (`created_by`) REFERENCES `employees` (`EID`),
  CONSTRAINT `daily_record_ibfk_4` FOREIGN KEY (`last_modified_by`) REFERENCES `employees` (`EID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `daily_record`
--

LOCK TABLES `daily_record` WRITE;
/*!40000 ALTER TABLE `daily_record` DISABLE KEYS */;
INSERT INTO `daily_record` VALUES (1,'01240701','060002','2024-08-17',NULL,45,'kg','022024040210','2024-09-09','022024040210','2024-09-09'),(2,'01240701','060004','2024-08-17',NULL,25,'kg','022024040210','2024-09-09','022024040210','2024-09-09'),(3,'01240701','060005','2024-08-16',5.5,1,'unit','022024040210','2024-09-09','022024040210','2024-09-09'),(4,'01240701','060007','2024-08-16',6,2,'unit','022024040210','2024-09-09','022024040210','2024-09-09'),(5,'01240701','060009','2024-08-17',6.5,1,'unit','022024040210','2024-09-09','022024040210','2024-09-09'),(6,'01240702','060001','2024-08-16',NULL,90,'kg','022024040210','2024-09-09','022024040210','2024-09-09'),(7,'01240702','060002','2024-08-17',NULL,60,'kg','022024040210','2024-09-09','022024040210','2024-09-09'),(8,'01240702','060002','2024-08-19',NULL,10,'kg','022024040210','2024-09-09','022024040210','2024-09-09'),(9,'01240702','060006','2024-08-16',5,1,'unit','022024040210','2024-09-09','022024040210','2024-09-09'),(10,'01240702','060007','2024-08-17',7,1,'unit','022024040210','2024-09-09','022024040210','2024-09-09'),(11,'01240702','060008','2024-08-17',2,2,'unit','022024040210','2024-09-09','022024040210','2024-09-09');
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
  `PID` varchar(10) NOT NULL,
  `PN` varchar(6) NOT NULL,
  `date` date NOT NULL,
  `runtime` float DEFAULT NULL,
  `amount` float NOT NULL,
  `unit` varchar(10) NOT NULL,
  `created_by` varchar(12) NOT NULL,
  `created_date` date NOT NULL,
  `status` int NOT NULL,
  PRIMARY KEY (`dailyID_modified`),
  KEY `daily_record_modified_ibfk_1` (`PID`),
  KEY `daily_record_modified_ibfk_2` (`PN`),
  KEY `daily_record_modified_ibfk_3` (`created_by`),
  CONSTRAINT `daily_record_modified_ibfk_1` FOREIGN KEY (`PID`) REFERENCES `projects` (`PID`),
  CONSTRAINT `daily_record_modified_ibfk_2` FOREIGN KEY (`PN`) REFERENCES `product_part_number` (`PN`),
  CONSTRAINT `daily_record_modified_ibfk_3` FOREIGN KEY (`created_by`) REFERENCES `employees` (`EID`)
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
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'helloworld','act'),(7,'helloworld','actfac'),(8,'helloworld','ef'),(9,'helloworld','es'),(10,'helloworld','gwps'),(11,'login','act'),(12,'login','actfac'),(13,'login','ef'),(14,'login','es'),(15,'login','gwps'),(28,'pm','boundary'),(29,'pm','emission'),(17,'pm','employee'),(18,'pm','equipment'),(30,'pm','gas'),(19,'pm','material'),(20,'pm','project'),(31,'pm','record'),(32,'pm','source'),(21,'pm','supplier'),(24,'pm','supply'),(23,'pm','usage'),(27,'pm','usageeq'),(26,'pm','usagem'),(22,'pm','user'),(25,'pm','workson'),(16,'sessions','session');
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
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-08-02 07:24:19.672000'),(2,'auth','0001_initial','2024-08-02 07:24:20.707217'),(3,'admin','0001_initial','2024-08-02 07:24:20.939531'),(4,'admin','0002_logentry_remove_auto_add','2024-08-02 07:24:20.954980'),(5,'admin','0003_logentry_add_action_flag_choices','2024-08-02 07:24:20.978110'),(6,'contenttypes','0002_remove_content_type_name','2024-08-02 07:24:21.110089'),(7,'auth','0002_alter_permission_name_max_length','2024-08-02 07:24:21.212032'),(8,'auth','0003_alter_user_email_max_length','2024-08-02 07:24:21.259136'),(9,'auth','0004_alter_user_username_opts','2024-08-02 07:24:21.281122'),(10,'auth','0005_alter_user_last_login_null','2024-08-02 07:24:21.376793'),(11,'auth','0006_require_contenttypes_0002','2024-08-02 07:24:21.385533'),(12,'auth','0007_alter_validators_add_error_messages','2024-08-02 07:24:21.409542'),(13,'auth','0008_alter_user_username_max_length','2024-08-02 07:24:21.525911'),(14,'auth','0009_alter_user_last_name_max_length','2024-08-02 07:24:21.633259'),(15,'auth','0010_alter_group_name_max_length','2024-08-02 07:24:21.677381'),(16,'auth','0011_update_proxy_permissions','2024-08-02 07:24:21.698053'),(17,'auth','0012_alter_user_first_name_max_length','2024-08-02 07:24:21.803437'),(18,'helloworld','0001_initial','2024-08-02 07:24:21.817863'),(19,'login','0001_initial','2024-08-02 07:24:21.840660'),(20,'pm','0001_initial','2024-08-07 05:53:11.943703'),(21,'pm','0002_usage_amount_usage_unit','2024-08-07 06:03:57.626789'),(22,'sessions','0001_initial','2024-08-07 06:03:57.772434'),(23,'pm','0003_usage_amount_usage_unit','2024-08-08 07:20:46.140220');
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
  `RID` varchar(14) NOT NULL,
  `GID` varchar(10) NOT NULL,
  `amount(kg)` float NOT NULL,
  PRIMARY KEY (`RID`,`GID`),
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
INSERT INTO `emission` VALUES ('03202401010010','1',10),('03202401010010','2',1),('03202403020012','1',12),('03202405010013','1',13),('03202406010014','1',14),('03202407010015','1',15),('03202407010017','1',17),('03202407010017','4',0.0005),('03202407010018','1',18),('03202407020016','1',16),('03202407020016','5',0.001),('03202408010020','1',20),('03202408010020','3',0.1),('03202408020021','1',21);
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
INSERT INTO `employees` VALUES ('022020112701','aaa',2,'aaa@mail.com','0911111111','JP',1),('022021021602','mmm',1,'mmm@mail.com','0922222222','TW',1),('022021032503','ddd',1,'ddd@mail.com','0933333333','UK',1),('022021110504','www',2,'www@mail.com','0944444444','UK',1),('022022051705','iii',1,'iii@mail.com','0955555555','VE',1),('022022062106','kkk',2,'kkk@mail.com','0966666666','TW',1),('022022062707','rrr',1,'rrr@mail.com','0977777777','VE',1),('022022070508','sss',1,'sss@mail.com','0988888888','JP',1),('022023050509','fff',2,'fff@mail.com','0999999999','VE',1),('022024040210','ccc',2,'ccc@mail.com','0910101010','TW',1);
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `green_house_gas`
--

DROP TABLE IF EXISTS `green_house_gas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `green_house_gas` (
  `GID` varchar(10) NOT NULL,
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
INSERT INTO `green_house_gas` VALUES ('1','CO2',1),('2','CH4',27.9),('3','N2O',273),('4','SF6',24300),('5','NF3',17400);
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
  PRIMARY KEY (`PN`),
  CONSTRAINT `check_pn_format` CHECK (regexp_like(`PN`,_utf8mb4'^06[0-9]{4}$'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_part_number`
--

LOCK TABLES `product_part_number` WRITE;
/*!40000 ALTER TABLE `product_part_number` DISABLE KEYS */;
INSERT INTO `product_part_number` VALUES ('060001','原油',140,'kg'),('060002','標籤貼紙',105,'kg'),('060003','油墨',120,'kg'),('060004','布料',90,'kg'),('060005','檢測儀',1,'unit'),('060006','掃描機',5,'unit'),('060007','風乾機',20,'unit'),('060008','機械手臂',14,'unit'),('060009','影印機',7,'unit');
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
INSERT INTO `projects` VALUES ('01240701','Project A','[\n    {\"step\": 1, \"equipments\": [{\"SRID\": \"03202107060003\", \"amount\": 1, \"unit\": \"unit\"}], \"materials\": [{\"SRID\": \"03202403020012\", \"amount\": 1, \"unit\": \"kg\"}], \"description\": \"Initial setup and preparation\"}, \n    {\"step\": 2, \"equipments\": [{\"SRID\": \"03202104080002\", \"amount\": 1, \"unit\": \"unit\"},{\"SRID\": \"03202207060005\", \"amount\": 1, \"unit\": \"unit\"},{\"SRID\": \"03202407010019\", \"amount\": 1, \"unit\": \"unit\"}], \"materials\": [{\"SRID\": \"03202401010010\", \"amount\": 1, \"unit\": \"kg\"},{\"SRID\": \"03202406010014\", \"amount\": 1, \"unit\": \"kg\"}], \"description\": \"Processing and assembly\"},\n    {\"step\": 3, \"equipments\": [{\"SRID\": \"03202302070007\", \"amount\": 1, \"unit\": \"unit\"}], \"materials\": [{\"SRID\": \"03202407010015\", \"amount\": 1, \"unit\": \"kg\"},{\"SRID\": \"03202407010018\", \"amount\": 1, \"unit\": \"kg\"}], \"description\": \"Final inspection and testing\"}\n]','022024040210','04106234002'),('01240702','Project B','[\n  {\"step\": 1, \"equipments\": [{\"SRID\": \"03202007060001\", \"amount\": 1, \"unit\": \"unit\"}], \"materials\": [\"\"], \"description\": \"Design and planning\"},\n  {\"step\": 2, \"equipments\": [{\"SRID\": \"03202209080006\", \"amount\": 1, \"unit\": \"unit\"}, {\"SRID\": \"03202307020008\", \"amount\": 1, \"unit\": \"unit\"}, {\"SRID\": \"03202311020009\", \"amount\": 1, \"unit\": \"unit\"}], \"materials\": [{\"SRID\": \"03202405010013\", \"amount\": 1, \"unit\": \"kg\"}, {\"SRID\": \"03202407020016\", \"amount\": 1, \"unit\": \"kg\"}, {\"SRID\": \"03202407010017\", \"amount\": 1, \"unit\": \"kg\"}, {\"SRID\": \"03202408010020\", \"amount\": 1, \"unit\": \"kg\"}], \"description\": \"Processing and assembly\"},\n  {\"step\": 3, \"equipments\": [{\"SRID\": \"03202402090011\", \"amount\": 1, \"unit\": \"unit\"}], \"materials\": [{\"SRID\": \"03202407010018\", \"amount\": 1, \"unit\": \"kg\"}], \"description\": \"Quality check and packaging\"},\n  {\"step\": 4, \"equipments\": [{\"SRID\": \"03202302070007\", \"amount\": 1, \"unit\": \"unit\"}], \"materials\": [{\"SRID\": \"03202407010015\", \"amount\": 1, \"unit\": \"kg\"}, {\"SRID\": \"03202408020021\", \"amount\": 1, \"unit\": \"kg\"}], \"description\": \"Final inspection and testing\"}\n]','022022070508','04106234002');
/*!40000 ALTER TABLE `projects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `repair_log`
--

DROP TABLE IF EXISTS `repair_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `repair_log` (
  `RID` varchar(14) NOT NULL,
  `date` date NOT NULL,
  `notes` mediumtext,
  PRIMARY KEY (`RID`,`date`),
  CONSTRAINT `repair_log_ibfk_1` FOREIGN KEY (`RID`) REFERENCES `resource` (`RID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `repair_log`
--

LOCK TABLES `repair_log` WRITE;
/*!40000 ALTER TABLE `repair_log` DISABLE KEYS */;
INSERT INTO `repair_log` VALUES ('03202007060001','2024-01-31','定期保養'),('03202104080002','2024-01-31','定期保養'),('03202107060003','2024-01-31','定期保養'),('03202201070004','2024-01-31','定期保養'),('03202207060005','2024-01-31','定期保養'),('03202209080006','2024-08-22','定期保養'),('03202302070007','2024-01-31','定期保養'),('03202307020008','2024-01-31','定期保養'),('03202311020009','2024-08-22','定期保養'),('03202407010015','2024-08-22','定期保養');
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
INSERT INTO `resource` VALUES ('03202007060001','Equipment A','060006',5,'unit','2020-07-15','2026-07-15',6,'052020010004',NULL,NULL,NULL,1),('03202104080002','Equipment B','060007',5,'unit','2021-04-01','2029-04-01',8,'052020100008',NULL,NULL,NULL,1),('03202107060003','Equipment C','060005',1,'unit','2021-07-10','2027-07-10',6,'052020020005',NULL,NULL,NULL,1),('03202201070004','Equipment D','060009',1,'unit','2022-01-01','2029-01-01',7,'052020100007',NULL,NULL,NULL,1),('03202207060005','Equipment E','060007',8,'unit','2022-07-15','2028-07-15',6,'052020020006',NULL,NULL,NULL,1),('03202209080006','Equipment F','060007',7,'unit','2022-09-01','2030-09-01',8,'052021040010',NULL,NULL,NULL,1),('03202302070007','Equipment G','060009',6,'unit','2023-02-05','2030-02-05',7,'052020100009',NULL,NULL,NULL,1),('03202307020008','Equipment H','060008',2,'unit','2023-07-01','2025-07-01',2,'052020010001',NULL,NULL,NULL,1),('03202311020009','Equipment I','060008',9,'unit','2023-11-10','2025-11-10',2,'052020010003',NULL,NULL,NULL,1),('03202401010010','Material A','060001',50,'kg','2024-01-10','2025-01-10',1,'052020100007',NULL,NULL,NULL,2),('03202402090011','Equipment J','060008',1,'unit','2024-02-01','2033-02-01',9,'052021080011',NULL,NULL,NULL,1),('03202403020012','Material B','060003',30,'kg','2024-03-15','2026-03-15',2,'052022030012',NULL,NULL,NULL,2),('03202405010013','Material C','060001',40,'kg','2024-05-20','2025-05-20',1,'052020010004',NULL,NULL,NULL,2),('03202406010014','Material D','060004',25,'kg','2024-06-25','2025-06-25',1,'052023050014',NULL,NULL,NULL,2),('03202407010015','Material E','060002',60,'kg','2024-07-10','2025-07-10',1,'052020010001',NULL,NULL,NULL,2),('03202407010017','Material G','060003',35,'kg','2024-07-15','2025-07-15',1,'052020100009',NULL,NULL,NULL,2),('03202407010018','Material H','060002',45,'kg','2024-07-20','2025-07-20',1,'052021080011',NULL,NULL,NULL,2),('03202407010019','Equipment K','060008',2,'unit','2024-07-20','2025-07-20',1,'052020010002',NULL,NULL,NULL,1),('03202407020016','Material F','060003',55,'kg','2024-07-13','2026-07-13',2,'052023050015',NULL,NULL,NULL,2),('03202408010020','Material I','060004',65,'kg','2024-08-05','2025-08-05',1,'052020010002',NULL,NULL,NULL,2),('03202408020021','Material J','060001',50,'kg','2024-08-05','2026-08-05',2,'052022070013',NULL,NULL,NULL,2);
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
INSERT INTO `suppliers` VALUES ('052020010001','Supplier A','0912345678','TW','1234 Taiwan St, Taipei'),('052020010002','Supplier B','0923456789','TW','5678 Taiwan Rd, Taipei'),('052020010003','Supplier C','0934567890','TW','9101 Taiwan Ave, Kaohsiung'),('052020010004','Supplier D','0945678901','TW','2345 Taiwan Blvd, Taichung'),('052020020005','Supplier E','0956789012','TW','6789 Taiwan Ln, Tainan'),('052020020006','Supplier F','0967890123','TW','3456 Taiwan Dr, Hsinchu'),('052020100007','Supplier G','0978901234','JP','7890 Tokyo St, Shibuya'),('052020100008','Supplier H','0989012345','JP','1234 Osaka Rd, Namba'),('052020100009','Supplier I','0990123456','JP','5678 Kyoto Ave, Gion'),('052021040010','Supplier J','0901234567','TW','9101 Taoyuan St, Taoyuan'),('052021080011','Supplier K','0912345670','TW','3456 Chiayi Ln, Chiayi'),('052022030012','Supplier L','0923456781','TW','6789 Pingtung Dr, Pingtung'),('052022070013','Supplier M','0934567892','TW','9101 Yunlin Blvd, Yunlin'),('052023050014','Supplier N','0945678903','TW','1234 Hualien Ct, Hualien'),('052023050015','Supplier O','0956789014','TW','5678 Keelung Pl, Keelung');
/*!40000 ALTER TABLE `suppliers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usage`
--

DROP TABLE IF EXISTS `usage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usage` (
  `PID` varchar(10) NOT NULL,
  `PN` varchar(6) NOT NULL,
  `amount` int NOT NULL,
  `unit` varchar(45) NOT NULL,
  PRIMARY KEY (`PN`,`PID`),
  KEY `usage_ibfk_1` (`PID`),
  CONSTRAINT `usage_ibfk_1` FOREIGN KEY (`PID`) REFERENCES `projects` (`PID`),
  CONSTRAINT `usage_ibfk_2` FOREIGN KEY (`PN`) REFERENCES `product_part_number` (`PN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usage`
--

LOCK TABLES `usage` WRITE;
/*!40000 ALTER TABLE `usage` DISABLE KEYS */;
INSERT INTO `usage` VALUES ('01240701','060001',1,'kg'),('01240702','060001',2,'kg'),('01240701','060002',2,'kg'),('01240702','060002',2,'kg'),('01240701','060003',1,'kg'),('01240702','060003',2,'kg'),('01240701','060004',1,'kg'),('01240702','060004',1,'kg'),('01240701','060005',1,'unit'),('01240702','060006',1,'unit'),('01240701','060007',2,'unit'),('01240702','060007',1,'unit'),('01240701','060008',1,'unit'),('01240702','060008',3,'unit'),('01240701','060009',1,'unit'),('01240702','060009',1,'unit');
/*!40000 ALTER TABLE `usage` ENABLE KEYS */;
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
  `role_on_sys` varchar(100) NOT NULL,
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
INSERT INTO `works_on` VALUES ('022020112701','01240701','top manager','admin'),('022020112701','01240702','top manager','admin'),('022021021602','01240702','Frontend Engineer','read-only'),('022021032503','01240701','Processing Technician','read-only'),('022021110504','01240701','Testing Specialist','read-only'),('022022051705','01240702','Packaging Specialist','read-only'),('022022062106','01240702','Design Engineer','read-only'),('022022062707','01240701','Setup Engineer','member'),('022022062707','01240702','Setup Engineer','member'),('022022070508','01240702','project manager','member'),('022023050509','01240702','Testing Specialist','read-only'),('022024040210','01240701','project manager','member');
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

-- Dump completed on 2024-09-23 14:18:56
