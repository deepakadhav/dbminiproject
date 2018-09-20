'''
Created on Oct 7, 2017

@author: deepa
'''
import mysql.connector as mysql
import GUIdb as guiconf

conn = mysql.connect(**guiconf.dbconf)

GUIDB = "voter"

cursor = conn.cursor()

#cursor.execute("SHOW DATABASES")
cursor.execute("USE VOTER")

cursor.execute("INSERT INTO LIST VALUE(102,'KHAINAR','HEMANT','HIRAMAN','17/5 ROOM.NO.5 DASAK GAON','ZXRY7894','KH102')")
cursor.execute("SELECT * FROM LIST")

print(cursor.fetchall())
#print(conn)
conn.close()

if __name__ == '__main__':
    pass