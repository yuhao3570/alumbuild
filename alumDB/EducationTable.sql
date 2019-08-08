CREATE TABLE IF NOT EXISTS education (
	pID int(5) NOT NULL,
    dummy_index int(5)  NOT NULL,
    school_name varchar(150) NOT NULL,
    subject_field varchar(200),
    degree varchar(200),
    deg_start_year int(4) NOT NULL,
    deg_end_year text,
    deg_received char(1),
    edu_source text,
    primary key (pID, Dummy_index, school_name),
    FOREIGN KEY (pID) references person (pID) ON DELETE CASCADE
);