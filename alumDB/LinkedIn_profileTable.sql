CREATE TABLE IF NOT EXISTS linkedin_profile (
	pID int(11) NOT NULL,
    headline varchar(250),
    location varchar(100),
    summary text,
    url text,
    url_checked tinyint(1) DEFAULT '0',
    url_added_manually tinyint(1) DEFAULT '0',
    no_linkedin_known tinyint(1) DEFAULT '0',
    url_changed tinyint(1) DEFAULT '0',
    last_date_scraped datetime,
    PRIMARY KEY (pID),
    FOREIGN KEY (pID) references person (pID) ON DELETE CASCADE
);
