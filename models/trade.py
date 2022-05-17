from sqlalchemy import Column, String, Integer, Date, Enum
from base import Base
class TradeType(enum.Enum):
    buy = 1,
    sell = 2

class Trade(Base):
    __tablename__ = 'trades'

    id = Column(Integer, primary_key=True)
    symbol = Column(String)
    price = Column(Numeric(precision=8, scale=2))
    tradetype = Column(Enum(TradeType))
    tradetime = Column(Date)
