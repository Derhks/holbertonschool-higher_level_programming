from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(autoincrement=True, Integer, nullable=False, primary_key=True)
    name = Column(Strign(128), nullable=False)
