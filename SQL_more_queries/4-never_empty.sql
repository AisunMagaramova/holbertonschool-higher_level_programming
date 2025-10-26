-- id_not_null deyeri olan cedvel yarat
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT default 1,
	name VARCHAR(256) NOT NULL
);
