from src.services.registry import CompanyRegistry

registry = CompanyRegistry()

companies = registry.get_companies()

print(f"Companies loaded: {len(companies)}")

print()

print(companies[0])