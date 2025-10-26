-- unique_id deyeri qaytaran scrip yarat
CREATE TABLE IF NOT EXISTS unique_id (
	id INT default 1 UNIQUE,
	name VARCHAR(256) NOT NULL
	);
