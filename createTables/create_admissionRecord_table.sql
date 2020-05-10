CREATE DATABASE IF NOT EXISTS `zjkhmr` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE zjkhmr;

CREATE TABLE IF NOT EXISTS `hospital_admission_record`(
   `id` INT(15) UNSIGNED AUTO_INCREMENT NOT NULL,
   `his` VARCHAR(20),
   `name` VARCHAR(20),
   `bah` INT(10),
   `blh` INT(10),
   `zyh` INT(10),
   `jzh` VARCHAR(10),
   `id_card` VARCHAR(20),
   `age` INT(2),
   `gender` VARCHAR(2),
   `nation` VARCHAR(255),
   `marial_status` VARCHAR(10),
   `onset_solar_term` VARCHAR(10),
   `admission_time` VARCHAR(255),
   `record_time` VARCHAR(255),
   `hospital_admit_location` VARCHAR(255),
   `hospital_admit_department` VARCHAR(255),
   `chief_complaint` VARCHAR(255),
   `present_history` VARCHAR(2000),
   `past_history` VARCHAR(255),
   `personal_history` VARCHAR(255),
   `menstrual_history` VARCHAR(255),
   `chinese_medicine_diagnosis` VARCHAR(255),
   `physical_examination` VARCHAR(1000),
   `auxiliary_examination` VARCHAR(1000),
   `primary_diagnosis` VARCHAR(255),
   PRIMARY KEY ( `id` )
) ENGINE = InnoDB;