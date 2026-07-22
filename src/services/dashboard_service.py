import pandas as pd
from sqlalchemy import text

from src.database.connection import engine


class DashboardService:
    """
    Retrieves dashboard data from PostgreSQL.
    """

    def get_overview(self):
        query = text("""
            SELECT *
            FROM dashboard_overview;
        """)

        return pd.read_sql(query, engine)

    def get_company_summary(self):
        query = text("""
            SELECT *
            FROM company_summary;
        """)

        return pd.read_sql(query, engine)

    def get_ats_summary(self):
        query = text("""
            SELECT *
            FROM ats_summary;
        """)

        return pd.read_sql(query, engine)

    def get_location_summary(self):
        query = text("""
            SELECT *
            FROM location_summary;
        """)

        return pd.read_sql(query, engine)

    def get_department_summary(self):
        query = text("""
            SELECT *
            FROM department_summary;
        """)

        return pd.read_sql(query, engine)

    def get_employment_summary(self):
        query = text("""
            SELECT *
            FROM employment_summary;
        """)

        return pd.read_sql(query, engine)

    def get_remote_summary(self):
        query = text("""
            SELECT *
            FROM remote_summary;
        """)

        return pd.read_sql(query, engine)

    def get_kenya_summary(self):
        query = text("""
            SELECT *
            FROM kenya_summary;
        """)

        return pd.read_sql(query, engine)

    def get_data_roles_summary(self):
        query = text("""
            SELECT *
            FROM data_roles_summary;
        """)

        return pd.read_sql(query, engine)

    def get_software_roles_summary(self):
        query = text("""
            SELECT *
            FROM software_roles_summary;
        """)

        return pd.read_sql(query, engine)