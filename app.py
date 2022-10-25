import time
import pandas as pd
import redis
from flask import Flask
import logging
import mysql.connectors

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)
logging.basicConfig(level=logging.DEBUG)
mydb = mysql.connector.connect(
  host="0.0.0.0:3388",
  user="usuario",
  password="123456",
  database="game"
)

#ENV MYSQL_HOST=0.0.0.0:3388
#ENV MYSQL_USER=usuario
#ENV MYSQL_PASSWORD=123456
#ENV MYSQL_DATABADE=game

def connectMysql(row):
    mycursor = mydb.cursor()
    sql = "INSERT INTO games (jogo, console, status) VALUES (%s, %s, %s, %s)"
    val = (row.Jogo, row.Consoles, row.Status)
    mycursor.execute(sql, val)


def readCsv():
    df = pd.read_csv('exemplo.csv')
    #for x in df:
        #   app.logger.info(df.iloc[2,2])
    for index, row in df.iterrows():
        connectMysql(row)
    return df.to_string()

@app.route('/')
def hello():
    teste = readCsv()
    return teste