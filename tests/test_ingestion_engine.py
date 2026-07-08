from src.services.ingestion_engine import IngestionEngine

engine = IngestionEngine()

jobs = engine.run()

print(f"\nCollected {len(jobs)} jobs.")