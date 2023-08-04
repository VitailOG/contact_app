from typing import Annotated

from fastapi import APIRouter

from src.api.dependencies.repositories import ContactDependency
from src.api.schemas.contact import ContactListSchema

router = APIRouter()


@router.get("/list")
async def read(
    repo: ContactDependency, contact: Annotated[str, ...]
) -> list[ContactListSchema]:
    return await repo.filter(contact)
