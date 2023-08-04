from typing import Any

from sqlalchemy import select, func, update, text

from src.models.contact import Contact
from src.repositories.base import BaseRepository


class ContactRepository(BaseRepository):

    async def filter(self, value: str):
        query = (
            select(Contact)
            .where(Contact.tsv.op('@@')(func.to_tsquery('english', value)))
        )
        res = await self.dbsession.execute(query)
        return res.scalars().all()

    def sync_update(self, condition: dict[str, Any], values: dict[str, Any]):
        self.dbsession.execute(
            update(Contact)
            .where(*(getattr(Contact, field) == value for field, value in condition.items()))
            .values(**values)
        )
        update_tsv_query = text(
            """UPDATE contacts SET tsv = to_tsvector('english', concat(email, ' ', first_name, ' ', last_name))"""
        )
        self.dbsession.execute(update_tsv_query)
