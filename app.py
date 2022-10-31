import time
import redis
from flask import Flask
from csvReader import CsvReader
import logging


app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)
logging.basicConfig(level=logging.DEBUG)


@app.route('/', methods=["POST"])
def hello():
    app.logger.info('TESTE')
    csv = CsvReader()
    teste = csv.readCsv()
    return teste