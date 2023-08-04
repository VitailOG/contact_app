import sqlalchemy as sa

from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import TSVECTOR

Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"
    id = sa.Column(sa.Integer, sa.Identity(always=True))
    first_name = sa.Column(sa.UnicodeText)
    last_name = sa.Column(sa.UnicodeText)
    email = sa.Column(sa.UnicodeText)
    tsv = sa.Column(TSVECTOR)

    __table_args__ = (
        sa.PrimaryKeyConstraint("id"),
        sa.Index('idx_tsv', tsv, postgresql_using='gin')
    )
