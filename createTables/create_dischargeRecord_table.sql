CREATE DATABASE IF NOT EXISTS `zjkhmr` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE zjkhmr;

CREATE TABLE IF NOT EXISTS `discharge_record`(
  `id` INT(15) UNSIGNED AUTO_INCREMENT NOT NULL ,
  `his` VARCHAR(20),
	`bah` VARCHAR(10),
  `blh` INT(10),
	`zyh` int (10),
	`ch` int (10),
	`name` VARCHAR (20),
	`gender` VARCHAR (10),
	`age`  INT (10),
	`marial_statu` VARCHAR (10),
	`admission_time` VARCHAR (255),
	`discharge_time` VARCHAR (255),
	`hospital_discharge_location` VARCHAR (255),
	`hospital_discharge_department` VARCHAR (255),
	`operation_time` VARCHAR (255),
	`operation_name` VARCHAR (255),
	`admission_statu` VARCHAR (2000),
	`admission_diagnosis` VARCHAR (1000),
	`treatment_process` VARCHAR (2000),
	`discharge_diagnosis` VARCHAR (1000),
	`discharge_statu` VARCHAR (1000),
	`discharge_order` VARCHAR(1000),
	`admission_id` int(15) UNSIGNED,
  PRIMARY KEY(`id`),
	FOREIGN KEY (`admission_id`) REFERENCES hospital_admission_record(`id`)
) ENGINE = INNODB;