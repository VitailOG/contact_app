from src.models import session
from src.services.api_requests import APIRequester
from src.repositories.contact import ContactRepository


def transform_api_data():
    contact_data = APIRequester.json()
    for i in contact_data["resources"]:
        if i["record_type"] == "person" and "email" in i['fields']:
            yield dict(
                email=i['fields']["email"][0]['value'],
                first_name=i['fields']["first name"][0]['value'],
                last_name=i['fields']["last name"][0]['value']
            )


def update_contact(dbsession):
    for contact in transform_api_data():
        ContactRepository(dbsession).sync_update(contact, {"email": contact.pop("email")})
    dbsession.commit()
