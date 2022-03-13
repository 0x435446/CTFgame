-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 13, 2022 at 06:27 PM
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
(1, 'Network Forensics 1', 'HackIT{e0603c499aae47eb89343ad0ef3178e044c62e70ae2309b35591d1d49a3211ec}', '-', 0, -1, './Challenges/Baby_HTTP.pcapng', 'Networking', 15, '0x435446', 0),
(2, 'Web 1', 'HackIT{Yummi_My_j@R_of_C0okie5}', '-', 0, -1, 'http://92.81.21.126:40000', 'Web', 15, '0x435446', 0),
(3, 'Web 2', 'HackIT{XSSRUlezz}', '-', 0, -1, 'http://92.81.21.126:40001', 'Web', 15, '0x435446', 0),
(4, 'Web 3', 'HackIT{__public_g1t__}', '-', 0, -1, 'http://92.81.21.126:40002', 'Web', 15, '0x435446', 0),
(5, 'Web 4', 'HackIT{imageinf0_i5_Th@t_1mportant??}', '-', 0, -1, 'http://92.81.21.126:40003', 'Web', 15, '0x435446', 0),
(6, 'Web 5', 'HackIT{ce635c4eabff5e4f56dba8fb1e39ca235530aa2b6b18533eef1af3862016c577}', '-', 0, -1, 'http://92.81.21.126:40004', 'Web', 15, '0x435446', 0),
(7, 'Web 6', 'HackIT{Command_Inj3c10n}', '-', 0, -1, 'http://92.81.21.126:40005', 'Web', 15, '0x435446', 0),
(8, 'Web 7', 'HackIT{phpArchives_Compact_as_Jh0nny_Bravo_Muscles}', '-', 0, -1, 'http://92.81.21.126:40006', 'Web', 15, '0x435446', 0),
(9, 'Web 8', 'HackIT{Typ3_Juggl1ng_15_th@@@t_fun}', '-', 0, -1, 'http://92.81.21.126:40007', 'Web', 15, '0x435446', 0),
(10, 'Web 9', 'HackIT{X-Forwarded-For-cuDeToate}', '-', 0, -1, 'http://92.81.21.126:40008', 'Web', 15, '0x435446', 0),
(11, 'Web 10', 'HackIT{Training1_c0mpleted}', '-', 0, -1, 'http://92.81.21.126:40009', 'Web', 15, '0x435446', 0),
(12, 'Web 11', 'HackIT{Training2_Juggling}', '-', 0, -1, 'http://92.81.21.126:40010', 'Web', 15, '0x435446', 0),
(13, 'Web 12', 'HackIT{Javascript_Sanitization_15_n0t_th@t_s3cure}', '-', 0, -1, 'http://92.81.21.126:40011', 'Web', 15, '0x435446', 0),
(14, 'Web 13', 'HackIT{R3placement_Sanitization_n3v3r_w0rks}', '-', 0, -1, 'http://92.81.21.126:40012', 'Web', 15, '0x435446', 0),
(15, 'Web 14', 'HackIT{J@vascript_credent1als?!?!}', '-', 0, -1, 'http://92.81.21.126:40013', 'Web', 15, '0x435446', 0);

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
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
