-- phpMyAdmin SQL Dump
-- version 4.2.12deb2+deb8u1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 31, 2016 at 12:00 AM
-- Server version: 5.5.44-0+deb8u1
-- PHP Version: 5.6.17-0+deb8u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `pi`
--

-- --------------------------------------------------------

--
-- Table structure for table `cards`
--

CREATE TABLE IF NOT EXISTS `cards` (
`id` int(11) unsigned NOT NULL,
  `userId` int(10) unsigned NOT NULL,
  `tagId` bigint(18) unsigned NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `cards`
--

INSERT INTO `cards` (`id`, `userId`, `tagId`) VALUES
(1, 1200, 19616039208147),
(2, 1201, 62200236117111),
(3, 1202, 210111230162);

-- --------------------------------------------------------

--
-- Table structure for table `readings`
--

CREATE TABLE IF NOT EXISTS `readings` (
  `tagId` bigint(18) unsigned NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `action` int(2) unsigned NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `readings`
--

INSERT INTO `readings` (`tagId`, `date`, `time`, `action`) VALUES
(1364218894, '2016-03-25', '20:25:51', 1),
(210111230162, '2016-03-26', '08:22:35', 1),
(210111230162, '2016-03-26', '08:22:58', 2),
(210111230162, '2016-03-26', '08:22:46', 3),
(210111230162, '2016-03-26', '08:22:53', 4),
(19616039208147, '2016-03-25', '20:26:00', 1),
(19616039208147, '2016-03-25', '20:26:11', 2),
(19616039208147, '2016-03-25', '20:26:04', 3),
(19616039208147, '2016-03-25', '20:26:07', 4),
(62200236117111, '2016-03-25', '20:24:40', 1),
(62200236117111, '2016-03-25', '20:24:57', 2),
(62200236117111, '2016-03-25', '20:24:49', 3),
(62200236117111, '2016-03-25', '20:24:53', 4);

-- --------------------------------------------------------

--
-- Table structure for table `total_hours`
--

CREATE TABLE IF NOT EXISTS `total_hours` (
  `tagId` bigint(19) NOT NULL,
  `date` date NOT NULL,
  `hours` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `total_hours`
--

INSERT INTO `total_hours` (`tagId`, `date`, `hours`) VALUES
(210111230162, '2016-03-26', '00:00:16'),
(19616039208147, '2016-03-25', '00:00:17'),
(62200236117111, '2016-03-25', '00:00:13');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE IF NOT EXISTS `users` (
`id` int(10) unsigned NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_czech_ci NOT NULL,
  `surname` varchar(255) CHARACTER SET utf8 COLLATE utf8_czech_ci NOT NULL,
  `active` enum('0','1') CHARACTER SET utf8 COLLATE utf8_czech_ci NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=1203 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `surname`, `active`) VALUES
(1200, 'Prabhjeet', 'Singh Chawla', '1'),
(1201, 'Rohit', 'Kumar', '1'),
(1202, 'Prabh', 'Singh', '1');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cards`
--
ALTER TABLE `cards`
 ADD PRIMARY KEY (`id`), ADD KEY `tagId` (`tagId`), ADD KEY `userId` (`userId`);

--
-- Indexes for table `readings`
--
ALTER TABLE `readings`
 ADD PRIMARY KEY (`tagId`,`date`,`action`);

--
-- Indexes for table `total_hours`
--
ALTER TABLE `total_hours`
 ADD PRIMARY KEY (`tagId`,`date`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
 ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cards`
--
ALTER TABLE `cards`
MODIFY `id` int(11) unsigned NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
MODIFY `id` int(10) unsigned NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=1203;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `cards`
--
ALTER TABLE `cards`
ADD CONSTRAINT `cards_ibfk_1` FOREIGN KEY (`userId`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
