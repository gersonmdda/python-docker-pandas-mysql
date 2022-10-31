import pandas as pd
from databaseMysql import DatabaseMysql

class CsvReader:

    def readCsv(self):
        df = pd.read_csv('exemplo.csv')
        database = DatabaseMysql()
        for index, row in df.iterrows():
            database.connectMysql(row)
        return df.to_string()