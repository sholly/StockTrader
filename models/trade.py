import enum
from sqlalchemy import Column, String, Integer, DateTime, Enum, Numeric
from decimal import *
from . import base
class TradeType(enum.Enum):
    buy = 'buy'
    sell = 'sell'

class Trade(base.Base):
    __tablename__ = 'trades'

    id = Column(Integer, primary_key=True)
    symbol = Column(String)
    price = Column(Numeric(precision=8, scale=2))
    quantity = Column(Integer)
    tradetype = Column(Enum(TradeType))
    tradetime = Column(DateTime)

    def __init__(self, symbol, price, quantity, tradetype, tradetime):
        self.symbol = symbol
        self.price = price
        self.quantity = quantity
        self.tradetype = tradetype
        self.tradetime = tradetime

    def as_dict(self):
        results = {}
        for c in self.__table__.columns:
            results[c.name] = str(getattr(self, c.name))
        return results
