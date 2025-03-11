from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship,backref
from database import Base

class User(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    id_position = Column(Integer, ForeignKey("positions.id"), nullable=False)
    age = Column(Integer)
    is_base = Column(Boolean)
    is_loaned = Column(Boolean)
    position = relationship("Position", back_populates="players")


class Position(Base):
    __tablename__ = "positions"

    id = Column(Integer, primary_key = True)
    position_name = Column(String, unique = True)
    cd_position = Column(String, unique=True)    
    players = relationship("Player", back_populates="position")
