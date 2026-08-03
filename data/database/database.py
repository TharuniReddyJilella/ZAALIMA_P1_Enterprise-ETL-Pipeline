from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///data/database/enterprise.db"

engine = create_engine(
    DATABASE_URL,
    echo=True
)
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)
if __name__ == "__main__":
    session = SessionLocal()

    print("Session created successfully!")

    session.close()