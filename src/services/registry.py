import csv
from pathlib import Path


class CompanyRegistry:
    """
    Reads the company registry.
    """

    def __init__(self):
        self.registry_path = (
            Path(__file__).resolve().parents[2]
            / "data"
            / "company_registry.csv"
        )

    def get_companies(self):
        with open(
            self.registry_path,
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            return list(reader)