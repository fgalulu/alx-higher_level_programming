-- list the number of records with the same score in the seocd_table

SELECT score, COUNT(*) AS number FROM second_table GROUP BY number DESC;
