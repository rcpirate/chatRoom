# -*-cod:utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

import os
from settings import DATABASE

engine = None
Session = None

Base = declarative_base()

class User(Base):
    Uid = Column(Integer,primary_key=True)
    NickName = Column(String)
    
    def __init__(self,uid,nickname):
        self.Uid = uid
        self.NickName = nickname
    
    __tablename__ = 'User'
    
    def __repr__(self):
        return '<MetaData("%s","%s")>' % (self.Uid,self.NickName)
    
    
def create_database():
    global enigne
    if DATABASE['engine'] == 'sqlite':
        engine = create_engine('sqlite:///'+DATABASE['address'], echo=True)
    if not engine:
        raise Exception('create sqlite database failed,please validate the DATABASE config')
    if not os.path.exists(DATABASE['address']):
        Base.metadata.create_all(engine)
    
    global Session
    Session = sessionmaker(bind=engine)

if not Session:
    create_database()

    
if __name__ == '__main__':
    create_database()