#!/usr/bin/python3
import MySQLdb
import sys

# Əgər skript birbaşa icra edilirsə
if __name__ == "__main__":
    # Argumentləri al
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # MySQL serverinə qoşul
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database)

    # Cursor yarad
    cur = db.cursor()

    # States cədvəlini seç və sıralı şəkildə məlumatları al
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Bütün nəticələri al
    rows = cur.fetchall()

    # Nəticələri çap et
    for row in rows:
        print(row)

    # Bağlantını bağla
    cur.close()
    db.close()
