import httpx


class APIRequester:
    url = "https://api.nimble.com/api/v1/contacts/"
    headers = {'Authorization': 'Bearer NxkA2RlXS3NiR8SKwRdDmroA992jgu'}
    params = {"fields": "email,first name,last name"}

    @classmethod
    def fetch(cls):
        response = httpx.get(cls.url, headers=cls.headers, params=cls.params)

        response.raise_for_status()

        return response

    @classmethod
    def json(cls):
        return cls.fetch().json()
