-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 02, 2024 at 05:21 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flight`
--

-- --------------------------------------------------------

--
-- Table structure for table `city`
--

CREATE TABLE `city` (
  `city_id` int(11) NOT NULL,
  `city_name` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `city`
--

INSERT INTO `city` (`city_id`, `city_name`) VALUES
(1, 'Tehran'),
(2, 'Mashhad'),
(3, 'Yasouj'),
(4, 'Arak'),
(5, 'Tabriz'),
(6, 'Rasht'),
(7, 'Zahedan'),
(8, 'Ilam'),
(9, 'Isfehan'),
(10, 'Qom'),
(11, 'Bojnord'),
(12, 'Gorgan'),
(13, 'Yazd'),
(14, 'Ahvaz'),
(15, 'Boshehr'),
(16, 'Semnan'),
(17, 'BandarAbas'),
(18, 'Kerman'),
(19, 'Sari'),
(20, 'Kermanshah'),
(21, 'Urmia'),
(22, 'Hamedan'),
(23, 'Shiraz'),
(24, 'Qazvin'),
(25, 'Zanjan'),
(26, 'Birjand'),
(27, 'Sanandaj'),
(28, 'KoramAbad'),
(29, 'Ardebil'),
(30, 'ShahrKord'),
(31, 'Karaj');

-- --------------------------------------------------------

--
-- Table structure for table `log`
--

CREATE TABLE `log` (
  `flight_id` int(11) NOT NULL,
  `flight_number` int(11) NOT NULL,
  `city` text NOT NULL,
  `plane` text NOT NULL,
  `action` text NOT NULL,
  `fly_date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `plane`
--

CREATE TABLE `plane` (
  `plane_id` int(11) NOT NULL,
  `plane_name` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `plane`
--

INSERT INTO `plane` (`plane_id`, `plane_name`) VALUES
(1, 'Boeing 757'),
(2, 'Ilyushin Il-96'),
(3, 'Bottom Line'),
(4, 'Airbus A330'),
(5, 'Boeing 777'),
(6, 'Airbus A380'),
(7, 'Tupolev Tu-134'),
(8, 'McDonnell MD-11'),
(9, 'Antonov An-140'),
(10, 'Lockheed L-1011');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `city`
--
ALTER TABLE `city`
  ADD PRIMARY KEY (`city_id`);

--
-- Indexes for table `log`
--
ALTER TABLE `log`
  ADD PRIMARY KEY (`flight_id`);

--
-- Indexes for table `plane`
--
ALTER TABLE `plane`
  ADD PRIMARY KEY (`plane_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `city`
--
ALTER TABLE `city`
  MODIFY `city_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `log`
--
ALTER TABLE `log`
  MODIFY `flight_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `plane`
--
ALTER TABLE `plane`
  MODIFY `plane_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
