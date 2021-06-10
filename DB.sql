-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.5.8-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para parcialfinal
CREATE DATABASE IF NOT EXISTS `parcialfinal` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `parcialfinal`;

-- Volcando estructura para tabla parcialfinal.materias
CREATE TABLE IF NOT EXISTS `materias` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(150) NOT NULL,
  `semestre` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla parcialfinal.materias: ~3 rows (aproximadamente)
/*!40000 ALTER TABLE `materias` DISABLE KEYS */;
INSERT INTO `materias` (`id`, `nombre`, `semestre`) VALUES
	(3, 'sociales', 4),
	(4, 'matematicas', 4),
	(5, 'programacion', 4),
	(6, 'base de datos', 4);
/*!40000 ALTER TABLE `materias` ENABLE KEYS */;

-- Volcando estructura para tabla parcialfinal.materias_usuarios
CREATE TABLE IF NOT EXISTS `materias_usuarios` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `id_usuario` int(10) unsigned NOT NULL,
  `id_materia` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_materias_usuarios_materias` (`id_materia`),
  KEY `FK_materias_usuarios_usuarios` (`id_usuario`),
  CONSTRAINT `FK_materias_usuarios_materias` FOREIGN KEY (`id_materia`) REFERENCES `materias` (`id`) ON UPDATE CASCADE,
  CONSTRAINT `FK_materias_usuarios_usuarios` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla parcialfinal.materias_usuarios: ~3 rows (aproximadamente)
/*!40000 ALTER TABLE `materias_usuarios` DISABLE KEYS */;
INSERT INTO `materias_usuarios` (`id`, `id_usuario`, `id_materia`) VALUES
	(9, 2, 3),
	(10, 2, 5),
	(12, 3, 5),
	(14, 3, 6);
/*!40000 ALTER TABLE `materias_usuarios` ENABLE KEYS */;

-- Volcando estructura para tabla parcialfinal.sesiones
CREATE TABLE IF NOT EXISTS `sesiones` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `id_materia` int(10) unsigned NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `fecha` date NOT NULL,
  `inicia` time NOT NULL,
  `termina` time NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_sesiones_materias` (`id_materia`),
  CONSTRAINT `FK_sesiones_materias` FOREIGN KEY (`id_materia`) REFERENCES `materias` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla parcialfinal.sesiones: ~5 rows (aproximadamente)
/*!40000 ALTER TABLE `sesiones` DISABLE KEYS */;
INSERT INTO `sesiones` (`id`, `id_materia`, `nombre`, `fecha`, `inicia`, `termina`) VALUES
	(2, 3, 'session11', '2021-05-24', '12:23:23', '01:23:12'),
	(3, 3, 'session2', '2021-05-31', '12:23:23', '01:23:12'),
	(8, 3, 'session33', '2021-05-31', '12:23:23', '01:23:12'),
	(9, 4, 'session001', '2021-05-31', '11:23:23', '03:23:12'),
	(10, 5, 'quiz', '2021-05-31', '11:23:23', '03:23:12'),
	(11, 6, 'quiz', '2021-05-31', '11:23:23', '03:23:12');
/*!40000 ALTER TABLE `sesiones` ENABLE KEYS */;

-- Volcando estructura para tabla parcialfinal.sesiones_usuarios
CREATE TABLE IF NOT EXISTS `sesiones_usuarios` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `id_usuario` int(10) unsigned NOT NULL,
  `id_sesion` int(10) unsigned NOT NULL,
  `asistencia` tinyint(3) unsigned DEFAULT NULL COMMENT '0 = no, 1= si',
  PRIMARY KEY (`id`),
  KEY `FK_sessiones_usuarios_usuarios` (`id_usuario`),
  KEY `FK_sessiones_usuarios_sesiones` (`id_sesion`) USING BTREE,
  CONSTRAINT `FK_sessiones_usuarios_sesiones` FOREIGN KEY (`id_sesion`) REFERENCES `sesiones` (`id`) ON UPDATE CASCADE,
  CONSTRAINT `FK_sessiones_usuarios_usuarios` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla parcialfinal.sesiones_usuarios: ~5 rows (aproximadamente)
/*!40000 ALTER TABLE `sesiones_usuarios` DISABLE KEYS */;
INSERT INTO `sesiones_usuarios` (`id`, `id_usuario`, `id_sesion`, `asistencia`) VALUES
	(15, 2, 2, 1),
	(16, 2, 3, 1),
	(17, 2, 8, 1),
	(18, 2, 10, 1),
	(19, 3, 10, 0),
	(20, 3, 11, NULL);
/*!40000 ALTER TABLE `sesiones_usuarios` ENABLE KEYS */;

-- Volcando estructura para tabla parcialfinal.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `semestre` int(10) unsigned NOT NULL,
  `identificacion` varchar(50) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `email` varchar(255) NOT NULL,
  `telefono` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla parcialfinal.usuarios: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` (`id`, `semestre`, `identificacion`, `nombre`, `apellido`, `email`, `telefono`) VALUES
	(2, 2, '123445', 'pedro', 'perex', 'email@gmail.com', '123123'),
	(3, 3, '444', 'cam', 'bgra', 'ecal@gmail.com', '3223'),
	(5, 3, '023444', 'suject', 'mocoa', 'stt@fgffil.com', '0322223');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
