-- convert hbtn_0c_0 db to utf8 in mysql server.

ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utfmb4_unicode_ci;
USE hbtn_0c_0;
ALTER TABLE first_table CONVERT TO CHARACTER SET utfmb4 COLLATE utfmb4_unicode_ci;
