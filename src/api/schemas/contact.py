from pydantic import BaseModel, EmailStr, ConfigDict


class ContactListSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    first_name: str
    last_name: str
    email: EmailStr
