from sqlalchemy import create_engine, text

from src.config.settings import (
    DATABASE_HOST,
    DATABASE_PORT,
    DATABASE_NAME,
    DATABASE_USER,
    DATABASE_PASSWORD,
)

DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{DATABASE_USER}:{DATABASE_PASSWORD}"
    f"@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
)

engine = create_engine(DATABASE_URL)


def test_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        print("✅ Successfully connected to PostgreSQL!")
        print(result.scalar())


if __name__ == "__main__":
    test_connection()