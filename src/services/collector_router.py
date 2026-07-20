from src.collectors.greenhouse.collector import GreenhouseCollector
from src.collectors.ashby.collector import AshbyCollector
from src.collectors.workable.collector import WorkableCollector
from src.collectors.breezy.collector import BreezyCollector

class CollectorRouter:
    """
    Chooses the correct collector based on the ATS.
    """

    def __init__(self):
        self.collectors = {
            "Greenhouse": GreenhouseCollector(),
            # We'll add Ashby here next.
            "Ashby": AshbyCollector(),
            "Workable": WorkableCollector(),
            "BreezyHR": BreezyCollector(),
        }

    def get_collector(self, ats: str):
        
        return self.collectors.get(ats)