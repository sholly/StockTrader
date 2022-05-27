#!/usr/bin/env python3
from datetime import datetime
import json
from decimal import * 
from flask import Flask
from flask_restful import Resource, Api, reqparse
from models.base import Base
from models.trade import Trade, TradeType
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
SQL_USER="user"
SQL_PASS="pass"
SQL_HOST="localhost"
SQL_PORT="5432"
SQL_DATABASE="stocktrader"



app = Flask(__name__)
api = Api(app)
print(dir(Trade))

class DBSession():
    def __init__(self):
        pass

    def createSession(self):
      conn_string = "postgresql://{}:{}@{}:{}/{}"\
        .format(SQL_USER, SQL_PASS, SQL_HOST, SQL_PORT, SQL_DATABASE)
      engine = create_engine(conn_string)
      Base.metadata.create_all(engine)
      Session = sessionmaker(bind=engine)
      return Session

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        # just stringify the damn thing
        if isinstance(obj, Decimal):
            return str(obj)
        return json.JSONEncoder.default(self, obj)

class TradeController(Resource):
    def get(self):
        dbSession = DBSession()
        Session = dbSession.createSession()
        session = Session()
        results = []
        print(dir)
        trades = session.query(Trade).all()
        for trade in trades: 
            results.append(trade.as_dict())
        return results

    def post(self):
        dbSession = DBSession()
        Session = dbSession.createSession()
        session = Session()

        parser = reqparse.RequestParser()
        parser.add_argument('symbol')
        parser.add_argument('price')
        parser.add_argument('quantity')
        parser.add_argument('tradetype')
        args = parser.parse_args()
        print(args)
        symbol = args['symbol']
        price = args['price']
        quantity = args['quantity']
        ttype = str(args['tradetype'])
        tradetype
        if ttype.lower() == "BUY":
            tradetype = TradeType.buy
        else:
            tradetype = TradeType.sell

        trade = Trade(symbol, price, quantity, tradetype, datetime.now())
        session.add(trade)
        session.commit()
        session.close()



api.add_resource(TradeController, '/trade')

if __name__ == '__main__':
    app.run(debug=True)

