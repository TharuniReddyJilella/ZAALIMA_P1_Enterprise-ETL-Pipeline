import sqlite3
from pathlib import Path
from app.logger.logger import get_logger


class SQLiteLoader:
    def __init__(self):
        Path("data/database").mkdir(parents=True, exist_ok=True)

        self.connection = sqlite3.connect("data/database/enterprise.db")

        self.logger = get_logger()

    def load(self, dataframe, table_name):
        dataframe.to_sql(
            table_name,
            self.connection,
            if_exists="replace",
            index=False,
        )

        self.logger.info(
            f"Loaded {len(dataframe)} rows into SQLite table '{table_name}'"
        )

    def close(self):
        self.connection.close()