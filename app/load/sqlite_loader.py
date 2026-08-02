import sqlite3
from pathlib import Path


class SQLiteLoader:
    def __init__(self):
        Path("data/database").mkdir(parents=True, exist_ok=True)
        self.connection = sqlite3.connect("data/database/enterprise.db")

    def load(self, dataframe, table_name):
        dataframe.to_sql(
            table_name,
            self.connection,
            if_exists="replace",
            index=False,
        )

        print(f"\nLoaded {len(dataframe)} rows into '{table_name}' table.")

    def close(self):
        self.connection.close()