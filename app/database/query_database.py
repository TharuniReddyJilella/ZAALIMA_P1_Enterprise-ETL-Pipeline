import sqlite3
import pandas as pd


connection = sqlite3.connect("data/database/enterprise.db")

df = pd.read_sql("SELECT * FROM customers", connection)

print(df)

connection.close()