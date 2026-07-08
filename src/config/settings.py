from pathlib import Path

from dotenv import load_dotenv
import os

# Project root
BASE_DIR = Path(__file__).resolve().parents[2]

# Load environment variables
load_dotenv(BASE_DIR / ".env")


DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

required_settings = {
    "DATABASE_HOST": DATABASE_HOST,
    "DATABASE_PORT": DATABASE_PORT,
    "DATABASE_NAME": DATABASE_NAME,
    "DATABASE_USER": DATABASE_USER,
    "DATABASE_PASSWORD": DATABASE_PASSWORD,
}

missing = [key for key, value in required_settings.items() if not value]

if missing:
    raise ValueError(
        f"Missing required environment variables: {', '.join(missing)}"
    )