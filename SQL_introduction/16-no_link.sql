-- cedveldeki buutun qeydleri sadalyiriq
-- nma e sutununds dyer olmayuan yeni NULL OLANLARI SAADALAMA
-- NAME VE SCORE SADA (ORDER ILE), AZALAN SIRA ILE(DECS)
SELECT score, name
FROM second_table
WHERE 'name' IS NOT NULL
ORDER BY score DESC;
