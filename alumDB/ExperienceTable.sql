CREATE TABLE IF NOT EXISTS experience (
	pID int(5) NOT NULL,
    pos_title varchar(200),
    company_name varchar(200) NOT NULL,
    pos_summary text,
    pos_start_month int(2) NOT NULL,
    pos_start_year int(4) NOT NULL,
    pos_end_month int(2),
    pos_end_year int(4),
    location text,
    exp_source text,
    PRIMARY KEY(pID,pos_title,company_name,pos_start_month,pos_start_year,pos_end_month,pos_end_year),
    FOREIGN KEY (pID) references person (pID) ON DELETE CASCADE
);