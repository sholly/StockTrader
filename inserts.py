#!/usr/bin/env python3
from datetime import datetime
from models.trade import Trade, TradeType
from models.trade import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def createSession():
    engine = create_engine('postgresql://user:pass@localhost:5432/stocktrader')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

def insert():
    session = createSession()
    trade_date = datetime.now()
    ibm_buy = Trade('IBM', 135.50,50, TradeType.buy, trade_date)
    session.add(ibm_buy)

    ibm_sell = Trade('IBM', 138, 50, TradeType.sell, trade_date)
    session.add(ibm_sell)
    session.commit()
    session.close()

if __name__ == '__main__':
    insert()
