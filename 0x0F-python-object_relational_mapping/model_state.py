from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):  # inherits from Base
    __tablename__ = 'states'  # links to the MySQL table states
    id = Column(autoincrement=True, Integer, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
