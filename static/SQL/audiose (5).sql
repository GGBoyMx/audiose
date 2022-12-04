-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-11-2022 a las 23:53:26
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `audiose`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id` int(11) NOT NULL,
  `precio` int(8) NOT NULL,
  `descripcion` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `metodoenvio` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `imagen` varchar(20) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id`, `precio`, `descripcion`, `metodoenvio`, `imagen`) VALUES
(23, 100, 'KZ SNZ Pro', 'UPS', 'img1.jpg'),
(24, 464, 'KZ Xrs SE', 'Correosmx', 'img12.jpg'),
(25, 984, 'KZ SNZ X', 'FEDEX', 'img3.jpg'),
(27, 632, 'KZ ZST ', 'UPS', 'img4.jpg'),
(28, 960, 'KZ Terminator', 'FEDEX', 'img5.jpg'),
(29, 960, 'KZ Terminator', 'FEDEX', 'img5.jpg'),
(30, 784, 'Sony RE ', 'DHL', 'img6.jpg'),
(31, 1300, 'OVO 13', 'CorreosMx', 'img8.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `apellidos` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `correo` varchar(80) COLLATE utf8_spanish_ci NOT NULL,
  `password` varchar(110) COLLATE utf8_spanish_ci NOT NULL,
  `telefono` varchar(15) COLLATE utf8_spanish_ci NOT NULL,
  `edad` int(4) NOT NULL,
  `pais` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `estado` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `municipio` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `cp` int(7) NOT NULL,
  `colonia` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `calle` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `fechanac` date NOT NULL,
  `perfil` char(1) COLLATE utf8_spanish_ci NOT NULL DEFAULT 'U'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `nombre`, `apellidos`, `correo`, `password`, `telefono`, `edad`, `pais`, `estado`, `municipio`, `cp`, `colonia`, `calle`, `fechanac`, `perfil`) VALUES
(1, 'Admin', 'admin', 'admin@gmail.com', 'pbkdf2:sha256:260000$eq7D8aFhXy60dZ19$aa5dd805b5719cacc49d5b52fac4f8c536102faf47cd91ba6ae36c204976afee', '3322121', 989, 'jnjknjk', 'njknjkn', 'jknjkn', 0, 'njn', 'njknk', '8989-09-08', 'A'),
(2, 'Cesar David', 'Arteaga Vazquez', 'davidarteaga495@gmail.com', 'pbkdf2:sha256:260000$LVHipbBthcOT78fI$1ccdee4d1abc2b0716e146a2d4cf454acdfec821fcc9cb001c849870e98101a2', '3322134064', 18, 'mexico', 'jalisco', 'zapopan', 45189, 'M', 'Carlos 17', '2004-10-26', 'U'),
(4, 'user', 'user', 'user@gmail.com', 'pbkdf2:sha256:260000$8w5AsG2Zp0tVOH3M$f7f016e3e17826304148f8c870e26531d2c84e4a5952750ce8405cfcbb9cf7bd', '3232323', 18, 'fyftf', 'tftrf', 'tygtg', 0, 'ºtgygy', 'gty', '2022-11-21', 'U');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
