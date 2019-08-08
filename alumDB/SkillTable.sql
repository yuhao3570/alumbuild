CREATE TABLE IF NOT EXISTS skill (
	pID int(5) NOT NULL,
    skill_name varchar(100) NOT NULL,
    endorsement int(5) DEFAULT 0,
    skill_source text,
    PRIMARY KEY (pID, skill_name, endorsement),
    FOREIGN KEY (pID) references person (pID) ON DELETE CASCADE
);
