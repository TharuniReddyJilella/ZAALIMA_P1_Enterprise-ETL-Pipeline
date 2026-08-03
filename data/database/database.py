from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///data/database/enterprise.db"

engine = create_engine(
    DATABASE_URL,
    echo=True
)
if __name__ == "__main__":
    connection = engine.connect()

    print("Database connected successfully!")

    connection.close()