import time
import pandas as pd
import redis
from flask import Flask
import logging
import mysql.connector
import os

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)
logging.basicConfig(level=logging.DEBUG)
mydb = mysql.connector.connect(
  host=os.environ['MYSQL_ROOT_HOST'],
  port=os.environ['MYSQL_ROOT_PORT'],
  user=os.environ['MYSQL_USER'],
  password=os.environ['MYSQL_ROOT_PASSWORD'],
  database=os.environ['MYSQL_DATABASE']
)


def connectMysql(row):
    mycursor = mydb.cursor()
    sql = "INSERT INTO games (jogo, consoles, status) VALUES (%s, %s, %s)"
    val = (row.Jogo, row.Consoles, row.Status)
    mycursor.execute(sql, val)
    mydb.commit()


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