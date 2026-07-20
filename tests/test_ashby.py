import requests
from pprint import pprint

url = "https://jobs.ashbyhq.com/api/non-user-graphql"

query = """
{
  __type(name: "Team") {
    fields {
      name
    }
  }
}
"""

response = requests.post(
    url,
    json={"query": query},
)

print(response.status_code)
pprint(response.json())