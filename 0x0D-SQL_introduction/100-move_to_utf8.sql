-- Converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
-- in MySQL Server
ALTER DATABASE
	hbtn_0c_0
	CHARACTER SET utf8mb4
	COLLATE utf8mb4_unicode_ci;

-- convert table "first_table' to UTF8
USE hbtn_0c_0;
ALTER TABLE
	first_table
	CONVERT TO CHARACTER SET utf8mb4
        COLLATE utf8mb4_unicode_ci;

-- convert column 'name' to UTF8
ALTER TABLE
	first_table
	MODIFY name
	VARCHAR(256)
	CHARACTER SET utf8mb4
	COLLATE utf8mb4_unicode_ci;
