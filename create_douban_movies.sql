CREATE TABLE `movies` (
  `url` varchar(256) NOT NULL,
  `title` varchar(128) DEFAULT NULL,
  `score` float(4,1) DEFAULT NULL,
  `commenter_counts` int(11) DEFAULT NULL,
  `tags` varchar(512) DEFAULT NULL,
  `actors` varchar(512) DEFAULT NULL,
  `related_info` text,
  `img` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8 
