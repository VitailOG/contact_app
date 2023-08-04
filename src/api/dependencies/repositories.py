from typing import Annotated

from fastapi import Depends

from src.api.dependencies.db import get_repository
from src.repositories.contact import ContactRepository


ContactDependency = Annotated[ContactRepository, Depends(get_repository(ContactRepository))]
