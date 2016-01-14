-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jan 14, 2016 at 03:41 PM
-- Server version: 5.5.46-0ubuntu0.14.04.2
-- PHP Version: 5.5.9-1ubuntu4.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `JCAssets`
--

-- --------------------------------------------------------

--
-- Table structure for table `Servers`
--

CREATE TABLE IF NOT EXISTS `Servers` (
  `sno` varchar(40) NOT NULL,
  `name` varchar(50) NOT NULL,
  `vendor` varchar(30) NOT NULL,
  `rackno` varchar(10) NOT NULL,
  `runits` varchar(30) NOT NULL,
  `mgmt_ip` varchar(16) NOT NULL,
  `Status` varchar(100) NOT NULL,
  PRIMARY KEY (`sno`),
  KEY `sno` (`sno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Server_DESC`
--

CREATE TABLE IF NOT EXISTS `Server_DESC` (
  `sno` varchar(40) NOT NULL,
  `type` varchar(40) NOT NULL,
  `hostname` varchar(30) NOT NULL,
  `role` varchar(30) NOT NULL,
  `owner` varchar(30) NOT NULL,
  `data_ip` varchar(16) NOT NULL,
  PRIMARY KEY (`sno`),
  KEY `sno` (`sno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `User`
--

CREATE TABLE IF NOT EXISTS `User` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `password_hash` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;