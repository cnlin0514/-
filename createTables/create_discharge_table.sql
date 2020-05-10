CREATE DATABASE IF NOT EXISTS `zjkhmr` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE zjkhmr;

CREATE TABLE IF NOT EXISTS `hospital_discharge_certificate`(
  `id` INT(15) UNSIGNED AUTO_INCREMENT NOT NULL ,
  `his` VARCHAR(20),
	`bah` VARCHAR(10),
  `blh` INT(10),
  `name` VARCHAR(20),
	`department` VARCHAR(20),
	`ch` INT(10),
	`admission_time` VARCHAR (20),
	`discharge_time` VARCHAR(20),
	`location` VARCHAR(255),
	`discharge_diagnosis` VARCHAR(500),
	`inhospital_course` VARCHAR(2000),
	`discharge_medicine` VARCHAR(500),
	`attention` VARCHAR(1000),
	`admission_id` INT (15) UNSIGNED,
  PRIMARY KEY(`id`),
	FOREIGN KEY (`admission_id`) REFERENCES hospital_admission_record(`id`)
) ENGINE = INNODB;