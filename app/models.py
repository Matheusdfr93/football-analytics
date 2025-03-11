from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Player(Base):  
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    id_position = Column(Integer, ForeignKey("positions.id"), nullable=False)
    age = Column(Integer, nullable=False)
    is_base = Column(Boolean, default=False)
    is_loaned = Column(Boolean, default=False)

    position = relationship("Position", back_populates="players")


class Position(Base):
    __tablename__ = "positions"

    id = Column(Integer, primary_key=True)
    position_name = Column(String, unique=True, nullable=False)
    cd_position = Column(String, unique=True, nullable=False)    

    players = relationship("Player", back_populates="position")