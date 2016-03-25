-- phpMyAdmin SQL Dump
-- version 4.2.12deb2+deb8u1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 25, 2016 at 10:02 AM
-- Server version: 5.5.44-0+deb8u1
-- PHP Version: 5.6.17-0+deb8u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `bank`
--

-- --------------------------------------------------------

--
-- Table structure for table `cards`
--

CREATE TABLE IF NOT EXISTS `cards` (
`id` int(11) unsigned NOT NULL,
  `userId` int(10) unsigned NOT NULL,
  `tagId` varchar(18) NOT NULL,
  `atmpin` varchar(200) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `cards`
--

INSERT INTO `cards` (`id`, `userId`, `tagId`, `atmpin`) VALUES
(1, 1234, '04DA08EAFC3880', 'b59c67bf196a4758191e42f76670ceba'),
(2, 1235, '3EC8EC75', '934b535800b1cba8f96a5d72f72f1611');

-- --------------------------------------------------------

--
-- Table structure for table `readings`
--

CREATE TABLE IF NOT EXISTS `readings` (
`id` bigint(11) unsigned NOT NULL,
  `tagId` varchar(18) NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `action` int(2) unsigned NOT NULL,
  `amtpay` int(11) NOT NULL DEFAULT '0',
  `current` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=84 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `readings`
--

INSERT INTO `readings` (`id`, `tagId`, `time`, `action`, `amtpay`, `current`) VALUES
(3, '04DA08EAFC3880', '2016-03-24 10:24:20', 1, 0, 0),
(4, '3EC8EC75', '2016-03-24 10:24:25', 1, 0, 0),
(5, 'C4A027D0', '2016-03-24 10:24:29', 1, 0, 0),
(6, '04DA08EAFC3880', '2016-03-24 10:29:30', 1, 0, 0),
(7, '3EC8EC75', '2016-03-24 10:29:41', 1, 0, 0),
(8, '3EC8EC75', '2016-03-24 10:36:40', 1, 0, 0),
(9, '3EC8EC75', '2016-03-24 10:51:54', 1, 0, 0),
(10, '3EC8EC75', '2016-03-24 10:54:26', 1, 0, 0),
(11, '3EC8EC75', '2016-03-24 10:55:52', 1, 0, 0),
(47, '04DA08EAFC3880', '2016-03-24 15:44:55', 1, 0, 0),
(53, '04DA08EAFC3880', '2016-03-25 06:46:44', 1, 0, 0),
(56, '04DA08EAFC3880', '2016-03-25 06:58:38', 1, 0, 0),
(57, '3EC8EC75', '2016-03-25 06:59:38', 1, 0, 0),
(58, '3EC8EC75', '2016-03-25 07:01:31', 1, 450, 0),
(64, 'C4A027D0', '2016-03-25 07:30:20', 1, 0, 0),
(65, '3EC8EC75', '2016-03-25 07:30:29', 1, 250, 0),
(66, '3EC8EC75', '2016-03-25 07:31:46', 1, 199, 0),
(67, '3EC8EC75', '2016-03-25 07:32:52', 1, 199, 0),
(68, '04DA08EAFC3880', '2016-03-25 07:36:07', 1, 450, 0),
(69, '04DA08EAFC3880', '2016-03-25 07:36:49', 1, 200, 0),
(70, 'D22B1300', '2016-03-25 07:40:00', 1, 0, 0),
(71, 'D22B1300', '2016-03-25 07:40:51', 1, 0, 0),
(72, 'D22B1300', '2016-03-25 07:41:02', 1, 0, 0),
(73, 'C4A027D0', '2016-03-25 07:54:27', 1, 0, 0),
(74, '04DA08EAFC3880', '2016-03-25 07:54:54', 1, 1000, 0),
(75, '04DA08EAFC3880', '2016-03-25 07:55:42', 1, 1000, 0),
(76, '04DA08EAFC3880', '2016-03-25 07:57:21', 1, 1, 0),
(77, '04DA08EAFC3880', '2016-03-25 08:06:36', 1, 100, 0),
(78, '04DA08EAFC3880', '2016-03-25 08:51:48', 1, 100, 0),
(79, '04DA08EAFC3880', '2016-03-25 08:52:46', 1, 20, 0),
(80, '04DA08EAFC3880', '2016-03-25 08:53:29', 1, 20, 0),
(81, '04DA08EAFC3880', '2016-03-25 08:54:16', 1, 60, 0),
(82, '04DA08EAFC3880', '2016-03-25 08:56:17', 1, 1, 0),
(83, '04DA08EAFC3880', '2016-03-25 08:56:45', 1, 1, 0);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE IF NOT EXISTS `users` (
`id` int(10) unsigned NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_czech_ci NOT NULL,
  `surname` varchar(255) CHARACTER SET utf8 COLLATE utf8_czech_ci NOT NULL,
  `balance` int(11) NOT NULL,
  `active` enum('0','1') CHARACTER SET utf8 COLLATE utf8_czech_ci NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=1236 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `surname`, `balance`, `active`) VALUES
(1234, 'Prabhjeet', 'Singh', 12439, '1'),
(1235, 'Rohit', 'Kumar', 16652, '1');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cards`
--
ALTER TABLE `cards`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `readings`
--
ALTER TABLE `readings`
 ADD PRIMARY KEY (`id`);

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
MODIFY `id` int(11) unsigned NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `readings`
--
ALTER TABLE `readings`
MODIFY `id` bigint(11) unsigned NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=84;
--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
MODIFY `id` int(10) unsigned NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=1236;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
