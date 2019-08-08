CREATE TABLE IF NOT EXISTS person (
  pID int(5) NOT NULL AUTO_INCREMENT,
  first_name varchar(30) NOT NULL,
  last_name varchar(30) NOT NULL,
  email varchar(255) DEFAULT NULL,
  subject_field varchar(30) DEFAULT NULL,
  degree varchar(5) DEFAULT NULL,
  deg_start_month int(2) NOT NULL,
  deg_start_year int(4) NOT NULL,
  deg_end_month int(2) DEFAULT NULL,
  deg_end_year int(4) DEFAULT NULL,
  deg_received char(1) NOT NULL,
  name_changed tinyint(1) DEFAULT NULL,
  PRIMARY KEY (pID, first_name, last_name, deg_start_year)
);