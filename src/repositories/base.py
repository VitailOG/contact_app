from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository:

    def __init__(self, dbsession: AsyncSession | Session) -> None:
        self.dbsession = dbsession
