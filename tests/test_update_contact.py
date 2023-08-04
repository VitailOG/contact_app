import pytest

from sqlalchemy import select

from src.models.contact import Contact
from src.services.update_contacts import update_contact
from tests.conftest import sync_test_session
from tests.mock_response import MockResponse


@pytest.fixture
def fetch_data(mocker):
    return mocker.patch("src.services.api_requests.httpx.get", return_value=MockResponse())


def test_ex(fetch_data):
    with sync_test_session() as dbsession:
        def get_email():
            return dbsession.execute(
                select(Contact.email)
                .where(Contact.last_name == 'Ferrara', Contact.first_name == 'Jon')
            ).scalar()

        assert get_email() == "randomemail@nimble.com"
        update_contact(dbsession)
        assert get_email() == "care@nimble.com"

        fetch_data.assert_called()
