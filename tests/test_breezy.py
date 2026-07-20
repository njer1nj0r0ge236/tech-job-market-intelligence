import requests
from pprint import pprint

...

data = requests.get(
    "https://synnefa.breezy.hr/json"
).json()

pprint(data[0])