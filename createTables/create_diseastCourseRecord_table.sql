CREATE DATABASE IF NOT EXISTS `zjkhmr` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE zjkhmr;

CREATE TABLE IF NOT EXISTS `disease_course_record`(
  `id` INT(15) UNSIGNED AUTO_INCREMENT NOT NULL ,
  `his` VARCHAR(20),
	`bah` VARCHAR(10),
  `blh` INT(10),
	`check_record` MEDIUMTEXT,
	`admission_id` int(15) UNSIGNED,
  PRIMARY KEY(`id`),
	FOREIGN KEY (`admission_id`) REFERENCES hospital_admission_record(`id`) ON DELETE SET NULL 
) ENGINE = INNODB;