from httpx import Response


class MockResponse(Response):

    def __init__(self, status: int = 200, *args, **kwargs):
        super().__init__(status, *args, **kwargs)

    def json(self):
        return{
            "resources": [
                {
                    "record_type": "person",
                    "fields": {
                        "email": [
                            {
                                "label": "email",
                                "modifier": "work",
                                "value": "care@nimble.com",
                                "is_primary": False
                            }
                        ],
                        "first name": [
                            {
                                "label": "first name",
                                "modifier": "",
                                "value": "Jon",
                                "is_primary": False
                            }
                        ],
                        "last name": [
                            {
                                "label": "last name",
                                "modifier": "",
                                "value": "Ferrara",
                                "is_primary": False
                            }
                        ]
                    },
                }
            ]
        }

    def raise_for_status(self):
        return None
