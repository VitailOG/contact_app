import pytest
from httpx import AsyncClient


pytestmark = [pytest.mark.asyncio]


async def test_contact_list(aclient: AsyncClient):
    response = await aclient.get("/list", params={"contact": "mystylename@gmail.com"})
    assert response.status_code == 200
    assert response.json() == [{'first_name': 'Oleg', 'last_name': 'Mishyn', 'email': 'mystylename@gmail.com'}]


async def test_contact_list_not_found(aclient: AsyncClient):
    response = await aclient.get("/list", params={"contact": "name"})
    assert response.status_code == 200
    assert response.json() == []
