from sqlalchemy import Column, Integer, String
from app.database.database import Base


class Guild(Base):
    __tablename__ = "guilds"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    server = Column(String)
    region = Column(String)