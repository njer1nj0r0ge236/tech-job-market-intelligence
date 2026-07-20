import requests


class AshbyClient:
    """
    Handles communication with the Ashby Jobs API.
    """

    BASE_URL = "https://jobs.ashbyhq.com/api/non-user-graphql"

    def get_jobs(self, organization_slug: str) -> list:
        """
        Fetch all public jobs from an Ashby organization.
        """

        payload = {
            "operationName": "ApiJobBoardWithTeams",
            "variables": {
                "organizationHostedJobsPageName": organization_slug,
            },
            "query": """
            query ApiJobBoardWithTeams($organizationHostedJobsPageName: String!) {
              jobBoard: jobBoardWithTeams(
                organizationHostedJobsPageName: $organizationHostedJobsPageName
              ) {
                teams {
                  jobs {
                    id
                    title
                    location
                    employmentType
                    secondaryLocations {
                      location
                    }
                  }
                }
              }
            }
            """
        }

        response = requests.post(
            self.BASE_URL,
            json=payload,
            timeout=30
        )

        response.raise_for_status()

        data = response.json()
        
        print(data)
        
        return []

        # data = response.json()

        # teams = data["data"]["jobBoard"]["teams"]

        jobs = []

        for team in teams:
            jobs.extend(team["jobs"])

        return jobs