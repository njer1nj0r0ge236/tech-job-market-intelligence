from src.collectors.greenhouse.collector import GreenhouseCollector


class CollectorRouter:
    """
    Chooses the correct collector based on the ATS.
    """

    def __init__(self):
        self.collectors = {
            "Greenhouse": GreenhouseCollector(),
            # We'll add Ashby here next.
            # "Ashby": AshbyCollector(),
        }

    def get_collector(self, ats: str):
        return self.collectors.get(ats)