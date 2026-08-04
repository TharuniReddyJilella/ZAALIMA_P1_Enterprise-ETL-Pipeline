from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

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
Base = declarative_base()

if __name__ == "__main__":
    session = SessionLocal()

    print("Session created successfully!")

    session.close()