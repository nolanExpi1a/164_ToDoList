-- --------------------------------------------------------
-- Hôte:                         127.0.0.1
-- Version du serveur:           8.0.30 - MySQL Community Server - GPL
-- SE du serveur:                Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Listage de la structure de la base pour swerzmann_nolan_todolist
CREATE DATABASE IF NOT EXISTS `swerzmann_nolan_todolist` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `swerzmann_nolan_todolist`;

-- Listage de la structure de table swerzmann_nolan_todolist. t_artistes
CREATE TABLE IF NOT EXISTS `t_artistes` (
  `ID_Artiste` int NOT NULL AUTO_INCREMENT,
  `Nom_Artiste` varchar(255) DEFAULT NULL,
  `Description` text,
  `Genre_Musical` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ID_Artiste`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table swerzmann_nolan_todolist.t_artistes : ~5 rows (environ)
INSERT INTO `t_artistes` (`ID_Artiste`, `Nom_Artiste`, `Description`, `Genre_Musical`) VALUES
	(1, 'Artiste 1', 'Description de l\'artiste 1', 'Genre musical 1'),
	(2, 'Artiste 2', 'Description de l\'artiste 2', 'Genre musical 2'),
	(3, 'Artiste 3', 'Description de l\'artiste 3', 'Genre musical 3'),
	(4, 'Artiste 4', 'Description de l\'artiste 4', 'Genre musical 4'),
	(5, 'Artiste 5', 'Description de l\'artiste 5', 'Genre musical 5');

-- Listage de la structure de table swerzmann_nolan_todolist. t_calendrier
CREATE TABLE IF NOT EXISTS `t_calendrier` (
  `ID_Evenement` int NOT NULL AUTO_INCREMENT,
  `Nom_Evenement` varchar(255) DEFAULT NULL,
  `Date_Evenement` date DEFAULT NULL,
  `Lieu` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID_Evenement`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table swerzmann_nolan_todolist.t_calendrier : ~5 rows (environ)
INSERT INTO `t_calendrier` (`ID_Evenement`, `Nom_Evenement`, `Date_Evenement`, `Lieu`) VALUES
	(2, 'Spectacle de feu d\'artifice', '2024-07-16', 'Parc municipal'),
	(3, 'Atelier de musique', '2024-07-17', 'Salle communautaire'),
	(4, 'Projection de films en plein air', '2024-07-18', 'Plage'),
	(5, 'Défilé de mode', '2024-07-19', 'Centre-ville'),
	(15, 'basidbf', '2024-06-29', 'allaman');

-- Listage de la structure de table swerzmann_nolan_todolist. t_categories
CREATE TABLE IF NOT EXISTS `t_categories` (
  `ID_Categorie` int NOT NULL AUTO_INCREMENT,
  `Nom_Categorie` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID_Categorie`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table swerzmann_nolan_todolist.t_categories : ~5 rows (environ)
INSERT INTO `t_categories` (`ID_Categorie`, `Nom_Categorie`) VALUES
	(1, 'Catégorie 1'),
	(2, 'Catégorie 2'),
	(3, 'Catégorie 3'),
	(4, 'Catégorie 4'),
	(5, 'Catégorie 5');

-- Listage de la structure de table swerzmann_nolan_todolist. t_contrats
CREATE TABLE IF NOT EXISTS `t_contrats` (
  `ID_Contrat` int NOT NULL AUTO_INCREMENT,
  `ID_Artiste` int DEFAULT NULL,
  `Date_Contrat` date DEFAULT NULL,
  `Description_Contrat` text,
  `Montant` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`ID_Contrat`),
  KEY `ID_Artiste` (`ID_Artiste`),
  CONSTRAINT `t_contrats_ibfk_1` FOREIGN KEY (`ID_Artiste`) REFERENCES `t_artistes` (`ID_Artiste`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table swerzmann_nolan_todolist.t_contrats : ~5 rows (environ)
INSERT INTO `t_contrats` (`ID_Contrat`, `ID_Artiste`, `Date_Contrat`, `Description_Contrat`, `Montant`) VALUES
	(1, 1, '2024-04-17', 'Description du contrat avec l\'artiste 1', 1500.00),
	(2, 2, '2024-04-17', 'Description du contrat avec l\'artiste 2', 2000.00),
	(3, 3, '2024-04-17', 'Description du contrat avec l\'artiste 3', 1800.00),
	(4, 4, '2024-04-17', 'Description du contrat avec l\'artiste 4', 1700.00),
	(5, 5, '2024-04-17', 'Description du contrat avec l\'artiste 5', 1600.00);

-- Listage de la structure de table swerzmann_nolan_todolist. t_participants
CREATE TABLE IF NOT EXISTS `t_participants` (
  `ID_Participant` int NOT NULL AUTO_INCREMENT,
  `Nom_Participant` varchar(255) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `Nombre_Billets` int DEFAULT NULL,
  `Montant_Total` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`ID_Participant`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table swerzmann_nolan_todolist.t_participants : ~5 rows (environ)
INSERT INTO `t_participants` (`ID_Participant`, `Nom_Participant`, `Email`, `Nombre_Billets`, `Montant_Total`) VALUES
	(1, 'Alice', 'alice@example.com', 2, 50.00),
	(2, 'Bob', 'bob@example.com', 3, 75.00),
	(3, 'Charlie', 'charlie@example.com', 1, 25.00),
	(4, 'David', 'david@example.com', 4, 100.00),
	(5, 'Eve', 'eve@example.com', 2, 50.00);

-- Listage de la structure de table swerzmann_nolan_todolist. t_personnel
CREATE TABLE IF NOT EXISTS `t_personnel` (
  `ID_Personnel` int NOT NULL AUTO_INCREMENT,
  `Nom_Personnel` varchar(255) DEFAULT NULL,
  `Role` varchar(255) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID_Personnel`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table swerzmann_nolan_todolist.t_personnel : ~5 rows (environ)
INSERT INTO `t_personnel` (`ID_Personnel`, `Nom_Personnel`, `Role`, `Email`) VALUES
	(1, 'Jean', 'Directeur du festival', 'jean@example.com'),
	(2, 'Marie', 'Responsable des artistes', 'marie@example.com'),
	(3, 'Pierre', 'Coordinateur des bénévoles', 'pierre@example.com'),
	(4, 'Sophie', 'Responsable de la sécurité', 'sophie@example.com'),
	(5, 'Luc', 'Technicien son et lumière', 'luc@example.com');

-- Listage de la structure de table swerzmann_nolan_todolist. t_projets
CREATE TABLE IF NOT EXISTS `t_projets` (
  `ID_Projet` int NOT NULL AUTO_INCREMENT,
  `Nom_Projet` varchar(255) DEFAULT NULL,
  `Description` text,
  PRIMARY KEY (`ID_Projet`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table swerzmann_nolan_todolist.t_projets : ~5 rows (environ)
INSERT INTO `t_projets` (`ID_Projet`, `Nom_Projet`, `Description`) VALUES
	(1, 'Projet A', 'Description du projet A'),
	(2, 'Projet B', 'Description du projet B'),
	(3, 'Projet C', 'Description du projet C'),
	(4, 'Projet D', 'Description du projet D'),
	(5, 'Projet E', 'Description du projet E');

-- Listage de la structure de table swerzmann_nolan_todolist. t_scenes
CREATE TABLE IF NOT EXISTS `t_scenes` (
  `ID_Scene` int NOT NULL AUTO_INCREMENT,
  `Nom_Scene` varchar(255) DEFAULT NULL,
  `Capacite` int DEFAULT NULL,
  `Description` text,
  PRIMARY KEY (`ID_Scene`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table swerzmann_nolan_todolist.t_scenes : ~5 rows (environ)
INSERT INTO `t_scenes` (`ID_Scene`, `Nom_Scene`, `Capacite`, `Description`) VALUES
	(1, 'Scène principale', 1000, 'La principale scène où se déroulent les concerts'),
	(2, 'Scène secondaire', 500, 'Une scène plus petite pour des performances plus intimes'),
	(3, 'Scène électro', 800, 'Scène dédiée à la musique électronique'),
	(4, 'Scène de théâtre', 300, 'Scène pour les pièces de théâtre et les performances artistiques'),
	(5, 'Scène acoustique', 200, 'Scène pour les performances musicales acoustiques');

-- Listage de la structure de table swerzmann_nolan_todolist. t_sponsors
CREATE TABLE IF NOT EXISTS `t_sponsors` (
  `ID_Sponsor` int NOT NULL AUTO_INCREMENT,
  `Nom_Sponsor` varchar(255) DEFAULT NULL,
  `Description` text,
  `Logo` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID_Sponsor`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table swerzmann_nolan_todolist.t_sponsors : ~5 rows (environ)
INSERT INTO `t_sponsors` (`ID_Sponsor`, `Nom_Sponsor`, `Description`, `Logo`) VALUES
	(1, 'Sponsor A', 'Sponsor principal du festival', 'logo_sponsor_a.png'),
	(2, 'Sponsor B', 'Sponsor du secteur de la restauration', 'logo_sponsor_b.png'),
	(3, 'Sponsor C', 'Sponsor du secteur de l\'électronique', 'logo_sponsor_c.png'),
	(4, 'Sponsor D', 'Sponsor du secteur de la mode', 'logo_sponsor_d.png'),
	(5, 'Sponsor E', 'Sponsor du secteur automobile', 'logo_sponsor_e.png');

-- Listage de la structure de table swerzmann_nolan_todolist. t_taches
CREATE TABLE IF NOT EXISTS `t_taches` (
  `ID_Tache` int NOT NULL AUTO_INCREMENT,
  `ID_Utilisateur` int DEFAULT NULL,
  `ID_Projet` int DEFAULT NULL,
  `ID_Categorie` int DEFAULT NULL,
  `Titre` varchar(255) DEFAULT NULL,
  `Description` text,
  `Date_Creation` date DEFAULT NULL,
  `Date_Echeance` date DEFAULT NULL,
  `Statut` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID_Tache`),
  KEY `ID_Utilisateur` (`ID_Utilisateur`),
  KEY `ID_Projet` (`ID_Projet`),
  KEY `ID_Categorie` (`ID_Categorie`),
  CONSTRAINT `t_taches_idfk_2` FOREIGN KEY (`ID_Projet`) REFERENCES `t_projets` (`ID_Projet`),
  CONSTRAINT `t_taches_idfk_3` FOREIGN KEY (`ID_Categorie`) REFERENCES `t_categories` (`ID_Categorie`),
  CONSTRAINT `t_taches_idk_1` FOREIGN KEY (`ID_Utilisateur`) REFERENCES `t_utilisateurs` (`ID_Utilisateur`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table swerzmann_nolan_todolist.t_taches : ~5 rows (environ)
INSERT INTO `t_taches` (`ID_Tache`, `ID_Utilisateur`, `ID_Projet`, `ID_Categorie`, `Titre`, `Description`, `Date_Creation`, `Date_Echeance`, `Statut`) VALUES
	(1, 1, 1, 1, 'Tâche 1', 'faire la vaiselle', '2024-04-17', '2024-04-20', 'À faire'),
	(2, 2, 1, 2, 'Tâche 2', 'sortir les poubelles', '2024-04-17', '2024-04-21', 'En cours'),
	(3, 3, 2, 3, 'Tâche 3', 'Description de la tâche 3', '2024-04-17', '2024-04-22', 'Terminé'),
	(4, 4, 2, 4, 'Tâche 4', 'Description de la tâche 4', '2024-04-17', '2024-04-23', 'À faire'),
	(5, 5, 3, 5, 'Tâche 5', 'Description de la tâche 5', '2024-04-17', '2024-04-24', 'À faire');

-- Listage de la structure de table swerzmann_nolan_todolist. t_taches_artistes
CREATE TABLE IF NOT EXISTS `t_taches_artistes` (
  `ID_Tache_Artiste` int NOT NULL AUTO_INCREMENT,
  `ID_Tache` int DEFAULT NULL,
  `ID_Artiste` int DEFAULT NULL,
  PRIMARY KEY (`ID_Tache_Artiste`),
  KEY `ID_Tache` (`ID_Tache`),
  KEY `ID_Artiste` (`ID_Artiste`),
  CONSTRAINT `t_taches_artistes_ibfk_1` FOREIGN KEY (`ID_Tache`) REFERENCES `t_taches_festival` (`ID_Tache`),
  CONSTRAINT `t_taches_artistes_ibfk_2` FOREIGN KEY (`ID_Artiste`) REFERENCES `t_artistes` (`ID_Artiste`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table swerzmann_nolan_todolist.t_taches_artistes : ~5 rows (environ)
INSERT INTO `t_taches_artistes` (`ID_Tache_Artiste`, `ID_Tache`, `ID_Artiste`) VALUES
	(1, 1, 1),
	(2, 2, 2),
	(3, 3, 3),
	(4, 4, 4),
	(5, 5, 5);

-- Listage de la structure de table swerzmann_nolan_todolist. t_taches_festival
CREATE TABLE IF NOT EXISTS `t_taches_festival` (
  `ID_Tache` int NOT NULL AUTO_INCREMENT,
  `Description_Tache` text,
  `Date_Echeance` date DEFAULT NULL,
  `Statut` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID_Tache`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table swerzmann_nolan_todolist.t_taches_festival : ~5 rows (environ)
INSERT INTO `t_taches_festival` (`ID_Tache`, `Description_Tache`, `Date_Echeance`, `Statut`) VALUES
	(1, 'Préparer la scène principale', '2024-04-20', 'À faire'),
	(2, 'Installer les stands de nourriture', '2024-04-21', 'En cours'),
	(3, 'Coordonner les bénévoles', '2024-04-22', 'Terminé'),
	(4, 'Assurer la sécurité des participants', '2024-04-23', 'À faire'),
	(5, 'Organiser les transports pour les artistes', '2024-04-24', 'À faire');

-- Listage de la structure de table swerzmann_nolan_todolist. t_taches_partagees
CREATE TABLE IF NOT EXISTS `t_taches_partagees` (
  `ID_Tache_Partagee` int NOT NULL AUTO_INCREMENT,
  `ID_Tache` int DEFAULT NULL,
  `ID_Utilisateur_Partage` int DEFAULT NULL,
  PRIMARY KEY (`ID_Tache_Partagee`),
  KEY `ID_Tache` (`ID_Tache`),
  KEY `ID_Utilisateur_Partage` (`ID_Utilisateur_Partage`),
  CONSTRAINT `t_taches_partagees_ibfk_1` FOREIGN KEY (`ID_Tache`) REFERENCES `t_taches` (`ID_Tache`),
  CONSTRAINT `t_taches_partagees_ibfk_2` FOREIGN KEY (`ID_Utilisateur_Partage`) REFERENCES `t_utilisateurs` (`ID_Utilisateur`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table swerzmann_nolan_todolist.t_taches_partagees : ~5 rows (environ)
INSERT INTO `t_taches_partagees` (`ID_Tache_Partagee`, `ID_Tache`, `ID_Utilisateur_Partage`) VALUES
	(1, 1, 2),
	(2, 2, 3),
	(3, 3, 4),
	(4, 4, 5),
	(5, 5, 1);

-- Listage de la structure de table swerzmann_nolan_todolist. t_utilisateurs
CREATE TABLE IF NOT EXISTS `t_utilisateurs` (
  `ID_Utilisateur` int NOT NULL AUTO_INCREMENT,
  `Nom_Utilisateur` varchar(255) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID_Utilisateur`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table swerzmann_nolan_todolist.t_utilisateurs : ~5 rows (environ)
INSERT INTO `t_utilisateurs` (`ID_Utilisateur`, `Nom_Utilisateur`, `Email`) VALUES
	(1, 'Alice', 'alice@example.com'),
	(2, 'Bob', 'bob@example.com'),
	(3, 'Charlie', 'charlie@example.com'),
	(4, 'David', 'david@example.com'),
	(5, 'Eve', 'eve@example.com');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
