#!/usr/bin/env python3
from flask import Flask
from flask_restful import Resource, Api
from datetime import datetime
from models.trade import Trade, TradeType
from models.trade import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
SQL_USER="user"
SQL_PASS="pass"
SQL_HOST="localhost"
SQL_PORT="5432"
SQL_DATABASE="stocktrader"



app = Flask(__name__)
api = Api(app)

class DBSession():
    def __init__():
        self.session = self.createSession()

    def createSession():
      conn_string = "postgresql://{}:{}@{}:{}/{}"\
        .format(SQL_USER, SQL_PASS, SQL_HOST, SQL_PORT, SQL_DATABASE)
      engine = create_engine(conn_string)
      Base.metadata.create_all(engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      return session
    def getSession(): 
        return session

class Trade(Resource):
    def get(self):
        dbSession = DBSession()
        self.session = dbSession.getSession()
        return {'hello':'world'}

api.add_resource(Trade, '/trade')

if __name__ == '__main__':
    app.run(debug=True)

