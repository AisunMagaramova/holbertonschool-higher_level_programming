-- cedvelde eyni olanlari sadala
-- azalan sira ile sadala
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
