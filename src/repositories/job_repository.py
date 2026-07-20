from sqlalchemy import text

from src.database.connection import engine


class JobRepository:
    """
    Handles all database operations for jobs.
    """

    def create_table(self):
        with open("src/database/schema.sql", "r") as f:
            schema = f.read()

        with engine.begin() as connection:
            connection.execute(text(schema))

    def insert_job(self, job: dict):
        query = text("""
            INSERT INTO jobs (
                title,
                company,
                location,
                description,
                department,
                employment_type,
                posted_date,
                url,
                ats
            )
            VALUES (
                :title,
                :company,
                :location,
                :description,
                :department,
                :employment_type,
                :posted_date,
                :url,
                :ats
            )
            ON CONFLICT (url) DO NOTHING;
        """)

        with engine.begin() as connection:
            connection.execute(query, job)

    def insert_many(self, jobs: list):
        for job in jobs:
            self.insert_job(job)