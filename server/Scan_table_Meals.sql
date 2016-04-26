
-- --------------------------------------------------------

--
-- Table structure for table `Meals`
--

CREATE TABLE `Meals` (
  `meal_id` int(11) NOT NULL,
  `scantime` datetime NOT NULL,
  `meal` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `location` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `code` varchar(250) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
