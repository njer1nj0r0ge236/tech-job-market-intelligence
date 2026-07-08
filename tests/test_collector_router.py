from src.services.collector_router import CollectorRouter

router = CollectorRouter()

# collector = router.get_collector("Greenhouse")

# print(type(collector))

collector = router.get_collector("Ashby")

print(collector)