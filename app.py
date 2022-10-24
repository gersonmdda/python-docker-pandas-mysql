import time
import pandas as pd
import redis
from flask import Flask
import logging

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)
logging.basicConfig(level=logging.DEBUG)


def readCsv():
    df = pd.read_csv('exemplo.csv')
    #for x in df:
        #   app.logger.info(df.iloc[2,2])
    for index, row in df.iterrows():
            #app.logger.info(row.Jogo)
    return df.to_string()

@app.route('/')
def hello():
    teste = readCsv()
    return teste