CREATE DATABASE IF NOT EXISTS `zjkhmr` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE zjkhmr;

CREATE TABLE IF NOT EXISTS `first_course_record`(
  `id` INT(15) UNSIGNED AUTO_INCREMENT NOT NULL ,
  `his` VARCHAR(20),
	`bah` VARCHAR(10),
  `blh` INT(10),
  `name` VARCHAR(20),
	`admission_time` VARCHAR(255),
	`medical_record_feature` VARCHAR (2000),
	`chinese_medicine_evidence` VARCHAR (1000),
	`western_medicine_evidence` VARCHAR (1000),
	`differential_diagnosis` VARCHAR (255),
	`treatment_plan` VARCHAR(2000),
	`admission_id` int(15) UNSIGNED,
  PRIMARY KEY(`id`),
	FOREIGN KEY (`admission_id`) REFERENCES hospital_admission_record(`id`)
) ENGINE = INNODB;