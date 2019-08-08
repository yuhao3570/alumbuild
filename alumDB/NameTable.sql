CREATE TABLE IF NOT EXISTS name_table (
	Id int(5) NOT NULL AUTO_INCREMENT,
    pID int(5) NOT NULL, FOREIGN KEY(pID) REFERENCES person(pID) ON DELETE CASCADE,
    first_name varchar(30) NOT NULL,
    last_name varchar(30) NOT NULL,
    deg_start_year int(4),
    name_changed varchar(1),
    type_code varchar(10),
    activity_date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    update_date varchar(20) NOT NULL DEFAULT '2018-01-01',
    PRIMARY KEY (Id, pID)
);
