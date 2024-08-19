-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-08-2024 a las 02:46:12
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `futbol`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `equipo`
--

CREATE TABLE `equipo` (
  `id` int(11) NOT NULL,
  `nombre` varchar(150) NOT NULL,
  `pais` varchar(150) NOT NULL,
  `estadio` varchar(150) NOT NULL,
  `presidente` int(11) NOT NULL,
  `presupuesto` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `equipo`
--

INSERT INTO `equipo` (`id`, `nombre`, `pais`, `estadio`, `presidente`, `presupuesto`) VALUES
(1, 'temu haul', 'mexico', 'nohay', 21, 150000),
(3, 'El balin', 'mexico', 'no tiene', 3, 15000),
(4, 'Danza', 'mexico', 'utd', 7, 0),
(5, 'futbolito', 'francia', 'colita', 6, 150000),
(6, 'idshfoids', 'iodshf', 'isdhfos', 15, 0),
(7, 'sfe', 'sdfsd', 'fsdf', 17, 0),
(8, 'baab', 'usa', '12000', 22, 12000);

--
-- Disparadores `equipo`
--
DELIMITER $$
CREATE TRIGGER `insertar_equipo_asociar_presidente` AFTER INSERT ON `equipo` FOR EACH ROW BEGIN
  UPDATE usuarios
  SET equipo = NEW.id
  WHERE id = NEW.presidente;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `goles`
--

CREATE TABLE `goles` (
  `id` int(11) NOT NULL,
  `id_jugador` int(11) NOT NULL,
  `id_equipo` int(11) NOT NULL,
  `id_partido` int(11) NOT NULL,
  `minuto` varchar(150) NOT NULL,
  `golesT` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `goles`
--

INSERT INTO `goles` (`id`, `id_jugador`, `id_equipo`, `id_partido`, `minuto`, `golesT`) VALUES
(1, 6, 1, 6, '15', 3),
(2, 6, 1, 6, '55', 3),
(4, 11, 4, 9, '10', 10),
(5, 11, 4, 9, '15', 10),
(6, 11, 4, 9, '20', 10),
(7, 11, 4, 9, '25', 10),
(8, 11, 4, 9, '30', 10),
(9, 12, 4, 9, '30', 10),
(10, 12, 4, 9, '35', 10),
(11, 12, 4, 9, '40', 10),
(12, 12, 4, 9, '45', 10),
(13, 12, 4, 9, '50', 10),
(38760, 1, 3, 11, '15', 1),
(38761, 8, 3, 12, '18', 13),
(38762, 8, 3, 11, '10', 2),
(38763, 8, 3, 11, '19', 2),
(38764, 1, 3, 11, '15', 2),
(38766, 1, 3, 11, '16', 2),
(38767, 15, 3, 12, '16', 3),
(38768, 15, 3, 12, '17', 3),
(38769, 15, 3, 12, '20', 3),
(38770, 15, 3, 12, '18', 2),
(38771, 1, 3, 12, '17', 2),
(38772, 8, 3, 12, '15', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `partido`
--

CREATE TABLE `partido` (
  `id` int(11) NOT NULL,
  `idEq1` int(11) NOT NULL,
  `idEq2` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `estado` varchar(150) NOT NULL,
  `estadio` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `partido`
--

INSERT INTO `partido` (`id`, `idEq1`, `idEq2`, `fecha`, `estado`, `estadio`) VALUES
(2, 3, 4, '2024-10-10', 'Cancelado', 'utd'),
(4, 4, 1, '2024-11-11', 'Cancelado', 'utd'),
(5, 1, 4, '2024-11-12', 'Completado', 'utd'),
(6, 3, 1, '2024-12-12', 'Completado', 'francisco villa'),
(7, 4, 1, '2024-08-20', 'Cancelado', 'politecnico'),
(8, 4, 3, '2024-08-20', 'Cancelado', 'tecno'),
(9, 1, 4, '2024-09-10', 'Completado', 'Parque'),
(10, 5, 3, '2024-08-13', 'Cancelado', 'no tiene'),
(11, 3, 1, '2024-10-10', 'Pendiente', 'tecno'),
(12, 3, 1, '2024-10-10', 'Completado', 'tecno'),
(13, 5, 3, '2024-12-12', 'Pendiente', 'utd');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `nombre_usuario` varchar(150) NOT NULL,
  `contraseña` varchar(150) NOT NULL,
  `nombre` varchar(150) NOT NULL,
  `apellido` varchar(150) NOT NULL,
  `fecha_nac` date NOT NULL,
  `salario` varchar(150) NOT NULL,
  `tipo` varchar(150) NOT NULL,
  `numeroCamiseta` int(10) DEFAULT NULL,
  `nacionalidad` varchar(150) DEFAULT NULL,
  `equipo` int(11) DEFAULT NULL,
  `antiguedad` varchar(150) DEFAULT NULL,
  `equipo_jug` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre_usuario`, `contraseña`, `nombre`, `apellido`, `fecha_nac`, `salario`, `tipo`, `numeroCamiseta`, `nacionalidad`, `equipo`, `antiguedad`, `equipo_jug`) VALUES
(1, 'localhost_diluk', 'sebas12', 'sebastian', 'lozano', '2005-04-05', '15000', 'Jugador', 15, 'mexico', NULL, NULL, 1),
(3, 'vallejo12', 'vallejin', 'leonardo', 'vallejo', '2005-06-27', '150000', 'Presidente', NULL, NULL, 3, '15 años', 0),
(6, 'pepito', 'pro', 'pepe', 'garza', '2024-08-13', '140231', 'Presidente', NULL, NULL, 5, '10 años', 0),
(7, 'enjambremx', 'enjambre', 'enjambre', 'mexico', '2000-01-01', '15', 'Presidente', NULL, NULL, 4, '1', 0),
(8, 'giss', 'giss', 'gisela', 'rey', '1972-05-02', '2000', 'Jugador', 12, 'mex', NULL, NULL, 3),
(10, 'lluvia', 'lluvia', 'lluvia', 'lluvia', '2000-01-01', '100000', 'Jugador', 3, 'usa', NULL, NULL, 3),
(11, 'mania', 'mani', 'mani', 'mani', '2020-01-01', '232134', 'Jugador', 21, 'africana', NULL, NULL, 4),
(12, 'kelsy', 'diez', 'kelsy', 'diez', '2005-06-03', '123', 'Jugador', 10, 'rusia', NULL, NULL, 4),
(13, 'lei', '1234', 'Leya', 'meza', '0000-00-00', '35000', 'Presidente', NULL, NULL, NULL, '34', 0),
(14, 'sdhifhs', 'oisbhioas', 'ssiofso', 'iodshf', '2000-01-01', '213213', 'Jugador', 34, 'mexico', NULL, NULL, 0),
(15, 'djsfbs', 'sdfjksbndf', 'esteban', 'lozano', '2000-01-01', '2424214', 'Presidente', NULL, NULL, 6, '56 años', 0),
(16, 'riki', 'riki', 'ricardo', 'lozano', '2013-03-21', '15000', 'Jugador', 6, 'mexico', NULL, NULL, 0),
(17, 'presidente1', 'presidente1', 'presidente1', 'presidente1', '2000-01-01', '1233421', 'Presidente', NULL, NULL, 7, '12 años', 0),
(18, 'dflsdkhf', 'dsfñshdf', 'oihsao', 'oioifhoiwe', '2000-01-01', '1234214', 'Jugador', 234, 'uitiogo', NULL, NULL, 0),
(19, 'ergr', 'sdgds', 'sdgsdg', 'sdgsd', '2000-01-01', '1213', 'Jugador', 321, 'sdgsd', NULL, NULL, 0),
(21, 'papito', 'papito', 'papito', 'papito', '2000-01-01', '12345', 'Presidente', NULL, NULL, 1, '16 años', 0),
(22, 'maynez', 'maynez123', 'maines', 'presindete', '2005-02-20', '7777', 'Presidente', NULL, NULL, 8, '20 años', 0);

--
-- Disparadores `usuarios`
--
DELIMITER $$
CREATE TRIGGER `actualizar_equipo_al_eliminar_equipo2` BEFORE DELETE ON `usuarios` FOR EACH ROW BEGIN
  UPDATE equipo
  SET presidente = NULL
  WHERE presidente = OLD.id;
END
$$
DELIMITER ;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `equipo`
--
ALTER TABLE `equipo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_presidente` (`presidente`);

--
-- Indices de la tabla `goles`
--
ALTER TABLE `goles`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_goles_equipo` (`id_equipo`),
  ADD KEY `fk_goles_partido` (`id_partido`),
  ADD KEY `fk_goles_jugador` (`id_jugador`);

--
-- Indices de la tabla `partido`
--
ALTER TABLE `partido`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idEq1` (`idEq1`),
  ADD KEY `idEq2` (`idEq2`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre_usuario` (`nombre_usuario`),
  ADD KEY `fk_equipo` (`equipo`),
  ADD KEY `equipo_jug` (`equipo_jug`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `equipo`
--
ALTER TABLE `equipo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `goles`
--
ALTER TABLE `goles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38773;

--
-- AUTO_INCREMENT de la tabla `partido`
--
ALTER TABLE `partido`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `equipo`
--
ALTER TABLE `equipo`
  ADD CONSTRAINT `fk_presidente` FOREIGN KEY (`presidente`) REFERENCES `usuarios` (`id`);

--
-- Filtros para la tabla `goles`
--
ALTER TABLE `goles`
  ADD CONSTRAINT `fk_goles_equipo` FOREIGN KEY (`id_equipo`) REFERENCES `equipo` (`id`),
  ADD CONSTRAINT `fk_goles_jugador` FOREIGN KEY (`id_jugador`) REFERENCES `usuarios` (`id`),
  ADD CONSTRAINT `fk_goles_partido` FOREIGN KEY (`id_partido`) REFERENCES `partido` (`id`);

--
-- Filtros para la tabla `partido`
--
ALTER TABLE `partido`
  ADD CONSTRAINT `fk_ideq1` FOREIGN KEY (`idEq1`) REFERENCES `equipo` (`id`),
  ADD CONSTRAINT `fk_ideq2` FOREIGN KEY (`idEq2`) REFERENCES `equipo` (`id`);

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `fk_equipo` FOREIGN KEY (`equipo`) REFERENCES `equipo` (`id`) ON DELETE SET NULL;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
