# -*-cod:utf-8 -*-

from settings import *
from sqlalchemy import create_engine

def create_db(type):
    db_type = {'sqlite':'sqlite://'}
    try:
        return create_engine(db_type[type]+DATABASE[type])
    except:
        raise 'open database failed ...'

if __name__ == '__main__':
    pass