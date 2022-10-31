import mysql.connector
import os

class DatabaseMysql:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host=os.environ['MYSQL_ROOT_HOST'],
            port=os.environ['MYSQL_ROOT_PORT'],
            user=os.environ['MYSQL_USER'],
            password=os.environ['MYSQL_ROOT_PASSWORD'],
            database=os.environ['MYSQL_DATABASE']
        )

    def connectMysql(self,row):
        mycursor = self.mydb.cursor()
        sql = "INSERT INTO games (jogo, consoles, status) VALUES (%s, %s, %s)"
        val = (row.Jogo, row.Consoles, row.Status)
        mycursor.execute(sql, val)
        self.mydb.commit()