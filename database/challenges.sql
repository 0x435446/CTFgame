-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 21, 2021 at 11:56 AM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.2.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `platformgame`
--

-- --------------------------------------------------------

--
-- Table structure for table `challenges`
--

CREATE TABLE `challenges` (
  `ID` int(11) NOT NULL,
  `Nume` varchar(256) NOT NULL,
  `Flag` varchar(1024) NOT NULL,
  `Descriere` mediumtext NOT NULL,
  `Solves` int(11) NOT NULL DEFAULT 0,
  `FirstBlood` int(11) NOT NULL DEFAULT -1,
  `Location` varchar(1024) NOT NULL,
  `Categorie` varchar(256) NOT NULL,
  `Puncte` int(11) NOT NULL,
  `Autor` varchar(256) NOT NULL,
  `Dificultate` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `challenges`
--

INSERT INTO `challenges` (`ID`, `Nume`, `Flag`, `Descriere`, `Solves`, `FirstBlood`, `Location`, `Categorie`, `Puncte`, `Autor`, `Dificultate`) VALUES
(1, 'Baby HTTP', 'HackIT{e0603c499aae47eb89343ad0ef3178e044c62e70ae2309b35591d1d49a3211ec}', 'Mai nimic', 0, -1, './Challenges/Baby_HTTP.pcapng', 'Networking', 10, '0x435446', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `challenges`
--
ALTER TABLE `challenges`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `challenges`
--
ALTER TABLE `challenges`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
