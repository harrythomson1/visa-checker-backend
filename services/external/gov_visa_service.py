import httpx
from httpx import RequestError, HTTPStatusError

class ApiUnavailableError(Exception):
    pass

class GovVisaService:

    async def get_country_slugs(self):
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                url = f"https://www.gov.uk/api/content/foreign-travel-advice"
                response = await client.get(url)
                response.raise_for_status()
                data = response.json()
                details = [{'slug': child['details']['country']['slug'], 'name': child['details']['country']['name']} for child in data['links']['children']]
                return details
        except (RequestError, HTTPStatusError) as e:
            raise ApiUnavailableError("External API is currently unavailable") from e

    async def get_country_visa_details(self, country_slug):
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                url = f"https://www.gov.uk/api/content/foreign-travel-advice/{country_slug}"
                response = await client.get(url)
                response.raise_for_status()
                data = response.json()
                return data
        except (RequestError, HTTPStatusError) as e:
            raise ApiUnavailableError("External API is currently unavailable") from e

